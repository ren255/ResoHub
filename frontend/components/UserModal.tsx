import { useState } from "react";

interface User {
  uuid: string;
  username: string;
  email: string;
  is_staff: boolean;
  is_superuser: boolean;
  date_joined: string;
}

interface UserModalProps {
  user: User | null;
  isOpen: boolean;
  onClose: () => void;
}

const UserModal: React.FC<UserModalProps> = ({ user, isOpen, onClose }) => {
  if (!user) return null;

  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString("ja-JP", {
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
      hour: "2-digit",
      minute: "2-digit",
    });
  };

  return (
    <>
      <input
        type="checkbox"
        id="user-modal"
        className="modal-toggle"
        checked={isOpen}
        onChange={() => {}}
      />
      <div className="modal modal-bottom sm:modal-middle">
        <div className="modal-box">
          <h3 className="font-bold text-lg mb-4">ユーザー詳細</h3>

          <div className="space-y-3">
            <div>
              <span className="font-semibold text-sm text-gray-500">UUID</span>
              <p className="text-sm font-mono bg-base-200 p-2 rounded mt-1 break-all">
                {user.uuid}
              </p>
            </div>

            <div>
              <span className="font-semibold text-sm text-gray-500">
                ユーザー名
              </span>
              <p className="text-base mt-1">{user.username}</p>
            </div>

            <div>
              <span className="font-semibold text-sm text-gray-500">
                メールアドレス
              </span>
              <p className="text-base mt-1">{user.email}</p>
            </div>

            <div className="flex gap-4">
              <div>
                <span className="font-semibold text-sm text-gray-500">
                  スタッフ権限
                </span>
                <div className="mt-1">
                  {user.is_staff ? (
                    <span className="badge badge-success">有効</span>
                  ) : (
                    <span className="badge badge-ghost">無効</span>
                  )}
                </div>
              </div>

              <div>
                <span className="font-semibold text-sm text-gray-500">
                  スーパーユーザー
                </span>
                <div className="mt-1">
                  {user.is_superuser ? (
                    <span className="badge badge-error">有効</span>
                  ) : (
                    <span className="badge badge-ghost">無効</span>
                  )}
                </div>
              </div>
            </div>

            <div>
              <span className="font-semibold text-sm text-gray-500">
                登録日時
              </span>
              <p className="text-base mt-1">{formatDate(user.date_joined)}</p>
            </div>
          </div>

          <div className="modal-action">
            <button className="btn" onClick={onClose}>
              閉じる
            </button>
          </div>
        </div>
        <label className="modal-backdrop" onClick={onClose}>
          閉じる
        </label>
      </div>
    </>
  );
};

export default UserModal;
