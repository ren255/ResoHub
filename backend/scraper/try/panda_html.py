import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()


import pandas as pd
from core.models import TextFileStorage
from core.services import CachedHttpClient

session = CachedHttpClient()

print("Libraries loaded")

# %%
url = "https://syllabus.kosen-k.go.jp/Pages/PublicSyllabus?school_id=14&department_id=13&subject_id=0039&year=2024&lang=ja"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

html = session.get(url, headers=headers)

tables = pd.read_html(html)

# %%
# table_4を取得
df = tables[4].copy()

print("元のデータ:")
print(df.head())
print(f"\n形状: {df.shape}")
print(f"\n列名: {df.columns.tolist()}")

# %%
# MultiIndexの列を平坦化
if isinstance(df.columns, pd.MultiIndex):
    # 最初の行（ヘッダー情報）を取得
    header_row = df.columns.get_level_values(0).tolist()

    # 新しい列名を設定
    df.columns = ["学期", "クォーター", "週", "授業内容", "週ごとの到達目標"]

    print("\n列名を修正しました")
    print(df.columns.tolist())

# %%
# 結合セルを前方埋め（forward fill）で処理
df["学期"] = df["学期"].replace("Unnamed.*", pd.NA, regex=True).ffill()
df["クォーター"] = df["クォーター"].replace("Unnamed.*", pd.NA, regex=True).ffill()

# 不要な行を削除（全てがUnnamed or 空の行）
df = df[
    ~(
        df["週"].astype(str).str.contains("Unnamed|^$", na=False)
        & df["授業内容"].astype(str).str.contains("Unnamed|^$", na=False)
    )
]

# インデックスをリセット
df = df.reset_index(drop=True)

print("\nクリーニング後のデータ:")
print(df)

# %%
# TextFileStorageに保存
from django.contrib.auth import get_user_model

User = get_user_model()

# 保存するユーザーを取得（適切なユーザーIDまたは取得方法に変更してください）
user = User.objects.first()  # または特定のユーザーを取得
if not user:
    raise ValueError("保存するユーザーが見つかりません")

# CSVデータを文字列として生成
csv_content = df.to_csv(index=False, encoding="utf-8")

# ファイルキーを設定
file_key = "tables/table_4_cleaned.csv"

# 既存のレコードを検索（更新または新規作成）
text_file, created = TextFileStorage.objects.update_or_create(
    key=file_key,
    defaults={
        'body': csv_content,
        'created_by': user,
        'mine_type': 'text/csv',  # CSVファイルのMIMEタイプ
        'is_deleted': False,
    }
)

if created:
    print(f"\n新規作成: {file_key}")
else:
    print(f"\n更新: {file_key}")

print(f"ID: {text_file.id}")
print(f"ファイルサイズ: {text_file.file_size} バイト")
print(f"MIME Type: {text_file.mine_type}")
print(f"行数: {len(df)}, 列数: {len(df.columns)}")
print(f"作成日時: {text_file.created_at}")
print(f"更新日時: {text_file.updated_at}")

# %%
# 保存されたデータを確認
stored_file = TextFileStorage.objects.get(key=file_key)
print("\n保存されたファイル情報:")
print(f"Key: {stored_file.key}")
print(f"Size: {stored_file.file_size} bytes")
print(f"Extension: {stored_file.get_extension()}")
print(f"Is Deleted: {stored_file.is_deleted}")
print(f"\nBody preview (first 200 chars):")
print(stored_file.body[:200] + "...")