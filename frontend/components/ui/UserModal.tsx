import { User } from "../../types/User";

interface UserModalProps {
  user: User | null;
  isOpen: boolean;
  onClose: () => void;
}

export default function UserModal({ user, isOpen, onClose }: UserModalProps) {
  if (!user) return null;

  return (
    <dialog className={`modal ${isOpen ? "modal-open" : ""}`}>
      <div className="modal-box">
        <h3 className="font-bold text-lg mb-4">ユーザー詳細</h3>

        <div className="space-y-3">
          <div>
            <span className="text-sm text-gray-500">ユーザー名</span>
            <p className="font-medium">{user.username}</p>
          </div>

          <div>
            <span className="text-sm text-gray-500">メールアドレス</span>
            <p className="font-medium">{user.email}</p>
          </div>

          <div>
            <span className="text-sm text-gray-500">UUID</span>
            <p className="font-mono text-sm">{user.uuid}</p>
          </div>

          <div>
            <span className="text-sm text-gray-500">権限</span>
            <div className="flex gap-2 mt-1">
              {user.is_staff && (
                <span className="badge badge-success">スタッフ</span>
              )}
              {user.is_superuser && (
                <span className="badge badge-error">スーパーユーザー</span>
              )}
              {!user.is_staff && !user.is_superuser && (
                <span className="badge badge-ghost">一般ユーザー</span>
              )}
            </div>
          </div>

          <div>
            <span className="text-sm text-gray-500">登録日</span>
            <p className="font-medium">
              {new Date(user.date_joined).toLocaleString("ja-JP")}
            </p>
          </div>
        </div>

        <div className="modal-action">
          <button className="btn" onClick={onClose}>
            閉じる
          </button>
        </div>
      </div>

      <form method="dialog" className="modal-backdrop">
        <button onClick={onClose}>close</button>
      </form>
    </dialog>
  );
}
