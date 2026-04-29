import type { ExamGroupe } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const ExamGroupeCard = ({ examGroupe }: { examGroupe: ExamGroupe }) => (
    <div className="card bg-base-100 shadow-sm border border-base-300">
        <div className="card-body">
            <h2 className="card-title text-xl">試験グループ {examGroupe.id}</h2>
            <div className="space-y-1 text-sm">
                <p>
                    <span className="text-gray-500">教科:</span>{" "}
                    <Link
                        to={`/subjects/${examGroupe.subject}`}
                        className="link link-primary hover:underline"
                    >
                        {examGroupe.subject_name}
                    </Link>
                </p>
                <p>
                    <span className="text-gray-500">教科グループ:</span>{" "}
                    <Link
                        to={`/subject-groupes/${examGroupe.subject_groupe}`}
                        className="link link-primary hover:underline"
                    >
                        グループ {examGroupe.subject_groupe}
                    </Link>
                </p>
            </div>
        </div>
    </div>
);
