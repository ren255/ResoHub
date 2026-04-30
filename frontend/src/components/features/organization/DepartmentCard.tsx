import type { Department } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const DepartmentCard = ({ department }: { department: Department }) => (
    <div className="card bg-base-100 shadow-sm border border-base-300 max-w-100">
        <div className="card-body">
            <h2 className="card-title text-xl">{department.name}</h2>
            <div className="space-y-1 text-sm">
                <Link
                    to={`/schools/${department.school}`}
                    className="link link-primary hover:underline"
                >
                    {department.school_name}
                </Link>
            </div>
        </div>
    </div>
);
