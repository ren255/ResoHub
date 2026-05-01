import { useEffect, useState } from "react";
import { schoolRetrieve } from "@/types/api/sdk.gen";
import type { School } from "@/types/api/types.gen";
import { DetailPage, DetailSection, ExternalLinkField } from "@ui/DetailPage";

interface SchoolDetailProps {
    id: number;
}

export const SchoolDetail = ({ id }: SchoolDetailProps) => {
    const [school, setSchool] = useState<School | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchSchool = async () => {
            try {
                setLoading(true);
                setError(null);
                const { data } = await schoolRetrieve({ path: { id } });
                if (data) {
                    setSchool(data);
                }
            } catch (err) {
                setError("学校情報の取得に失敗しました");
                console.error("Error fetching school:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchSchool();
    }, [id]);

    if (!school && !loading && !error) {
        return (
            <div className="alert alert-error">
                <span>学校が見つかりません</span>
            </div>
        );
    }

    const fields = [
        { label: "ID", value: <span className="font-mono">{school?.id}</span> },
        { label: "学校コード", value: <span className="font-mono">{school?.code}</span> },
        ...(school?.url
            ? [
                {
                    label: "URL",
                    value: <ExternalLinkField href={school.url}>{school.url}</ExternalLinkField>,
                },
            ]
            : []),
    ];

    return (
        <DetailPage title={school?.name || "学校詳細"} loading={loading} error={error}>
            <DetailSection fields={fields} />
        </DetailPage>
    );
};
