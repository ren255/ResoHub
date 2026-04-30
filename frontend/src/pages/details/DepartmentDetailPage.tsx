import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { departmentRetrieve } from "@/types/api/sdk.gen";
import type { Department } from "@/types/api/types.gen";

export default function DepartmentDetailPage() {
    const { id } = useParams<{ id: string }>();
    const [department, setDepartment] = useState<Department | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchDepartment = async () => {
            if (!id) return;
            try {
                setLoading(true);
                setError(null);
                const { data } = await departmentRetrieve({ path: { id: Number(id) } });
                if (data) {
                    setDepartment(data);
                }
            } catch (err) {
                setError("学部情報の取得に失敗しました");
                console.error("Error fetching department:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchDepartment();
    }, [id]);

    if (loading) {
        return (
            <div className="flex justify-center items-center py-12">
                <span className="loading loading-spinner loading-lg"></span>
            </div>
        );
    }

    if (error || !department) {
        return (
            <div className="alert alert-error">
                <span>{error || "学部が見つかりません"}</span>
            </div>
        );
    }

    return (
        <div className="p-8 max-w-4xl mx-auto">


            <div className="card bg-base-100 shadow-lg border border-base-300">
                <div className="card-body">
                    <h1 className="card-title text-3xl mb-6">{department.name}</h1>

                    <div className="space-y-4">
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">ID</p>
                                <p className="font-mono">{department.id}</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">学校</p>
                                <Link
                                    to={`/schools/${department.school}`}
                                    className="link link-primary hover:underline"
                                >
                                    {department.school_name}
                                </Link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
