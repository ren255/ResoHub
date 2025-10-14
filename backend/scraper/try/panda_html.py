# %%
import pandas as pd
import requests
from io import StringIO
import os

print("Libraries loaded")

# %%
url = "https://syllabus.kosen-k.go.jp/Pages/PublicSyllabus?school_id=14&department_id=13&subject_id=0039&year=2024&lang=ja"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

tables = pd.read_html(StringIO(response.text))

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
# 保存
os.makedirs("./tables", exist_ok=True)
output_path = "./tables/table_4_cleaned.csv"
df.to_csv(output_path, index=False, encoding="utf-8-sig")
print(f"\n保存完了: {output_path}")
print(f"行数: {len(df)}, 列数: {len(df.columns)}")

# %%
