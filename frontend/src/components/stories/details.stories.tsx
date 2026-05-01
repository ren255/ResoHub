import { useState, useEffect } from "react";
import { UserDetail } from "@features/user/UserDetail";
import { TeacherInfoDetail } from "@features/user/TeacherInfoDetail";
import { StudentInfoDetail } from "@features/user/StudentInfoDetail";
import { DepartmentDetail } from "@features/organization/DepartmentDetail";
import { SchoolDetail } from "@features/organization/SchoolDetail";
import { SchoolClassDetail } from "@features/organization/SchoolClassDetail";
import { SyllabusDepartmentDetail } from "@features/organization/SyllabusDepartmentDetail";
import { GradeClassDetail } from "@features/organization/GradeClassDetail";
import { SubjectDetail } from "@features/subject/SubjectDetail";
import { SubjectGroupeDetail } from "@features/subject/SubjectGroupeDetail";
import { ExamDetail } from "@features/exam/ExamDetail";
import { ExamGroupeDetail } from "@features/exam/ExamGroupeDetail";
import { DetailPage, DetailSection, LinkField, ExternalLinkField } from "@ui/DetailPage";
import {
    userList,
    departmentList,
    schoolList,
    schoolClassList,
    syllabusDepartmentList,
    gradeClassList,
    subjectList,
    subjectGroupeList,
    examList,
    examGroupeList,
} from "@/types/api/sdk.gen";

// Helper to get random item from array
function getRandomId<T extends { id: number }>(items: T[]): number | null {
    if (!items || items.length === 0) return null;
    const randomItem = items[Math.floor(Math.random() * items.length)];
    return randomItem.id;
}

// Helper to get random UUID from array
function getRandomUuid<T extends { uuid: string }>(items: T[]): string | null {
    if (!items || items.length === 0) return null;
    const randomItem = items[Math.floor(Math.random() * items.length)];
    return randomItem.uuid;
}

// DetailPage Base Component Stories
export function DetailPageBaseStory() {
    return (
        <DetailPage title="サンプル詳細ページ" loading={false} error={null}>
            <DetailSection
                fields={[
                    { label: "ID", value: <span className="font-mono">123</span> },
                    { label: "名前", value: "サンプル名前" },
                    { label: "メール", value: "sample@example.com" },
                    { label: "役割", value: <span className="badge badge-primary">管理者</span> },
                ]}
            />
        </DetailPage>
    );
}

export function DetailPageLoadingStory() {
    return <DetailPage title="読み込み中..." loading={true} error={null} />;
}

export function DetailPageErrorStory() {
    return <DetailPage title="エラー" loading={false} error="データの取得に失敗しました" />;
}

export function DetailSectionSingleColumnStory() {
    return (
        <div className="p-8 max-w-4xl mx-auto">
            <h1 className="text-3xl font-bold mb-8">1列表示</h1>
            <DetailSection
                title="追加情報"
                fields={[
                    { label: "内容", value: "これは長いテキストコンテンツです。" },
                    { label: "目標", value: "目標設定のテキストです。" },
                    { label: "備考", value: "備考欄のテキストです。" },
                ]}
                columns={1}
            />
        </div>
    );
}

export function LinkFieldStory() {
    return (
        <div className="p-8 max-w-4xl mx-auto">
            <h1 className="text-3xl font-bold mb-8">リンクフィールド</h1>
            <DetailSection
                fields={[
                    { label: "内部リンク", value: <LinkField to="/users/1">ユーザー詳細</LinkField> },
                    {
                        label: "外部リンク",
                        value: <ExternalLinkField href="https://example.com">Example</ExternalLinkField>,
                    },
                ]}
            />
        </div>
    );
}

// User Detail Stories
export function UserDetailStory() {
    const [uuid, setUuid] = useState<string | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        userList({ query: { page: 1 } })
            .then((response) => {
                const results = response.data?.results || [];
                const randomUuid = getRandomUuid(results);
                setUuid(randomUuid);
                setLoading(false);
            })
            .catch(() => setLoading(false));
    }, []);

    if (loading) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">UserDetail (実データ)</h2>
                <div className="alert alert-info">読み込み中...</div>
            </div>
        );
    }

    if (!uuid) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">UserDetail (実データ)</h2>
                <div className="alert alert-warning">データが見つかりません</div>
            </div>
        );
    }

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">UserDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します (UUID: {uuid})
            </p>
            <UserDetail uuid={uuid} />
        </div>
    );
}

