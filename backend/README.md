# ResoHub バックエンド

Django + Django REST Framework で構築されたResoHubのバックエンドAPIサーバーです。

## アクセスURL

| サービス | URL |
|---------|-----|
| Django Admin | http://localhost:8001/admin |
| APIドキュメント | http://localhost:8001/api/docs |
| MinIOダッシュボード | http://localhost:9001/ |
| Scrapyd | http://127.0.0.1:6800/ |

## 開発環境

### データベース接続

```bash
# DBコンテナに入る
docker compose exec -it db bash

# MySQLクライアントで接続
mysql -u root -proot

# データベース一覧を表示
show databases;
```

### migration

```sh
python manage.py makemigrations content
```

```sh
python manage.py migrate
```

### Scrapydの起動

```bash
scrapyd
```

参考: [How to use Scrapy with Django Application](https://alioguzhan.medium.com/how-to-use-scrapy-with-django-application-c16fabd0e62e)

## ER図の生成

```bash
python manage.py graph_models -a --group-models -o image/er_diagram.png
```

## ユーザーインポート

### 1. Teamsエクスポートサービスの起動

```bash
cd teams_export
docker compose up
```

### 2. ユーザーインポートスクリプトの実行

```bash
cd backend
docker compose exec backend python -m scripts.import_users
```

## Scrapyの実行

### 1. バックエンドコンテナに入る

```bash
cd backend
docker compose exec backend zsh
```

### 2. Scrapy用ユーザーの作成（初回のみ）

```bash
python manage.py shell -c \
  "from django.contrib.auth import get_user_model; \
  User = get_user_model(); \
  User.objects.create_user('scrapy@example.com', 'scrapy', username='scrapy')"
```

### 3. シラバスクローラーの実行

```bash
cd /app/scraper
python -m launch.syllabus
```

dbへ読み込み再試行
```sh
cd /app/scraper
python -m data_export.exporter --scrape-id
```

### 4. データ前処理

```bash
cd /app
python -m scripts.data_preprocess
```

```sh
python -m scripts.update_groupe
```
