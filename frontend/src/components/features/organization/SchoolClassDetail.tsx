import { useEffect, useState } from "react";
import { schoolClassRetrieve } from "@/types/api/sdk.gen";
import type { SchoolClass } from "@/types/api/types.gen";
import { DetailPage, DetailSection, LinkField } from "@ui/DetailPage";

interface SchoolClassDetailProps {
    id: number;
}

export const SchoolClassDetail = ({ id }: SchoolClassDetailProps) => {
    const [schoolClass, setSchoolClass] = useState<SchoolClass | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchSchoolClass = async () => {
            try {
                setLoading(true);
                setError(null);
                const { data } = await schoolClassRetrieve({ path: { id } });
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

    if (!schoolClass && !loading && !error) {
        return (
            <div className="alert alert-error">
                <span>クラスが見つかりません</span>
            </div>
        );
    }

    const fields = [
        { label: "ID", value: <span className="font-mono">{schoolClass?.id}</span> },
        { label: "入学年度", value: `${schoolClass?.admission_year}年度` },
        {
            label: "学部",
            value: schoolClass?.department ? (
                <LinkField to={`/departments/${schoolClass.department}`}>
                    {schoolClass.department_name}
                </LinkField>
            ) : (
                "-"
            ),
        },
        {
            label: "シラバス学部",
            value: schoolClass?.syllabus_department ? (
                <LinkField to={`/syllabus-departments/${schoolClass.syllabus_department}`}>
                    {schoolClass.syllabus_department_name}
                </LinkField>
            ) : (
                "-"
            ),
        },
    ];

    return (
        <DetailPage
            title={schoolClass?.syllabus_department_name || "クラス詳細"}
            loading={loading}
            error={error}
        >
            <DetailSection fields={fields} />
        </DetailPage>
    );
};
