import type { School } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const SchoolCard = ({ school }: { school: School }) => (
    <div className="card bg-base-100 shadow-sm border border-base-300">
        <div className="card-body">
            <h2 className="card-title text-xl">{school.name}</h2>
            <div className="space-y-1 text-sm">
                <p>
                    <span className="text-gray-500">学校コード:</span> {school.code}
                </p>
                {school.url && (
                    <p>
                        <span className="text-gray-500">URL:</span>{" "}
                        <a
                            href={school.url}
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
