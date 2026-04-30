import type { StudentInfo } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const StudentInfoCard = ({ info }: { info: StudentInfo }) => (
    <div className="card bg-base-100 shadow-sm border border-base-300 max-w-100">
        <div className="card-body">
            <h2 className="card-title text-xl"><Link
                to={`/profile/${info.user}`}
                className="link link-primary hover:underline"
            >
                {info.user_name}
            </Link></h2>

            <div className="space-y-1 text-sm">
                <Link
                    to={`/school-classes/${info.school_class}`}
                    className="link link-primary hover:underline"
                >
                    {info.school_class_str}
                </Link>
                <p>
                    <span className="text-gray-500">学籍番号:</span> {info.student_id}
                </p>
            </div>
        </div>
    </div>
);
