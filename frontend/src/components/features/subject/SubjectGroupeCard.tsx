import type { SubjectGroupe } from "@/types/api/types.gen";

export const SubjectGroupeCard = ({
    subjectGroupe,
}: {
    subjectGroupe: SubjectGroupe;
}) => (
    <div className="card bg-base-100 shadow-sm border border-base-300 max-w-100">
        <div className="card-body">
            <h2 className="card-title text-xl"> {subjectGroupe.name}</h2>
            <div className="flex gap-2 items-center text-sm">
                <span className="text-gray-500">subject ctn:</span> {subjectGroupe.subjects?.length || 0}
                <span className="text-gray-500"> teacher ctn:</span> {subjectGroupe.teachers?.length || 0}
            </div>
        </div>
    </div>
);
