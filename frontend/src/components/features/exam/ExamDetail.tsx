import { useEffect, useState } from "react";
import { examRetrieve } from "@/types/api/sdk.gen";
import type { Exam } from "@/types/api/types.gen";
import { DetailPage, DetailSection, LinkField, ExternalLinkField } from "@ui/DetailPage";

interface ExamDetailProps {
    id: number;
}

export const ExamDetail = ({ id }: ExamDetailProps) => {
    const [exam, setExam] = useState<Exam | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchExam = async () => {
            try {
                setLoading(true);
                setError(null);
                const { data } = await examRetrieve({ path: { id } });
                if (data) {
                    setExam(data);
                }
            } catch (err) {
                setError("試験情報の取得に失敗しました");
                console.error("Error fetching exam:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchExam();
    }, [id]);

    if (!exam && !loading && !error) {
        return (
            <div className="alert alert-error">
                <span>試験が見つかりません</span>
            </div>
        );
    }

    const fields = [
        { label: "ID", value: <span className="font-mono">{exam?.id}</span> },
        { label: "四半期", value: `第${exam?.quarter}Q` },
        { label: "週", value: `第${exam?.week}週` },
        {
            label: "教科",
            value: exam?.subject ? (
                <LinkField to={`/subjects/${exam.subject}`}>{exam.subject_name}</LinkField>
            ) : (
                "-"
            ),
        },
        ...(exam?.exam_groupe
            ? [
                {
                    label: "試験グループ",
                    value: (
                        <LinkField to={`/exam-groupes/${exam.exam_groupe}`}>グループ詳細</LinkField>
                    ),
                },
            ]
            : []),
    ];

    const additionalFields = [
        ...(exam?.content ? [{ label: "内容", value: exam.content }] : []),
        ...(exam?.goal ? [{ label: "目標", value: exam.goal }] : []),
        ...(exam?.file
            ? [
                {
                    label: "ファイル",
                    value: (
                        <a
                            href={`/api/files/${exam.file}/download`}
                            className="btn btn-primary btn-sm"
                        >
                            ダウンロード
                        </a>
                    ),
                },
            ]
            : []),
        ...(exam?.url
            ? [
                {
                    label: "URL",
                    value: <ExternalLinkField href={exam.url}>{exam.url}</ExternalLinkField>,
                },
            ]
            : []),
    ];

    return (
        <DetailPage
            title={exam ? `${exam.subject_name} - 第${exam.quarter}Q` : "試験詳細"}
            loading={loading}
            error={error}
        >
            <DetailSection fields={fields} />
            {additionalFields.length > 0 && <DetailSection fields={additionalFields} columns={1} />}
        </DetailPage>
    );
};
