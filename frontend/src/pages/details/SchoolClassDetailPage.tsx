import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { schoolClassRetrieve } from "@/types/api/sdk.gen";
import type { SchoolClass } from "@/types/api/types.gen";

export default function SchoolClassDetailPage() {
    const { id } = useParams<{ id: string }>();
    const [schoolClass, setSchoolClass] = useState<SchoolClass | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchSchoolClass = async () => {
            if (!id) return;
            try {
                setLoading(true);
                setError(null);
                const { data } = await schoolClassRetrieve({ path: { id: Number(id) } });
                if (data) {
                    setSchoolClass(data);
                }
            } catch (err) {
                setError("クラス情報の取得に失敗しました");
                console.error("Error fetching school class:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchSchoolClass();
    }, [id]);

    if (loading) {
        return (
            <div className="flex justify-center items-center py-12">
                <span className="loading loading-spinner loading-lg"></span>
            </div>
        );
    }

    if (error || !schoolClass) {
        return (
            <div className="alert alert-error">
                <span>{error || "クラスが見つかりません"}</span>
            </div>
        );
    }

    return (
        <div className="p-8 max-w-4xl mx-auto">


            <div className="card bg-base-100 shadow-lg border border-base-300">
                <div className="card-body">
                    <h1 className="card-title text-3xl mb-6">{schoolClass.syllabus_department_name}</h1>

                    <div className="space-y-4">
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">ID</p>
                                <p className="font-mono">{schoolClass.id}</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">入学年度</p>
                                <p>{schoolClass.admission_year}年度</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">学部</p>
                                <Link
                                    to={`/departments/${schoolClass.department}`}
                                    className="link link-primary hover:underline"
                                >
                                    {schoolClass.department_name}
                                </Link>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">シラバス学部</p>
                                <Link
                                    to={`/syllabus-departments/${schoolClass.syllabus_department}`}
                                    className="link link-primary hover:underline"
                                >
                                    {schoolClass.syllabus_department_name}
                                </Link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
