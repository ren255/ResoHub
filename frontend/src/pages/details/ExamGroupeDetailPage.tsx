import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { examGroupeRetrieve } from "@/types/api/sdk.gen";
import type { ExamGroupe } from "@/types/api/types.gen";

export default function ExamGroupeDetailPage() {
    const { id } = useParams<{ id: string }>();
    const [examGroupe, setExamGroupe] = useState<ExamGroupe | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchExamGroupe = async () => {
            if (!id) return;
            try {
                setLoading(true);
                setError(null);
                const { data } = await examGroupeRetrieve({ path: { id: Number(id) } });
                if (data) {
                    setExamGroupe(data);
                }
            } catch (err) {
                setError("試験グループ情報の取得に失敗しました");
                console.error("Error fetching exam groupe:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchExamGroupe();
    }, [id]);

    if (loading) {
        return (
            <div className="flex justify-center items-center py-12">
                <span className="loading loading-spinner loading-lg"></span>
            </div>
        );
    }

    if (error || !examGroupe) {
        return (
            <div className="alert alert-error">
                <span>{error || "試験グループが見つかりません"}</span>
            </div>
        );
    }

    return (
        <div className="p-8 max-w-4xl mx-auto">


            <div className="card bg-base-100 shadow-lg border border-base-300">
                <div className="card-body">
                    <h1 className="card-title text-3xl mb-6">試験グループ #{examGroupe.id}</h1>

                    <div className="space-y-4">
                        <div className="bg-base-200 p-4 rounded-lg">
                            <p className="text-sm text-gray-500 mb-1">ID</p>
                            <p className="font-mono">{examGroupe.id}</p>
                        </div>

                        <div className="bg-base-200 p-4 rounded-lg">
                            <p className="text-sm text-gray-500 mb-1">教科</p>
                            <Link
                                to={`/subjects/${examGroupe.subject}`}
                                className="link link-primary hover:underline"
                            >
                                {examGroupe.subject_name}
                            </Link>
                        </div>

                        <div className="bg-base-200 p-4 rounded-lg">
                            <p className="text-sm text-gray-500 mb-1">教科グループ</p>
                            <Link
                                to={`/subject-groupes/${examGroupe.subject_groupe}`}
                                className="link link-primary hover:underline"
                            >
                                グループ詳細
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
