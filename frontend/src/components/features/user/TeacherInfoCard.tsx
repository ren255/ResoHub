import type { TeacherInfo } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const TeacherInfoCard = ({ info }: { info: TeacherInfo }) => (
    <div className="card bg-base-100 shadow-sm border border-base-300">
        <div className="card-body">
            <h2 className="card-title text-xl">教師情報</h2>
            <div className="space-y-1 text-sm">
                <p>
                    <span className="text-gray-500">ユーザー:</span>{" "}
                    <Link
                        to={`/users/${info.user}`}
                        className="link link-primary hover:underline"
                    >
                        {info.user_name}
                    </Link>
                </p>
                {info.department && (
                    <p>
                        <span className="text-gray-500">学部:</span>{" "}
                        <Link
                            to={`/departments/${info.department}`}
                            className="link link-primary hover:underline"
                        >
                            {info.department_name}
                        </Link>
                    </p>
                )}
                {info.department_type && (
                    <p>
                        <span className="text-gray-500">職種:</span> {info.department_type}
                    </p>
                )}
                {info.owner && (
                    <p>
                        <span className="badge badge-sm badge-accent">オーナー</span>
                    </p>
                )}
                {info.subdomain && (
                    <p>
                        <span className="text-gray-500">サブドメイン:</span> {info.subdomain}
                    </p>
                )}
                {info.subjects.length > 0 && (
                    <p>
                        <span className="text-gray-500">担当教科:</span>{" "}
                        {info.subjects.length}科目
                    </p>
                )}
            </div>
        </div>
    </div>
);
