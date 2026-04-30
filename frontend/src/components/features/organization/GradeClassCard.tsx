import type { GradeClass } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const GradeClassCard = ({ gradeClass }: { gradeClass: GradeClass }) => (
    <div className="card bg-base-100 shadow-sm border border-base-300 max-w-100">
        <div className="card-body">
            <h2 className="card-title text-xl">
                <Link
                    to={`/school-classes/${gradeClass.school_class}`}
                    className="link link-primary hover:underline"
                >
                    {gradeClass.school_class_str}
                </Link>
                {`${gradeClass.grade}年`}
            </h2>
        </div>
    </div>
);
