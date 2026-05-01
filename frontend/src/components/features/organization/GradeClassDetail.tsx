import { useEffect, useState } from "react";
import { gradeClassRetrieve } from "@/types/api/sdk.gen";
import type { GradeClass } from "@/types/api/types.gen";
import { DetailPage, DetailSection, LinkField } from "@ui/DetailPage";

interface GradeClassDetailProps {
    id: number;
}

export const GradeClassDetail = ({ id }: GradeClassDetailProps) => {
    const [gradeClass, setGradeClass] = useState<GradeClass | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchGradeClass = async () => {
            try {
                setLoading(true);
                setError(null);
                const { data } = await gradeClassRetrieve({ path: { id } });
                if (data) {
                    setGradeClass(data);
                }
            } catch (err) {
                setError("学年クラス情報の取得に失敗しました");
                console.error("Error fetching grade class:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchGradeClass();
    }, [id]);

    if (!gradeClass && !loading && !error) {
        return (
            <div className="alert alert-error">
                <span>学年クラスが見つかりません</span>
            </div>
        );
    }

    const fields = [
        { label: "ID", value: <span className="font-mono">{gradeClass?.id}</span> },
        { label: "学年", value: `${gradeClass?.grade}年` },
        { label: "年度", value: `${gradeClass?.year}年度` },
        {
            label: "クラス",
            value: gradeClass?.school_class ? (
                <LinkField to={`/school-classes/${gradeClass.school_class}`}>
                    {gradeClass.school_class_str}
                </LinkField>
            ) : (
                "-"
            ),
        },
    ];

    return (
        <DetailPage
            title={gradeClass?.grade_str || `${gradeClass?.year}年度`}
            loading={loading}
            error={error}
        >
            <DetailSection fields={fields} />
        </DetailPage>
    );
};
