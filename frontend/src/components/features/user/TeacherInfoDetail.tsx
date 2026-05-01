import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { teacherInfoList } from "@/types/api/sdk.gen";
import type { TeacherInfo } from "@/types/api/types.gen";
import { DetailSection, LinkField } from "@ui/DetailPage";

interface TeacherInfoDetailProps {
    userUuid: string;
}

export const TeacherInfoDetail = ({ userUuid }: TeacherInfoDetailProps) => {
    const [teacherInfo, setTeacherInfo] = useState<TeacherInfo | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchTeacherInfo = async () => {
            try {
                setLoading(true);
                const { data: teachers } = await teacherInfoList();
                const teacher = teachers?.find((t) => t.user === userUuid);
                if (teacher) {
                    setTeacherInfo(teacher);
                }
            } catch (err) {
                console.error("Error fetching teacher info:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchTeacherInfo();
    }, [userUuid]);

    if (loading || !teacherInfo) {
        return null;
    }

    const fields = [
        {
            label: "所属学部",
            value: teacherInfo.department ? (
                <LinkField to={`/departments/${teacherInfo.department}`}>
                    {teacherInfo.department_name}
                </LinkField>
            ) : (
                "-"
            ),
        },
        ...(teacherInfo.department_type
            ? [{ label: "学部タイプ", value: teacherInfo.department_type }]
            : []),
        ...(teacherInfo.subdomain
            ? [
                {
                    label: "サブドメイン",
                    value: <span className="font-mono">{teacherInfo.subdomain}</span>,
                },
            ]
            : []),
    ];

    return (
        <>
            <DetailSection title="教師情報" fields={fields} />

            {teacherInfo.owner && (
                <div className="mb-8">
                    <span className="badge badge-accent">オーナー</span>
                </div>
            )}

            {teacherInfo.subjects.length > 0 && (
                <div className="mb-8">
                    <h3 className="text-lg font-semibold mb-3">担当教科</h3>
                    <div className="flex flex-wrap gap-2">
                        {teacherInfo.subjects.map((subjectId) => (
                            <Link
                                key={subjectId}
                                to={`/subjects/${subjectId}`}
                                className="badge badge-primary badge-lg hover:badge-secondary"
                            >
                                教科 #{subjectId}
                            </Link>
                        ))}
                    </div>
                </div>
            )}
        </>
    );
};
