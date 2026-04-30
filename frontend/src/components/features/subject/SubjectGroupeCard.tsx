import type { SubjectGroupe } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const SubjectGroupeCard = ({
    subjectGroupe,
}: {
    subjectGroupe: SubjectGroupe;
}) => (
    <div className="card bg-base-100 shadow-sm border border-base-300">
        <div className="card-body">
            <h2 className="card-title text-xl"> {subjectGroupe.name}</h2>
            <div className="space-y-1 text-sm">
                <p>
                    <span className="text-gray-500">subject ctn:</span> {subjectGroupe.subjects?.length || 0}
                </p>
                <p>
                    <span className="text-gray-500">teacher ctn:</span> {subjectGroupe.teachers?.length || 0}
                </p>
            </div>
        </div>
    </div>
);
