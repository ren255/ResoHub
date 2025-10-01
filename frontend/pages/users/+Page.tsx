import { useState, useEffect } from "react";
import axios from "axios";
import UserModal from "../../components/UserModal";

interface User {
  uuid: string;
  username: string;
  email: string;
  is_staff: boolean;
  is_superuser: boolean;
  date_joined: string;
}

export default function Page() {
  const [users, setUsers] = useState<User[]>([]);
  const [selectedUser, setSelectedUser] = useState<User | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await axios.get("/api/user/");
      setUsers(response.data);
    } catch (err) {
      setError("ユーザー情報の取得に失敗しました");
      console.error("Error fetching users:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleUserClick = (user: User) => {
    setSelectedUser(user);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setSelectedUser(null);
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center min-h-screen">
        <span className="loading loading-spinner loading-lg"></span>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex justify-center items-center min-h-screen">
        <div className="alert alert-error max-w-md">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="stroke-current shrink-0 h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
          <span>{error}</span>
        </div>
      </div>
    );
  }

  return (
    <div className="container mx-auto p-4">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">ユーザー一覧</h1>
        <button className="btn btn-primary" onClick={fetchUsers}>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-5 w-5"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              fillRule="evenodd"
              d="M4 2a1 1 0 011 1v2.101a7.002 7.002 0 0111.601 2.566 1 1 0 11-1.885.666A5.002 5.002 0 005.999 7H9a1 1 0 010 2H4a1 1 0 01-1-1V3a1 1 0 011-1zm.008 9.057a1 1 0 011.276.61A5.002 5.002 0 0014.001 13H11a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0v-2.101a7.002 7.002 0 01-11.601-2.566 1 1 0 01.61-1.276z"
              clipRule="evenodd"
            />
          </svg>
          更新
        </button>
      </div>

      <div className="overflow-x-auto">
        <table className="table table-zebra w-full">
          <thead>
            <tr>
              <th>ユーザー名</th>
              <th>メールアドレス</th>
              <th>スタッフ</th>
              <th>スーパーユーザー</th>
              <th>登録日</th>
              <th>操作</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user) => (
              <tr key={user.uuid} className="hover">
                <td className="font-medium">{user.username}</td>
                <td>{user.email}</td>
                <td>
                  {user.is_staff ? (
                    <span className="badge badge-success badge-sm">有効</span>
                  ) : (
                    <span className="badge badge-ghost badge-sm">無効</span>
                  )}
                </td>
                <td>
                  {user.is_superuser ? (
                    <span className="badge badge-error badge-sm">有効</span>
                  ) : (
                    <span className="badge badge-ghost badge-sm">無効</span>
                  )}
                </td>
                <td>
                  {new Date(user.date_joined).toLocaleDateString("ja-JP")}
                </td>
                <td>
                  <button
                    className="btn btn-sm btn-ghost"
                    onClick={() => handleUserClick(user)}
                  >
                    詳細
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {users.length === 0 && (
        <div className="text-center py-12">
          <p className="text-gray-500">ユーザーが見つかりませんでした</p>
        </div>
      )}

      <UserModal
        user={selectedUser}
        isOpen={isModalOpen}
        onClose={handleCloseModal}
      />
    </div>
  );
}
