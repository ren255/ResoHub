import type { TeacherInfo } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const TeacherInfoCard = ({ info }: { info: TeacherInfo }) => (
    <div className="card bg-base-100 shadow-sm border border-base-300 max-w-100">
        <div className="card-body">
            <h2 className="card-title text-xl"><Link
                to={`/users/${info.user}`}
                className="link link-primary hover:underline"
            >
                {info.user_name}
            </Link></h2>
            <div className="flex gap-2 text-sm">
                <span className="text-gray-500">学科:</span>
                {info.department_type}
                <Link
                    to={`/departments/${info.department}`}
                    className="link link-primary hover:underline"
                >
                    {info.department_name}
                </Link>
                <span className="text-gray-500">担当教科数:</span>{" "}
                {info.subjects.length}
            </div>
        </div>
    </div >
);
