import type { School } from "@/types/api/types.gen";

export const SchoolCard = ({ school }: { school: School }) => (
    <div className="card bg-base-100 shadow-sm border border-base-300 max-w-100">
        <div className="card-body">
            <h2 className="card-title text-xl">{school.name}</h2>
            <div className="space-y-1 text-sm">
                <a
                    href={school.url}
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
