import type { User } from "@/types/api/types.gen";

export const UserCard = ({ user }: { user: User }) => (
    <div className="card bg-base-100 shadow-sm border border-base-300">
        <div className="card-body">
            <h2 className="card-title text-xl">{user.name || user.username}</h2>
            <div className="space-y-1 text-sm">
                <p>
                    <span className="text-gray-500">メール:</span> {user.email}
                </p>
                <p>
                    <span className="text-gray-500">役割:</span>{" "}
                    <span className="badge badge-sm badge-primary">{user.role}</span>
                </p>
                <p>
                    <span className="text-gray-500">登録日:</span>{" "}
                    {user.date_joined
                        ? new Date(user.date_joined).toLocaleDateString("ja-JP")
                        : "-"}
                </p>
                {user.is_staff && (
                    <p>
                        <span className="badge badge-sm badge-secondary">スタッフ</span>
                    </p>
                )}
            </div>
        </div>
    </div>
);
