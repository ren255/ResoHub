import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { syllabusDepartmentRetrieve } from "@/types/api/sdk.gen";
import type { SyllabusDepartment } from "@/types/api/types.gen";

export default function SyllabusDepartmentDetailPage() {
    const { id } = useParams<{ id: string }>();
    const [syllabusDepartment, setSyllabusDepartment] = useState<SyllabusDepartment | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchSyllabusDepartment = async () => {
            if (!id) return;
            try {
                setLoading(true);
                setError(null);
                const { data } = await syllabusDepartmentRetrieve({ path: { id: Number(id) } });
                if (data) {
                    setSyllabusDepartment(data);
                }
            } catch (err) {
                setError("シラバス学部情報の取得に失敗しました");
                console.error("Error fetching syllabus department:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchSyllabusDepartment();
    }, [id]);

    if (loading) {
        return (
            <div className="flex justify-center items-center py-12">
                <span className="loading loading-spinner loading-lg"></span>
            </div>
        );
    }

    if (error || !syllabusDepartment) {
        return (
            <div className="alert alert-error">
                <span>{error || "シラバス学部が見つかりません"}</span>
            </div>
        );
    }

    return (
        <div className="p-8 max-w-4xl mx-auto">


            <div className="card bg-base-100 shadow-lg border border-base-300">
                <div className="card-body">
                    <h1 className="card-title text-3xl mb-6">{syllabusDepartment.name}</h1>

                    <div className="space-y-4">
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">ID</p>
                                <p className="font-mono">{syllabusDepartment.id}</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">コード</p>
                                <p className="font-mono">{syllabusDepartment.code}</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">入学年度</p>
                                <p>{syllabusDepartment.admission_year}年度</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">学校</p>
                                <Link
                                    to={`/schools/${syllabusDepartment.school}`}
                                    className="link link-primary hover:underline"
                                >
                                    {syllabusDepartment.school_name}
                                </Link>
                            </div>
                        </div>
                        {syllabusDepartment.department && (
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">親学部</p>
                                <Link
                                    to={`/departments/${syllabusDepartment.department}`}
                                    className="link link-primary hover:underline"
                                >
                                    {syllabusDepartment.department_name}
                                </Link>
                            </div>
                        )}
                        {syllabusDepartment.url && (
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">URL</p>
                                <a
                                    href={syllabusDepartment.url}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="link link-primary hover:underline"
                                >
                                    {syllabusDepartment.url}
                                </a>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
}
