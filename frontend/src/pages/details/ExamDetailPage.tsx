import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { examRetrieve } from "@/types/api/sdk.gen";
import type { Exam } from "@/types/api/types.gen";

export default function ExamDetailPage() {
    const { id } = useParams<{ id: string }>();
    const [exam, setExam] = useState<Exam | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchExam = async () => {
            if (!id) return;
            try {
                setLoading(true);
                setError(null);
                const { data } = await examRetrieve({ path: { id: Number(id) } });
                if (data) {
                    setExam(data);
                }
            } catch (err) {
                setError("試験情報の取得に失敗しました");
                console.error("Error fetching exam:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchExam();
    }, [id]);

    if (loading) {
        return (
            <div className="flex justify-center items-center py-12">
                <span className="loading loading-spinner loading-lg"></span>
            </div>
        );
    }

    if (error || !exam) {
        return (
            <div className="alert alert-error">
                <span>{error || "試験が見つかりません"}</span>
            </div>
        );
    }

    return (
        <div className="p-8 max-w-4xl mx-auto">
            <div className="mb-6">
                <Link to="/obj-search" className="link link-primary text-sm">
                    ← オブジェクト検索に戻る
                </Link>
            </div>

            <div className="card bg-base-100 shadow-lg border border-base-300">
                <div className="card-body">
                    <h1 className="card-title text-3xl mb-6">{exam.subject_name} - 第{exam.quarter}Q</h1>

                    <div className="space-y-4">
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">ID</p>
                                <p className="font-mono">{exam.id}</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">四半期</p>
                                <p>第{exam.quarter}Q</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">週</p>
                                <p>第{exam.week}週</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">教科</p>
                                <Link
                                    to={`/subjects/${exam.subject}`}
                                    className="link link-primary hover:underline"
                                >
                                    {exam.subject_name}
                                </Link>
                            </div>
                        </div>

                        {exam.exam_groupe && (
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">試験グループ</p>
                                <Link
                                    to={`/exam-groupes/${exam.exam_groupe}`}
                                    className="link link-primary hover:underline"
                                >
                                    グループ詳細
                                </Link>
                            </div>
                        )}

                        {exam.content && (
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">内容</p>
                                <p className="whitespace-pre-wrap">{exam.content}</p>
                            </div>
                        )}

                        {exam.goal && (
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">目標</p>
                                <p className="whitespace-pre-wrap">{exam.goal}</p>
                            </div>
                        )}

                        {exam.file && (
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">ファイル</p>
                                <a
                                    href={`/api/files/${exam.file}/download`}
                                    className="btn btn-primary btn-sm"
                                >
                                    ダウンロード
                                </a>
                            </div>
                        )}

                        {exam.url && (
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">URL</p>
                                <a
                                    href={exam.url}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="link link-primary hover:underline"
                                >
                                    {exam.url}
                                </a>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
}
