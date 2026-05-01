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
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">UserDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します
            </p>
            <UserDetail uuid="ffaf3eee-5a9e-49d5-9440-0afa8d63e4e9" />
        </div>
    );
}

export function TeacherInfoDetailStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">TeacherInfoDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します
            </p>
            <TeacherInfoDetail userUuid="f2329aee-890f-4aa5-9422-acdf85e40f61" />
        </div>
    );
}

export function StudentInfoDetailStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">StudentInfoDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します
            </p>
            <StudentInfoDetail userUuid="ffaf3eee-5a9e-49d5-9440-0afa8d63e4e9" />
        </div>
    );
}

// Organization Detail Stories
export function DepartmentDetailStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">DepartmentDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します
            </p>
            <DepartmentDetail id={20} />
        </div>
    );
}

export function SchoolDetailStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">SchoolDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します
            </p>
            <SchoolDetail id={1} />
        </div>
    );
}

export function SchoolClassDetailStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">SchoolClassDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します
            </p>
            <SchoolClassDetail id={1} />
        </div>
    );
}

export function SyllabusDepartmentDetailStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">SyllabusDepartmentDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します
            </p>
            <SyllabusDepartmentDetail id={1} />
        </div>
    );
}

export function GradeClassDetailStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">GradeClassDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します
            </p>
            <GradeClassDetail id={1} />
        </div>
    );
}

// Subject Detail Stories
export function SubjectDetailStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">SubjectDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します
            </p>
            <SubjectDetail id={1} />
        </div>
    );
}

export function SubjectGroupeDetailStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">SubjectGroupeDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します
            </p>
            <SubjectGroupeDetail id={1} />
        </div>
    );
}

// Exam Detail Stories
export function ExamDetailStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">ExamDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します
            </p>
            <ExamDetail id={1} />
        </div>
    );
}

export function ExamGroupeDetailStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">ExamGroupeDetail (実データ)</h2>
            <p className="text-sm text-gray-500 mb-4">
                注意: このコンポーネントは実際のAPIを呼び出します
            </p>
            <ExamGroupeDetail id={1} />
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
