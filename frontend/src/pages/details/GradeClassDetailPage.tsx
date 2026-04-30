import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { gradeClassRetrieve } from "@/types/api/sdk.gen";
import type { GradeClass } from "@/types/api/types.gen";

export default function GradeClassDetailPage() {
    const { id } = useParams<{ id: string }>();
    const [gradeClass, setGradeClass] = useState<GradeClass | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchGradeClass = async () => {
            if (!id) return;
            try {
                setLoading(true);
                setError(null);
                const { data } = await gradeClassRetrieve({ path: { id: Number(id) } });
                if (data) {
                    setGradeClass(data);
                }
            } catch (err) {
                setError("学年クラス情報の取得に失敗しました");
                console.error("Error fetching grade class:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchGradeClass();
    }, [id]);

    if (loading) {
        return (
            <div className="flex justify-center items-center py-12">
                <span className="loading loading-spinner loading-lg"></span>
            </div>
        );
    }

    if (error || !gradeClass) {
        return (
            <div className="alert alert-error">
                <span>{error || "学年クラスが見つかりません"}</span>
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
                    <h1 className="card-title text-3xl mb-6">
                        {gradeClass.grade_str || `${gradeClass.year}年度`}
                    </h1>

                    <div className="space-y-4">
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">ID</p>
                                <p className="font-mono">{gradeClass.id}</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">学年</p>
                                <p>{gradeClass.grade}年</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">年度</p>
                                <p>{gradeClass.year}年度</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">クラス</p>
                                <Link
                                    to={`/school-classes/${gradeClass.school_class}`}
                                    className="link link-primary hover:underline"
                                >
                                    {gradeClass.school_class_str}
                                </Link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
