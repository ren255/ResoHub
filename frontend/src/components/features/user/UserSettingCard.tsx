import type { UserSetting } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const UserSettingCard = ({ setting }: { setting: UserSetting }) => (
    <div className="card bg-base-100 shadow-sm border border-base-300">
        <div className="card-body">
            <h2 className="card-title text-xl">ユーザー設定</h2>
            <div className="space-y-1 text-sm">
                <p>
                    <span className="text-gray-500">ユーザー:</span>{" "}
                    <Link
                        to={`/users/${setting.user}`}
                        className="link link-primary hover:underline"
                    >
                        {setting.user_name}
                    </Link>
                </p>
            </div>
        </div>
    </div>
);
