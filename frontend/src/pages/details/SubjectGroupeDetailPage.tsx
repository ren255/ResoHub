import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { subjectGroupeRetrieve } from "@/types/api/sdk.gen";
import type { SubjectGroupe } from "@/types/api/types.gen";

export default function SubjectGroupeDetailPage() {
    const { id } = useParams<{ id: string }>();
    const [subjectGroupe, setSubjectGroupe] = useState<SubjectGroupe | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchSubjectGroupe = async () => {
            if (!id) return;
            try {
                setLoading(true);
                setError(null);
                const { data } = await subjectGroupeRetrieve({ path: { id: Number(id) } });
                if (data) {
                    setSubjectGroupe(data);
                }
            } catch (err) {
                setError("教科グループ情報の取得に失敗しました");
                console.error("Error fetching subject groupe:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchSubjectGroupe();
    }, [id]);

    if (loading) {
        return (
            <div className="flex justify-center items-center py-12">
                <span className="loading loading-spinner loading-lg"></span>
            </div>
        );
    }

    if (error || !subjectGroupe) {
        return (
            <div className="alert alert-error">
                <span>{error || "教科グループが見つかりません"}</span>
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
                    <h1 className="card-title text-3xl mb-6">{subjectGroupe.name}</h1>

                    <div className="space-y-4">
                        <div className="bg-base-200 p-4 rounded-lg">
                            <p className="text-sm text-gray-500 mb-1">ID</p>
                            <p className="font-mono">{subjectGroupe.id}</p>
                        </div>

                        {subjectGroupe.teachers.length > 0 && (
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-2">担当教師</p>
                                <div className="flex flex-wrap gap-2">
                                    {subjectGroupe.teachers.map((teacherId) => (
                                        <Link
                                            key={teacherId}
                                            to={`/teacher-info/${teacherId}`}
                                            className="badge badge-primary badge-lg hover:badge-secondary"
                                        >
                                            教師 #{teacherId}
                                        </Link>
                                    ))}
                                </div>
                            </div>
                        )}

                        {subjectGroupe.subjects.length > 0 && (
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-2">所属教科</p>
                                <div className="flex flex-wrap gap-2">
                                    {subjectGroupe.subjects.map((subjectId) => (
                                        <Link
                                            key={subjectId}
                                            to={`/subjects/${subjectId}`}
                                            className="badge badge-secondary badge-lg hover:badge-primary"
                                        >
                                            教科 #{subjectId}
                                        </Link>
                                    ))}
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
}
