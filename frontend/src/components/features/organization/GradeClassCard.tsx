import type { GradeClass } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const GradeClassCard = ({ gradeClass }: { gradeClass: GradeClass }) => (
    <div className="card bg-base-100 shadow-sm border border-base-300">
        <div className="card-body">
            <h2 className="card-title text-xl">
                {gradeClass.grade_str || `${gradeClass.grade}年`}
            </h2>
            <div className="space-y-1 text-sm">
                <p>
                    <span className="text-gray-500">クラス:</span>{" "}
                    <Link
                        to={`/school-classes/${gradeClass.school_class}`}
                        className="link link-primary hover:underline"
                    >
                        {gradeClass.school_class_str}
                    </Link>
                </p>
                <p>
                    <span className="text-gray-500">年度:</span> {gradeClass.year}年
                </p>
                <p>
                    <span className="text-gray-500">補正学年:</span> {gradeClass.grade}
                </p>
            </div>
        </div>
    </div>
);
