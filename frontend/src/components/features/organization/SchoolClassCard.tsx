import type { SchoolClass } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const SchoolClassCard = ({ schoolClass }: { schoolClass: SchoolClass }) => (
    <div className="card bg-base-100 shadow-sm border border-base-300 max-w-100">
        <div className="card-body">
            <h2 className="card-title text-xl">{`${schoolClass.admission_year}入学`}
                <Link
                    to={`/departments/${schoolClass.department}`}
                    className="link link-primary hover:underline"
                >
                    {schoolClass.department_name}
                </Link>
            </h2>
        </div>
    </div >
);
