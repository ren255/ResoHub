import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { userRetrieve, studentInfoList, teacherInfoList } from "@/types/api/sdk.gen";
import type { User, StudentInfo, TeacherInfo } from "@/types/api/types.gen";

export default function ProfilePage() {
    const { uuid } = useParams<{ uuid: string }>();
    const [user, setUser] = useState<User | null>(null);
    const [studentInfo, setStudentInfo] = useState<StudentInfo | null>(null);
    const [teacherInfo, setTeacherInfo] = useState<TeacherInfo | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchUserData = async () => {
            if (!uuid) return;
            try {
                setLoading(true);
                setError(null);

                // Fetch user data
                const { data: userData } = await userRetrieve({ path: { uuid } });
                if (userData) {
                    setUser(userData);

                    // Fetch student info if user is a student
                    if (userData.role === "student") {
                        const { data: students } = await studentInfoList();
                        const student = students?.find((s) => s.user === uuid);
                        if (student) {
                            setStudentInfo(student);
                        }
                    }

                    // Fetch teacher info if user is a teacher
                    if (userData.role === "teacher") {
                        const { data: teachers } = await teacherInfoList();
                        const teacher = teachers?.find((t) => t.user === uuid);
                        if (teacher) {
                            setTeacherInfo(teacher);
                        }
                    }
                }
            } catch (err) {
                setError("ユーザー情報の取得に失敗しました");
                console.error("Error fetching user:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchUserData();
    }, [uuid]);

    if (loading) {
        return (
            <div className="flex justify-center items-center py-12">
                <span className="loading loading-spinner loading-lg"></span>
            </div>
        );
    }

    if (error || !user) {
        return (
            <div className="alert alert-error">
                <span>{error || "ユーザーが見つかりません"}</span>
            </div>
        );
    }

    return (
        <div className="p-8 max-w-4xl mx-auto">


            <div className="card bg-base-100 shadow-lg border border-base-300">
                <div className="card-body">
                    <h1 className="card-title text-3xl mb-6">{user.name || user.username}</h1>

                    <div className="space-y-4">
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">UUID</p>
                                <p className="font-mono text-sm">{user.uuid}</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">ユーザー名</p>
                                <p>{user.username}</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">メール</p>
                                <p>{user.email || "-"}</p>
                            </div>
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">役割</p>
                                <span className="badge badge-primary">{user.role}</span>
                            </div>
                        </div>

                        {user.date_joined && (
                            <div className="bg-base-200 p-4 rounded-lg">
                                <p className="text-sm text-gray-500 mb-1">登録日</p>
                                <p>{new Date(user.date_joined).toLocaleDateString("ja-JP")}</p>
                            </div>
                        )}

                        {user.is_staff && (
                            <div className="bg-base-200 p-4 rounded-lg">
                                <span className="badge badge-secondary">スタッフ</span>
                            </div>
                        )}
                    </div>
                </div>
            </div>

            {/* Student Info */}
            {studentInfo && (
                <div className="card bg-base-100 shadow-lg border border-base-300 mt-6">
                    <div className="card-body">
                        <h2 className="card-title text-2xl mb-4">生徒情報</h2>
                        <div className="space-y-4">
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div className="bg-base-200 p-4 rounded-lg">
                                    <p className="text-sm text-gray-500 mb-1">学籍番号</p>
                                    <p className="font-mono">{studentInfo.student_id}</p>
                                </div>
                                {studentInfo.school_class && (
                                    <div className="bg-base-200 p-4 rounded-lg">
                                        <p className="text-sm text-gray-500 mb-1">クラス</p>
                                        <Link
                                            to={`/school-classes/${studentInfo.school_class}`}
                                            className="link link-primary hover:underline"
                                        >
                                            {studentInfo.school_class_str}
                                        </Link>
                                    </div>
                                )}
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* Teacher Info */}
            {teacherInfo && (
                <div className="card bg-base-100 shadow-lg border border-base-300 mt-6">
                    <div className="card-body">
                        <h2 className="card-title text-2xl mb-4">教師情報</h2>
                        <div className="space-y-4">
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                {teacherInfo.department && (
                                    <div className="bg-base-200 p-4 rounded-lg">
                                        <p className="text-sm text-gray-500 mb-1">所属学部</p>
                                        <Link
                                            to={`/departments/${teacherInfo.department}`}
                                            className="link link-primary hover:underline"
                                        >
                                            {teacherInfo.department_name}
                                        </Link>
                                    </div>
                                )}
                                {teacherInfo.department_type && (
                                    <div className="bg-base-200 p-4 rounded-lg">
                                        <p className="text-sm text-gray-500 mb-1">学部タイプ</p>
                                        <p>{teacherInfo.department_type}</p>
                                    </div>
                                )}
                                {teacherInfo.subdomain && (
                                    <div className="bg-base-200 p-4 rounded-lg">
                                        <p className="text-sm text-gray-500 mb-1">サブドメイン</p>
                                        <p className="font-mono">{teacherInfo.subdomain}</p>
                                    </div>
                                )}
                            </div>
                            {teacherInfo.owner && (
                                <div className="bg-base-200 p-4 rounded-lg">
                                    <span className="badge badge-accent">オーナー</span>
                                </div>
                            )}
                            {teacherInfo.subjects.length > 0 && (
                                <div className="bg-base-200 p-4 rounded-lg">
                                    <p className="text-sm text-gray-500 mb-2">担当教科</p>
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
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}
