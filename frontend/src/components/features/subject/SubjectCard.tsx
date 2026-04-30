import type { Subject } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const SubjectCard = ({ subject }: { subject: Subject }) => (
    <div className="card bg-base-100 shadow-sm border border-base-300 max-w-100">
        <div className="card-body">
            <h2 className="card-title text-xl">{subject.name}</h2>
            <div className="space-y-1 text-sm">
                <div className="flex gap-2 items-center">
                    <span>
                        {subject.subject_type}
                    </span>
                    <span>
                        {subject.credits}<span className="text-gray-500">単位</span>
                    </span>
                    <span>
                        <a
                            href={subject.url}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="link link-primary hover:underline"
                        >シラバス
                        </a>
                    </span>
                </div>
                <p>
                    <Link
                        to={`/grade-classes/${subject.grade_class}`}
                        className="link link-primary hover:underline"
                    >
                        {subject.grade_class_str}
                    </Link>
                </p>
                <p>
                    <span className="text-gray-500">担当教員:</span> {subject.teachers_str}
                </p>
                <p>
                    <span className="text-gray-500">教科書:</span> {subject.textbooks.slice(0, 30)}
                </p>
            </div>
        </div>
    </div>
);
