import { useEffect, useState } from "react";
import { subjectRetrieve } from "@/types/api/sdk.gen";
import type { Subject } from "@/types/api/types.gen";
import { DetailPage, DetailSection, LinkField, ExternalLinkField } from "@ui/DetailPage";

interface SubjectDetailProps {
    id: number;
}

export const SubjectDetail = ({ id }: SubjectDetailProps) => {
    const [subject, setSubject] = useState<Subject | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchSubject = async () => {
            try {
                setLoading(true);
                setError(null);
                const { data } = await subjectRetrieve({ path: { id } });
                if (data) {
                    setSubject(data);
                }
            } catch (err) {
                setError("教科情報の取得に失敗しました");
                console.error("Error fetching subject:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchSubject();
    }, [id]);

    if (!subject && !loading && !error) {
        return (
            <div className="alert alert-error">
                <span>教科が見つかりません</span>
            </div>
        );
    }

    const fields = [
        { label: "ID", value: <span className="font-mono">{subject?.id}</span> },
        { label: "コード", value: <span className="font-mono">{subject?.code}</span> },
        { label: "種別", value: subject?.subject_type },
        { label: "単位数", value: subject?.credits },
        {
            label: "学年クラス",
            value: subject?.grade_class ? (
                <LinkField to={`/grade-classes/${subject.grade_class}`}>
                    {subject.grade_class_str}
                </LinkField>
            ) : (
                "-"
            ),
        },
        ...(subject?.subject_groupe
            ? [
                {
                    label: "教科グループ",
                    value: (
                        <LinkField to={`/subject-groupes/${subject.subject_groupe}`}>
                            グループ詳細
                        </LinkField>
                    ),
                },
            ]
            : []),
    ];

    const additionalFields = [
        ...(subject?.teachers_str
            ? [{ label: "教師", value: subject.teachers_str }]
            : []),
        ...(subject?.textbooks
            ? [{ label: "教科書", value: subject.textbooks }]
            : []),
        ...(subject?.url
            ? [
                {
                    label: "URL",
                    value: <ExternalLinkField href={subject.url}>{subject.url}</ExternalLinkField>,
                },
            ]
            : []),
    ];

    return (
        <DetailPage title={subject?.name || "教科詳細"} loading={loading} error={error}>
            <DetailSection fields={fields} />
            {additionalFields.length > 0 && <DetailSection fields={additionalFields} columns={1} />}
        </DetailPage>
    );
};
