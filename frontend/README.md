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
| 型システム | TypeScript（Django APIからの型定義を使用） |

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


## Ladle（コンポーネントカタログ）

[Ladle](https://ladle.dev/)を使用して、コンポーネントの開発とテストを行います。

```sh
# Ladleサーバーの起動
npm run ladle
```

ストーリーファイルは `src/components/stories/` に配置しています。

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