export function TeacherInfoDetailStory() {
    const [uuid, setUuid] = useState<string | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        userList({ query: { page: 1 } })
            .then((response) => {
                const results = response.data?.results || [];
                const randomUuid = getRandomUuid(results);
                setUuid(randomUuid);
                setLoading(false);
            })
            .catch(() => setLoading(false));
    }, []);

    if (loading) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">TeacherInfoDetail (実データ)</h2>
                <div className="alert alert-info">読み込み中...</div>
            </div>
        );
    }

    if (!uuid) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">TeacherInfoDetail (実データ)</h2>
                <div className="alert alert-warning">データが見つかりません</div>
            </div>
        );
    }

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">TeacherInfoDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します (UUID: {uuid})
            </p>
            <TeacherInfoDetail userUuid={uuid} />
        </div>
    );
}

export function StudentInfoDetailStory() {
    const [uuid, setUuid] = useState<string | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        userList({ query: { page: 1 } })
            .then((response) => {
                const results = response.data?.results || [];
                const randomUuid = getRandomUuid(results);
                setUuid(randomUuid);
                setLoading(false);
            })
            .catch(() => setLoading(false));
    }, []);

    if (loading) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">StudentInfoDetail (実データ)</h2>
                <div className="alert alert-info">読み込み中...</div>
            </div>
        );
    }

    if (!uuid) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">StudentInfoDetail (実データ)</h2>
                <div className="alert alert-warning">データが見つかりません</div>
            </div>
        );
    }

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">StudentInfoDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します (UUID: {uuid})
            </p>
            <StudentInfoDetail userUuid={uuid} />
        </div>
    );
}

// Organization Detail Stories
export function DepartmentDetailStory() {
    const [id, setId] = useState<number | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        departmentList({ query: { page: 1 } })
            .then((response) => {
                const results = response.data?.results || [];
                const randomId = getRandomId(results);
                setId(randomId);
                setLoading(false);
            })
            .catch(() => setLoading(false));
    }, []);

    if (loading) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">DepartmentDetail (実データ)</h2>
                <div className="alert alert-info">読み込み中...</div>
            </div>
        );
    }

    if (!id) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">DepartmentDetail (実データ)</h2>
                <div className="alert alert-warning">データが見つかりません</div>
            </div>
        );
    }

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">DepartmentDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します (ID: {id})
            </p>
            <DepartmentDetail id={id} />
        </div>
    );
}

export function SchoolDetailStory() {
    const [id, setId] = useState<number | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        schoolList({ query: { page: 1 } })
            .then((response) => {
                const results = response.data?.results || [];
                const randomId = getRandomId(results);
                setId(randomId);
                setLoading(false);
            })
            .catch(() => setLoading(false));
    }, []);

    if (loading) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">SchoolDetail (実データ)</h2>
                <div className="alert alert-info">読み込み中...</div>
            </div>
        );
    }

    if (!id) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">SchoolDetail (実データ)</h2>
                <div className="alert alert-warning">データが見つかりません</div>
            </div>
        );
    }

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">SchoolDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します (ID: {id})
            </p>
            <SchoolDetail id={id} />
        </div>
    );
}

export function SchoolClassDetailStory() {
    const [id, setId] = useState<number | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        schoolClassList({ query: { page: 1 } })
            .then((response) => {
                const results = response.data?.results || [];
                const randomId = getRandomId(results);
                setId(randomId);
                setLoading(false);
            })
            .catch(() => setLoading(false));
    }, []);

    if (loading) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">SchoolClassDetail (実データ)</h2>
                <div className="alert alert-info">読み込み中...</div>
            </div>
        );
    }

    if (!id) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">SchoolClassDetail (実データ)</h2>
                <div className="alert alert-warning">データが見つかりません</div>
            </div>
        );
    }

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">SchoolClassDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します (ID: {id})
            </p>
            <SchoolClassDetail id={id} />
        </div>
    );
}

export function SyllabusDepartmentDetailStory() {
    const [id, setId] = useState<number | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        syllabusDepartmentList({ query: { page: 1 } })
            .then((response) => {
                const results = response.data?.results || [];
                const randomId = getRandomId(results);
                setId(randomId);
                setLoading(false);
            })
            .catch(() => setLoading(false));
    }, []);

    if (loading) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">SyllabusDepartmentDetail (実データ)</h2>
                <div className="alert alert-info">読み込み中...</div>
            </div>
        );
    }

    if (!id) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">SyllabusDepartmentDetail (実データ)</h2>
                <div className="alert alert-warning">データが見つかりません</div>
            </div>
        );
    }

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">SyllabusDepartmentDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します (ID: {id})
            </p>
            <SyllabusDepartmentDetail id={id} />
        </div>
    );
}

