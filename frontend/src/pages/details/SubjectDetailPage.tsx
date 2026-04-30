import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { subjectRetrieve } from "@/types/api/sdk.gen";
import type { Subject } from "@/types/api/types.gen";

export default function SubjectDetailPage() {
    const { id } = useParams<{ id: string }>();
    const [subject, setSubject] = useState<Subject | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchSubject = async () => {
            if (!id) return;
            try {
                setLoading(true);
                setError(null);
                const { data } = await subjectRetrieve({ path: { id: Number(id) } });
                if (data) {
                    setSubject(data);
                }
            } catch (err) {
                setError("教科情報の取得に失敗しました");
                console.error("Error fetching subject:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchSubject();
    }, [id]);

    if (loading) {
        return (
            <div className="flex justify-center items-center py-12">
                <span className="loading loading-spinner loading-lg"></span>
            </div>
        );
    }

    if (error || !subject) {
        return (
            <div className="alert alert-error">
                <span>{error || "教科が見つかりません"}</span>
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
                    <h1 className="card-title text-3xl mb-6">{subject.name}</h1>

                    <div className="space-y-4">
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">ID</p>
                                <p className="font-mono">{subject.id}</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">コード</p>
                                <p className="font-mono">{subject.code}</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">種別</p>
                                <p>{subject.subject_type}</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">単位数</p>
                                <p>{subject.credits}</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">学年クラス</p>
                                <Link
                                    to={`/grade-classes/${subject.grade_class}`}
                                    className="link link-primary hover:underline"
                                >
                                    {subject.grade_class_str}
                                </Link>
                            </div>
                            {subject.subject_groupe && (
                                <div className="bg-base-200 p-4 rounded-lg">
                                    <p className="text-sm text-gray-500 mb-1">教科グループ</p>
                                    <Link
                                        to={`/subject-groupes/${subject.subject_groupe}`}
                                        className="link link-primary hover:underline"
                                    >
                                        グループ詳細
                                    </Link>
                                </div>
                            )}
                        </div>
                        {subject.teachers_str && (
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">教師</p>
                                <p>{subject.teachers_str}</p>
                            </div>
                        )}
                        {subject.textbooks && (
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">教科書</p>
                                <p>{subject.textbooks}</p>
                            </div>
                        )}
                        {subject.url && (
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">URL</p>
                                <a
                                    href={subject.url}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="link link-primary hover:underline"
                                >
                                    {subject.url}
                                </a>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
}
