import type { Exam } from "@/types/api/types.gen";
import { Link } from "react-router-dom";

export const ExamCard = ({ exam }: { exam: Exam }) => (
    <div className="card bg-base-100 shadow-sm border border-base-300 max-w-100">
        <div className="card-body">
            <h2 className="card-title text-xl">
                <Link
                    to={`/subjects/${exam.subject}`}
                    className="link link-primary hover:underline"
                >
                    {exam.subject_name}
                </Link>
                Q{exam.quarter}第{exam.week}週
            </h2>
            <div className="space-y-1 text-sm">
                <a
                    href={exam.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="link link-primary hover:underline"
                >
                    シラバス
                </a>
                <p>
                    <span className="text-gray-500">内容:</span> {exam.content}
                </p>
                <p>
                    <span className="text-gray-500">目標:</span> {exam.goal}
                </p>
            </div>
        </div>
    </div>
);
