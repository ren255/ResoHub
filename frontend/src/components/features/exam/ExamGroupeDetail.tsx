import { useEffect, useState } from "react";
import { examGroupeRetrieve } from "@/types/api/sdk.gen";
import type { ExamGroupe } from "@/types/api/types.gen";
import { DetailPage, DetailSection, LinkField } from "@ui/DetailPage";

interface ExamGroupeDetailProps {
    id: number;
}

export const ExamGroupeDetail = ({ id }: ExamGroupeDetailProps) => {
    const [examGroupe, setExamGroupe] = useState<ExamGroupe | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchExamGroupe = async () => {
            try {
                setLoading(true);
                setError(null);
                const { data } = await examGroupeRetrieve({ path: { id } });
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

    if (!examGroupe && !loading && !error) {
        return (
            <div className="alert alert-error">
                <span>試験グループが見つかりません</span>
            </div>
        );
    }

    const fields = [
        { label: "ID", value: <span className="font-mono">{examGroupe?.id}</span> },
        {
            label: "教科",
            value: examGroupe?.subject ? (
                <LinkField to={`/subjects/${examGroupe.subject}`}>
                    {examGroupe.subject_name}
                </LinkField>
            ) : (
                "-"
            ),
        },
        {
            label: "教科グループ",
            value: examGroupe?.subject_groupe ? (
                <LinkField to={`/subject-groupes/${examGroupe.subject_groupe}`}>
                    グループ詳細
                </LinkField>
            ) : (
                "-"
            ),
        },
    ];

    return (
        <DetailPage
            title={`試験グループ #${examGroupe?.id || ""}`}
            loading={loading}
            error={error}
        >
            <DetailSection fields={fields} />
        </DetailPage>
    );
};
