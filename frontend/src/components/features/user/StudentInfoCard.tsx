import type { StudentInfo } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const StudentInfoCard = ({ info }: { info: StudentInfo }) => (
    <div className="card bg-base-100 shadow-sm border border-base-300">
        <div className="card-body">
            <h2 className="card-title text-xl">生徒情報</h2>
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
                <p>
                    <span className="text-gray-500">学籍番号:</span> {info.student_id}
                </p>
                {info.school_class && (
                    <p>
                        <span className="text-gray-500">クラス:</span>{" "}
                        <Link
                            to={`/school-classes/${info.school_class}`}
                            className="link link-primary hover:underline"
                        >
                            {info.school_class_str}
                        </Link>
                    </p>
                )}
            </div>
        </div>
    </div>
);
