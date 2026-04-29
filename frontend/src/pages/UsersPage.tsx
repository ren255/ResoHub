import { useState, useEffect } from "react";
import { userList } from "@/types/api/sdk.gen";
import UserTable from "@features/user/UserTable";
import UserModal from "@features/user/UserModal";
import type { User } from "@/types/api/types.gen";

export default function Page() {
  const [users, setUsers] = useState<User[]>([]);
  const [selectedUser, setSelectedUser] = useState<User | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        setLoading(true);
        setError(null);
        const { data } = await userList();
        if (data) {
          setUsers(data);
        }
      } catch (err) {
        setError("ユーザー情報の取得に失敗しました");
        console.error("Error fetching users:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  const handleUserClick = (user: User) => {
    setSelectedUser(user);
    setIsModalOpen(true);
  };

  if (error) {
    return (
      <div className="p-8">
        <div className="text-red-600">{error}</div>
      </div>
    );
  }

  return (
    <div className="p-8">
      <h2 className="text-2xl font-bold mb-4">ユーザー管理</h2>
      <UserTable
        users={users}
        isLoading={loading}
        onUserClick={handleUserClick}
      />
      <UserModal
        user={selectedUser}
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
      />
    </div>
  );
}
