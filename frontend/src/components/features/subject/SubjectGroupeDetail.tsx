import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { subjectGroupeRetrieve } from "@/types/api/sdk.gen";
import type { SubjectGroupe } from "@/types/api/types.gen";
import { DetailPage, DetailSection } from "@ui/DetailPage";

interface SubjectGroupeDetailProps {
    id: number;
}

export const SubjectGroupeDetail = ({ id }: SubjectGroupeDetailProps) => {
    const [subjectGroupe, setSubjectGroupe] = useState<SubjectGroupe | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchSubjectGroupe = async () => {
            try {
                setLoading(true);
                setError(null);
                const { data } = await subjectGroupeRetrieve({ path: { id } });
                if (data) {
                    setSubjectGroupe(data);
                }
            } catch (err) {
                setError("教科グループ情報の取得に失敗しました");
                console.error("Error fetching subject groupe:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchSubjectGroupe();
    }, [id]);

    if (!subjectGroupe && !loading && !error) {
        return (
            <div className="alert alert-error">
                <span>教科グループが見つかりません</span>
            </div>
        );
    }

    const fields = [
        { label: "ID", value: <span className="font-mono">{subjectGroupe?.id}</span> },
    ];

    return (
        <DetailPage
            title={subjectGroupe?.name || "教科グループ詳細"}
            loading={loading}
            error={error}
        >
            <DetailSection fields={fields} />

            {subjectGroupe && subjectGroupe.teachers.length > 0 && (
                <div className="mb-8">
                    <h3 className="text-lg font-semibold mb-3">担当教師</h3>
                    <div className="flex flex-wrap gap-2">
                        {subjectGroupe.teachers.map((teacherId) => (
                            <Link
                                key={teacherId}
                                to={`/teacher-info/${teacherId}`}
                                className="badge badge-primary badge-lg hover:badge-secondary"
                            >
                                教師 #{teacherId}
                            </Link>
                        ))}
                    </div>
                </div>
            )}

            {subjectGroupe && subjectGroupe.subjects.length > 0 && (
                <div className="mb-8">
                    <h3 className="text-lg font-semibold mb-3">所属教科</h3>
                    <div className="flex flex-wrap gap-2">
                        {subjectGroupe.subjects.map((subjectId) => (
                            <Link
                                key={subjectId}
                                to={`/subjects/${subjectId}`}
                                className="badge badge-secondary badge-lg hover:badge-primary"
                            >
                                教科 #{subjectId}
                            </Link>
                        ))}
                    </div>
                </div>
            )}
        </DetailPage>
    );
};
