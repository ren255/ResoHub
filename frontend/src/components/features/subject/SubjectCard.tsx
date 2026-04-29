import type { Subject } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const SubjectCard = ({ subject }: { subject: Subject }) => (
    <div className="card bg-base-100 shadow-sm border border-base-300">
        <div className="card-body">
            <h2 className="card-title text-xl">{subject.name}</h2>
            <div className="space-y-1 text-sm">
                <p>
                    <span className="text-gray-500">コード:</span> {subject.code}
                </p>
                <p>
                    <span className="text-gray-500">種別:</span> {subject.subject_type}
                </p>
                <p>
                    <span className="text-gray-500">単位:</span> {subject.credits}
                </p>
                <p>
                    <span className="text-gray-500">学年クラス:</span>{" "}
                    <Link
                        to={`/grade-classes/${subject.grade_class}`}
                        className="link link-primary hover:underline"
                    >
                        {subject.grade_class_str}
                    </Link>
                </p>
                {subject.subject_groupe && (
                    <p>
                        <span className="text-gray-500">教科グループ:</span>{" "}
                        <Link
                            to={`/subject-groupes/${subject.subject_groupe}`}
                            className="link link-primary hover:underline"
                        >
                            グループ {subject.subject_groupe}
                        </Link>
                    </p>
                )}
                {subject.teachers_str && (
                    <p>
                        <span className="text-gray-500">担当教員:</span> {subject.teachers_str}
                    </p>
                )}
                {subject.textbooks && (
                    <p>
                        <span className="text-gray-500">教科書:</span> {subject.textbooks}
                    </p>
                )}
                {subject.url && (
                    <p>
                        <span className="text-gray-500">URL:</span>{" "}
                        <a
                            href={subject.url}
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
