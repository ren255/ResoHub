import type { SchoolClass } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const SchoolClassCard = ({ schoolClass }: { schoolClass: SchoolClass }) => (
    <div className="card bg-base-100 shadow-sm border border-base-300">
        <div className="card-body">
            <h2 className="card-title text-xl">{schoolClass.syllabus_department_name}</h2>
            <div className="space-y-1 text-sm">
                <p>
                    <span className="text-gray-500">学部:</span>{" "}
                    <Link
                        to={`/departments/${schoolClass.department}`}
                        className="link link-primary hover:underline"
                    >
                        {schoolClass.department_name}
                    </Link>
                </p>
                <p>
                    <span className="text-gray-500">シラバス学部:</span>{" "}
                    <Link
                        to={`/syllabus-departments/${schoolClass.syllabus_department}`}
                        className="link link-primary hover:underline"
                    >
                        {schoolClass.syllabus_department_name}
                    </Link>
                </p>
                <p>
                    <span className="text-gray-500">入学年度:</span> {schoolClass.admission_year}年
                </p>
            </div>
        </div>
    </div>
);
