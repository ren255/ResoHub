import { useEffect, useState } from "react";
import { syllabusDepartmentRetrieve } from "@/types/api/sdk.gen";
import type { SyllabusDepartment } from "@/types/api/types.gen";
import { DetailPage, DetailSection, LinkField, ExternalLinkField } from "@ui/DetailPage";

interface SyllabusDepartmentDetailProps {
    id: number;
}

export const SyllabusDepartmentDetail = ({ id }: SyllabusDepartmentDetailProps) => {
    const [syllabusDepartment, setSyllabusDepartment] = useState<SyllabusDepartment | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchSyllabusDepartment = async () => {
            try {
                setLoading(true);
                setError(null);
                const { data } = await syllabusDepartmentRetrieve({ path: { id } });
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

    if (!syllabusDepartment && !loading && !error) {
        return (
            <div className="alert alert-error">
                <span>シラバス学部が見つかりません</span>
            </div>
        );
    }

    const fields = [
        { label: "ID", value: <span className="font-mono">{syllabusDepartment?.id}</span> },
        { label: "コード", value: <span className="font-mono">{syllabusDepartment?.code}</span> },
        { label: "入学年度", value: `${syllabusDepartment?.admission_year}年度` },
        {
            label: "学校",
            value: syllabusDepartment?.school ? (
                <LinkField to={`/schools/${syllabusDepartment.school}`}>
                    {syllabusDepartment.school_name}
                </LinkField>
            ) : (
                "-"
            ),
        },
        ...(syllabusDepartment?.department
            ? [
                {
                    label: "親学部",
                    value: (
                        <LinkField to={`/departments/${syllabusDepartment.department}`}>
                            {syllabusDepartment.department_name}
                        </LinkField>
                    ),
                },
            ]
            : []),
        ...(syllabusDepartment?.url
            ? [
                {
                    label: "URL",
                    value: <ExternalLinkField href={syllabusDepartment.url}>{syllabusDepartment.url}</ExternalLinkField>,
                },
            ]
            : []),
    ];

    return (
        <DetailPage
            title={syllabusDepartment?.name || "シラバス学部詳細"}
            loading={loading}
            error={error}
        >
            <DetailSection fields={fields} />
        </DetailPage>
    );
};
