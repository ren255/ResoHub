# ResoHub Frontend

ResoHubのフロントエンドアプリケーションです。

## 技術スタック

| 項目 | 技術 |
|------|------|
| ビルドツール | [Vite](https://vitejs.dev/) |
| フレームワーク | [React](https://react.dev/) 19 |
| ルーティング | [React Router](https://reactrouter.com/) v7 |
| スタイリング | [Tailwind CSS](https://tailwindcss.com/) v4 + [DaisyUI](https://daisyui.com/) |
| UIコンポーネントカタログ | [Ladle](https://ladle.dev/) |
| リンター/フォーマッター | [Biome](https://biomejs.dev/) |
| 型システム | [@hey-api/openapi-ts](https://heyapi.dev/) |

## 開発環境のセットアップ

```sh
npm install
```

## 開発サーバーの起動

```sh
# 開発サーバー（Vite）
npm run dev

# Storybook（Ladle）
npm run ladle

# 両方同時に起動
npm run dev:all
```

## ビルド

```sh
npm run build
```

## コード品質

```sh
# リント
npm run lint

# フォーマット
npm run format
```

## プロジェクト構成

```
frontend/
├── src/
│   ├── components/
│   │   ├── features/     # 機能別コンポーネント
│   │   ├── layouts/      # レイアウトコンポーネント
│   │   ├── stories/      # Ladle用ストーリー
│   │   └── ui/           # 共通UIコンポーネント
│   ├── hooks/            # カスタムフック
│   ├── layouts/          # ページレイアウト
│   ├── pages/            # ページコンポーネント
│   ├── types/            # TypeScript型定義（Django API準拠）
│   ├── App.tsx           # アプリケーションルート
│   └── main.tsx          # エントリーポイント
├── vite.config.ts        # Vite設定
├── ladle-vite.config.ts  # Ladle設定
├── openapi-ts.config.ts  # API型定義生成設定
├── biome.json            # Biome設定
└── package.json
```

## ルーティング

[React Router](https://reactrouter.com/) v7を使用しています。

```tsx
// src/App.tsx
<Routes>
    <Route element={<LayoutDefault />}>
        <Route path="/" element={<IndexPage />} />
        <Route path="/users" element={<UsersPage />} />
        <Route path="*" element={<ErrorPage />} />
    </Route>
</Routes>
```

## 型定義

DjangoバックエンドのAPIレスポンスに合わせた型定義を使用しています。

### API型の生成

[@hey-api/openapi-ts](https://heyapi.dev/) を使用して、DjangoのOpenAPIスキーマからTypeScript型とaxiosクライアントを自動生成します。

```sh
# API型とクライアントの生成
npm run generate:api
```

生成されたファイルは `src/types/api/` に出力されます：
- `types.gen.ts` - TypeScript型定義
- `client.gen.ts` - axiosクライアント
- `sdk.gen.ts` - API操作関数

### 設定

`openapi-ts.config.ts` で設定を変更できます：
- 入力: `http://resohub-backend:8000/api/schema/`
- 出力: `src/types/api/`

### 使用例

```ts
import { client } from "@/types/api/client.gen";
import { userList, userRetrieve } from "@/types/api/sdk.gen";


// API呼び出し
const { data: users } = await userList();
const { data: user } = await userRetrieve({ path: { uuid: "xxx" } });
```

## Ladle（コンポーネントカタログ）

[Ladle](https://ladle.dev/)を使用して、コンポーネントの開発とテストを行います。

```sh
# Ladleサーバーの起動
npm run ladle
```

ストーリーファイルは `src/components/stories/` に配置しています。

ladleが真っ白で描画されたときはキャッシュを消してから試してみてください。
```sh
rm -rf node_modules/.vite
```

## エイリアス設定

Viteの設定で以下のパスエイリアスを定義しています：

| エイリアス | パス |
|-----------|------|
| `@` | `./src` |
| `@features` | `./src/components/features` |
| `@layouts` | `./src/components/layouts` |
| `@stories` | `./src/components/stories` |
| `@ui` | `./src/components/ui` |

## プロキシ設定

開発時、APIリクエストは axiosを使用し`http://resohub-backend:8000` にプロキシされます。

```ts
await axios.get("/api/user/");
```
