import type { SubjectGroupe } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const SubjectGroupeCard = ({
    subjectGroupe,
}: {
    subjectGroupe: SubjectGroupe;
}) => (
    <div className="card bg-base-100 shadow-sm border border-base-300">
        <div className="card-body">
            <h2 className="card-title text-xl">教科グループ {subjectGroupe.id}</h2>
            <div className="space-y-1 text-sm">
                <p>
                    <span className="text-gray-500">ID:</span> {subjectGroupe.id}
                </p>
            </div>
        </div>
    </div>
);
