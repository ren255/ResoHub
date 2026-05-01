import { useEffect, useState } from "react";
import { departmentRetrieve } from "@/types/api/sdk.gen";
import type { Department } from "@/types/api/types.gen";
import { DetailPage, DetailSection, LinkField } from "@ui/DetailPage";

interface DepartmentDetailProps {
    id: number;
}

export const DepartmentDetail = ({ id }: DepartmentDetailProps) => {
    const [department, setDepartment] = useState<Department | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchDepartment = async () => {
            try {
                setLoading(true);
                setError(null);
                const { data } = await departmentRetrieve({ path: { id } });
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

    if (!department && !loading && !error) {
        return (
            <div className="alert alert-error">
                <span>学部が見つかりません</span>
            </div>
        );
    }

    const fields = [
        { label: "ID", value: <span className="font-mono">{department?.id}</span> },
        {
            label: "学校",
            value: department?.school ? (
                <LinkField to={`/schools/${department.school}`}>{department.school_name}</LinkField>
            ) : (
                "-"
            ),
        },
    ];

    return (
        <DetailPage
            title={department?.name || "学部詳細"}
            loading={loading}
            error={error}
        >
            <DetailSection fields={fields} />
        </DetailPage>
    );
};
