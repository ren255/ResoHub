import type { SyllabusDepartment } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const SyllabusDepartmentCard = ({
    syllabusDepartment,
}: {
    syllabusDepartment: SyllabusDepartment;
}) => (
    <div className="card bg-base-100 shadow-sm border border-base-300">
        <div className="card-body">
            <h2 className="card-title text-xl">{syllabusDepartment.name}</h2>
            <div className="space-y-1 text-sm">
                <p>
                    <span className="text-gray-500">学校:</span>{" "}
                    <Link
                        to={`/schools/${syllabusDepartment.school}`}
                        className="link link-primary hover:underline"
                    >
                        {syllabusDepartment.school_name}
                    </Link>
                </p>
                {syllabusDepartment.department && (
                    <p>
                        <span className="text-gray-500">学部:</span>{" "}
                        <Link
                            to={`/departments/${syllabusDepartment.department}`}
                            className="link link-primary hover:underline"
                        >
                            {syllabusDepartment.department_name}
                        </Link>
                    </p>
                )}
                <p>
                    <span className="text-gray-500">入学年度:</span>{" "}
                    {syllabusDepartment.admission_year}年
                </p>
                <p>
                    <span className="text-gray-500">コード:</span> {syllabusDepartment.code}
                </p>
                {syllabusDepartment.url && (
                    <p>
                        <span className="text-gray-500">URL:</span>{" "}
                        <a
                            href={syllabusDepartment.url}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="link link-primary hover:underline"
                        >
                            リンク
                        </a>
                    </p>
                )}
            </div>
        </div>
    </div>
);
