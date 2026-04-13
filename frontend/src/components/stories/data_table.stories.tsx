import { useState } from "react";
import { ColumnDef } from "@tanstack/react-table";
import { DataTable } from "@ui/DataTable";

// データ型定義
interface User {
  id: number;
  name: string;
  email: string;
  role: string;
  createdAt: string;
}

interface Product {
  id: number;
  name: string;
  price: number;
  stock: number;
}

// ユーザーカラム定義
const userColumns: ColumnDef<User>[] = [
  {
    accessorKey: "id",
    header: "ID",
  },
  {
    accessorKey: "name",
    header: "名前",
  },
  {
    accessorKey: "email",
    header: "メールアドレス",
  },
  {
    accessorKey: "role",
    header: "役割",
  },
  {
    accessorKey: "createdAt",
    header: "作成日",
  },
];

// 商品カラム定義
const productColumns: ColumnDef<Product>[] = [
  {
    accessorKey: "id",
    header: "ID",
  },
  {
    accessorKey: "name",
    header: "商品名",
  },
  {
    accessorKey: "price",
    header: "価格",
    cell: ({ row }) => `¥${row.original.price.toLocaleString()}`,
  },
  {
    accessorKey: "stock",
    header: "在庫数",
  },
];

// サンプルデータ
const users: User[] = [
  {
    id: 1,
    name: "田中太郎",
    email: "tanaka@example.com",
    role: "管理者",
    createdAt: "2024-01-15",
  },
  {
    id: 2,
    name: "佐藤花子",
    email: "sato@example.com",
    role: "ユーザー",
    createdAt: "2024-02-20",
  },
  {
    id: 3,
    name: "鈴木一郎",
    email: "suzuki@example.com",
    role: "ユーザー",
    createdAt: "2024-03-10",
  },
];

// 1000行の商品データを生成
const generateProducts = (): Product[] => {
  const productNames = [
    "ノートPC",
    "マウス",
    "キーボード",
    "モニター",
    "ヘッドセット",
    "Webカメラ",
    "スピーカー",
    "マイク",
    "外付けHDD",
    "USBメモリ",
    "充電器",
    "ケーブル",
    "スタンド",
    "バッグ",
    "マット",
  ];

  return Array.from({ length: 1000 }, (_, i) => ({
    id: i + 1,
    name: `${productNames[Math.floor(Math.random() * productNames.length)]} ${i + 1
      }`,
    price: Math.floor(Math.random() * 50000) + 1000,
    stock: Math.floor(Math.random() * 100),
  }));
};

const products = generateProducts();

// ユーザーリスト
export function UserList() {
  const [isLoading, setIsLoading] = useState(false);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">ユーザー一覧</h1>
      <DataTable data={users} columns={userColumns} isLoading={isLoading} />
    </div>
  );
}

// 商品リスト（1000行）
export function ProductList() {
  const [isLoading, setIsLoading] = useState(false);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">商品一覧（1000件）</h1>
      <DataTable
        data={products}
        columns={productColumns}
        isLoading={isLoading}
      />
    </div>
  );
}
