import { useEffect, useState } from "react";
import { studentInfoList } from "@/types/api/sdk.gen";
import type { StudentInfo } from "@/types/api/types.gen";
import { DetailSection, LinkField } from "@ui/DetailPage";

interface StudentInfoDetailProps {
    userUuid: string;
}

export const StudentInfoDetail = ({ userUuid }: StudentInfoDetailProps) => {
    const [studentInfo, setStudentInfo] = useState<StudentInfo | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchStudentInfo = async () => {
            try {
                setLoading(true);
                const { data: students } = await studentInfoList();
                const student = students?.find((s) => s.user === userUuid);
                if (student) {
                    setStudentInfo(student);
                }
            } catch (err) {
                console.error("Error fetching student info:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchStudentInfo();
    }, [userUuid]);

    if (loading || !studentInfo) {
        return null;
    }

    const fields = [
        {
            label: "学籍番号",
            value: <span className="font-mono">{studentInfo.student_id}</span>,
        },
        ...(studentInfo.school_class
            ? [
                {
                    label: "クラス",
                    value: (
                        <LinkField to={`/school-classes/${studentInfo.school_class}`}>
                            {studentInfo.school_class_str}
                        </LinkField>
                    ),
                },
            ]
            : []),
    ];

    return <DetailSection title="生徒情報" fields={fields} />;
};
