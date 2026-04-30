import type { SyllabusDepartment } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const SyllabusDepartmentCard = ({
    syllabusDepartment,
}: {
    syllabusDepartment: SyllabusDepartment;
}) => (
    <div className="card bg-base-100 shadow-sm border border-base-300 max-w-100">
        <div className="card-body">
            <h2 className="card-title text-xl">{`${syllabusDepartment.admission_year}年入学${syllabusDepartment.name}`}</h2>
            <div className="flex gap-2 text-sm">
                <Link
                    to={`/schools/${syllabusDepartment.school}`}
                    className="link link-primary hover:underline"
                >
                    {syllabusDepartment.school_name}
                </Link>

                <Link
                    to={`/departments/${syllabusDepartment.department}`}
                    className="link link-primary hover:underline"
                >
                    {syllabusDepartment.department_name}
                </Link>

                <a
                    href={syllabusDepartment.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="link link-primary hover:underline"
                >
                    シラバス
                </a>
            </div>
        </div>
    </div>
);