export function GradeClassDetailStory() {
    const [id, setId] = useState<number | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        gradeClassList({ query: { page: 1 } })
            .then((response) => {
                const results = response.data?.results || [];
                const randomId = getRandomId(results);
                setId(randomId);
                setLoading(false);
            })
            .catch(() => setLoading(false));
    }, []);

    if (loading) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">GradeClassDetail (実データ)</h2>
                <div className="alert alert-info">読み込み中...</div>
            </div>
        );
    }

    if (!id) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">GradeClassDetail (実データ)</h2>
                <div className="alert alert-warning">データが見つかりません</div>
            </div>
        );
    }

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">GradeClassDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します (ID: {id})
            </p>
            <GradeClassDetail id={id} />
        </div>
    );
}

// Subject Detail Stories
export function SubjectDetailStory() {
    const [id, setId] = useState<number | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        subjectList({ query: { page: 1 } })
            .then((response) => {
                const results = response.data?.results || [];
                const randomId = getRandomId(results);
                setId(randomId);
                setLoading(false);
            })
            .catch(() => setLoading(false));
    }, []);

    if (loading) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">SubjectDetail (実データ)</h2>
                <div className="alert alert-info">読み込み中...</div>
            </div>
        );
    }

    if (!id) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">SubjectDetail (実データ)</h2>
                <div className="alert alert-warning">データが見つかりません</div>
            </div>
        );
    }

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">SubjectDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します (ID: {id})
            </p>
            <SubjectDetail id={id} />
        </div>
    );
}

export function SubjectGroupeDetailStory() {
    const [id, setId] = useState<number | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        subjectGroupeList({ query: { page: 1 } })
            .then((response) => {
                const results = response.data?.results || [];
                const randomId = getRandomId(results);
                setId(randomId);
                setLoading(false);
            })
            .catch(() => setLoading(false));
    }, []);

    if (loading) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">SubjectGroupeDetail (実データ)</h2>
                <div className="alert alert-info">読み込み中...</div>
            </div>
        );
    }

    if (!id) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">SubjectGroupeDetail (実データ)</h2>
                <div className="alert alert-warning">データが見つかりません</div>
            </div>
        );
    }

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">SubjectGroupeDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します (ID: {id})
            </p>
            <SubjectGroupeDetail id={id} />
        </div>
    );
}

// Exam Detail Stories
export function ExamDetailStory() {
    const [id, setId] = useState<number | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        examList({ query: { page: 1 } })
            .then((response) => {
                const results = response.data?.results || [];
                const randomId = getRandomId(results);
                setId(randomId);
                setLoading(false);
            })
            .catch(() => setLoading(false));
    }, []);

    if (loading) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">ExamDetail (実データ)</h2>
                <div className="alert alert-info">読み込み中...</div>
            </div>
        );
    }

    if (!id) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">ExamDetail (実データ)</h2>
                <div className="alert alert-warning">データが見つかりません</div>
            </div>
        );
    }

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">ExamDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します (ID: {id})
            </p>
            <ExamDetail id={id} />
        </div>
    );
}

export function ExamGroupeDetailStory() {
    const [id, setId] = useState<number | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        examGroupeList({ query: { page: 1 } })
            .then((response) => {
                const results = response.data?.results || [];
                const randomId = getRandomId(results);
                setId(randomId);
                setLoading(false);
            })
            .catch(() => setLoading(false));
    }, []);

    if (loading) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">ExamGroupeDetail (実データ)</h2>
                <div className="alert alert-info">読み込み中...</div>
            </div>
        );
    }

    if (!id) {
        return (
            <div className="p-4">
                <h2 className="text-xl font-bold mb-4">ExamGroupeDetail (実データ)</h2>
                <div className="alert alert-warning">データが見つかりません</div>
            </div>
        );
    }

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">ExamGroupeDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します (ID: {id})
            </p>
            <ExamGroupeDetail id={id} />
        </div>
    );
}

// All Details Overview
export function AllDetailsOverview() {
    return (
        <div className="p-4 space-y-8">
            <h2 className="text-2xl font-bold">Detailコンポーネント一覧</h2>
            <p className="text-sm text-gray-500">
                以下はベースコンポーネントの表示例です。各Detailコンポーネントは実際のAPIを呼び出します。
            </p>

            <section>
                <h3 className="text-xl font-semibold mb-4">ベースコンポーネント</h3>
                <div className="space-y-4">
                    <DetailPageBaseStory />
                </div>
            </section>
        </div>
    );
}
