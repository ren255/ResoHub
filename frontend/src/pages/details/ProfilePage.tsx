import { useParams } from "react-router-dom";
import { UserDetail } from "@features/user/UserDetail";
import { TeacherInfoDetail } from "@features/user/TeacherInfoDetail";
import { StudentInfoDetail } from "@features/user/StudentInfoDetail";

export default function ProfilePage() {
    const { uuid } = useParams<{ uuid: string }>();

    if (!uuid) {
        return (
            <div className="alert alert-error">
                <span>ユーザーIDが指定されていません</span>
            </div>
        );
    }

    return (
        <>
            <UserDetail uuid={uuid} />
            <div className="px-8 max-w-4xl mx-auto">
                <TeacherInfoDetail userUuid={uuid} />
                <StudentInfoDetail userUuid={uuid} />
            </div>
        </>
    );
}
