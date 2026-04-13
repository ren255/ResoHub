import { useMemo } from "react";
import { ColumnDef } from "@tanstack/react-table";
import { DataTable } from "../../ui/DataTable";
import { User } from "../../../types/User";

interface UserTableProps {
  users: User[];
  isLoading?: boolean;
  onUserClick: (user: User) => void;
}

export default function UserTable({
  users,
  isLoading,
  onUserClick,
}: UserTableProps) {
  const columns = useMemo<ColumnDef<User>[]>(
    () => [
      {
        accessorKey: "username",
        header: "ユーザー名",
        cell: ({ row }) => (
          <span className="font-medium">{row.original.username}</span>
        ),
      },
      {
        accessorKey: "email",
        header: "メールアドレス",
      },
      {
        accessorKey: "is_staff",
        header: "スタッフ",
        cell: ({ row }) =>
          row.original.is_staff ? (
            <span className="badge badge-success badge-sm">有効</span>
          ) : (
            <span className="badge badge-ghost badge-sm">無効</span>
          ),
      },
      {
        accessorKey: "is_superuser",
        header: "スーパーユーザー",
        cell: ({ row }) =>
          row.original.is_superuser ? (
            <span className="badge badge-error badge-sm">有効</span>
          ) : (
            <span className="badge badge-ghost badge-sm">無効</span>
          ),
      },
      {
        accessorKey: "date_joined",
        header: "登録日",
        cell: ({ row }) =>
          new Date(row.original.date_joined).toLocaleDateString("ja-JP"),
      },
      {
        id: "actions",
        header: "操作",
        cell: ({ row }) => (
          <button
            className="btn btn-sm btn-ghost"
            onClick={() => onUserClick(row.original)}
          >
            詳細
          </button>
        ),
      },
    ],
    [onUserClick]
  );

  return <DataTable data={users} columns={columns} isLoading={isLoading} />;
}
