import { UserCard } from "@features/user/UserCard";
import { UserSettingCard } from "@features/user/UserSettingCard";
import { StudentInfoCard } from "@features/user/StudentInfoCard";
import { TeacherInfoCard } from "@features/user/TeacherInfoCard";
import { SchoolCard } from "@features/organization/SchoolCard";
import { DepartmentCard } from "@features/organization/DepartmentCard";
import { SyllabusDepartmentCard } from "@features/organization/SyllabusDepartmentCard";
import { SchoolClassCard } from "@features/organization/SchoolClassCard";
import { GradeClassCard } from "@features/organization/GradeClassCard";
import { SubjectCard } from "@features/subject/SubjectCard";
import { SubjectGroupeCard } from "@features/subject/SubjectGroupeCard";
import { ExamCard } from "@features/exam/ExamCard";
import { ExamGroupeCard } from "@features/exam/ExamGroupeCard";
import type {
    User,
    UserSetting,
    StudentInfo,
    TeacherInfo,
    School,
    Department,
    SyllabusDepartment,
    SchoolClass,
    GradeClass,
    Subject,
    SubjectGroupe,
    Exam,
    ExamGroupe,
} from "@/types/api/types.gen";

// User mocks
const mockUser: User = {
    uuid: "123e4567-e89b-12d3-a456-426614174000",
    username: "admin_user",
    email: "admin@example.com",
    name: "管理者 太郎",
    role: "staff",
    is_staff: true,
    is_superuser: true,
    is_active: true,
    date_joined: "2024-01-15T10:30:00Z",
};

const mockUserSetting: UserSetting = {
    id: 1,
    user: "123e4567-e89b-12d3-a456-426614174000",
    user_name: "管理者 太郎",
};

const mockStudentInfo: StudentInfo = {
    id: 1,
    user: "123e4567-e89b-12d3-a456-426614174000",
    user_name: "学生 花子",
    student_id: "20240001",
    school_class: 1,
    school_class_str: "情報工学科 2024",
};

const mockTeacherInfo: TeacherInfo = {
    id: 1,
    user: "123e4567-e89b-12d3-a456-426614174001",
    user_name: "教員 一郎",
    department: 1,
    department_name: "情報工学部",
    department_type: "教授",
    owner: true,
    subdomain: "teacher1",
    subjects: [1, 2, 3],
};

// Organization mocks
const mockSchool: School = {
    id: 1,
    url: "https://example.com/school",
    name: "東京工科大学",
    code: "TKY",
};

const mockDepartment: Department = {
    id: 1,
    name: "情報工学部",
    school: 1,
    school_name: "東京工科大学",
};

const mockSyllabusDepartment: SyllabusDepartment = {
    id: 1,
    url: "https://example.com/syllabus",
    name: "情報工学科 2024",
    admission_year: 2024,
    code: "I2024",
    school: 1,
    school_name: "東京工科大学",
    department: 1,
    department_name: "情報工学部",
};

const mockSchoolClass: SchoolClass = {
    id: 1,
    department: 1,
    department_name: "情報工学部",
    syllabus_department: 1,
    syllabus_department_name: "情報工学科 2024",
    admission_year: 2024,
};

const mockGradeClass: GradeClass = {
    id: 1,
    school_class: 1,
    school_class_str: "情報工学科 2024",
    grade_str: "1年",
    grade: 1,
    year: 2024,
};

// Subject mocks
const mockSubject: Subject = {
    id: 1,
    name: "プログラミング基礎",
    code: "PRO101",
    subject_type: "必修",
    credits: 2,
    teachers_str: "山田太郎, 佐藤花子",
    textbooks: "プログラミング入門",
    url: "https://example.com/subject",
    grade_class: 1,
    grade_class_str: "情報工学科 2024 1年",
    subject_groupe: 1,
};

const mockSubjectGroupe: SubjectGroupe = {
    id: 1,
};

// Exam mocks
const mockExam: Exam = {
    id: 1,
    url: "https://example.com/exam",
    quarter: 1,
    week: 3,
    content: "変数とデータ型",
    goal: "基本的な変数の使い方を理解する",
    subject: 1,
    subject_name: "プログラミング基礎",
    exam_groupe: 1,
    file: 1,
};

const mockExamGroupe: ExamGroupe = {
    id: 1,
    subject: 1,
    subject_name: "プログラミング基礎",
    subject_groupe: 1,
};

// User Cards
export function UserCardStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">UserCard</h2>
            <UserCard user={mockUser} />
        </div>
    );
}

export function UserSettingCardStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">UserSettingCard</h2>
            <UserSettingCard setting={mockUserSetting} />
        </div>
    );
}

export function StudentInfoCardStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">StudentInfoCard</h2>
            <StudentInfoCard info={mockStudentInfo} />
        </div>
    );
}

export function TeacherInfoCardStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">TeacherInfoCard</h2>
            <TeacherInfoCard info={mockTeacherInfo} />
        </div>
    );
}

// Organization Cards
export function SchoolCardStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">SchoolCard</h2>
            <SchoolCard school={mockSchool} />
        </div>
    );
}

export function DepartmentCardStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">DepartmentCard</h2>
            <DepartmentCard department={mockDepartment} />
        </div>
    );
}

export function SyllabusDepartmentCardStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">SyllabusDepartmentCard</h2>
            <SyllabusDepartmentCard syllabusDepartment={mockSyllabusDepartment} />
        </div>
    );
}

export function SchoolClassCardStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">SchoolClassCard</h2>
            <SchoolClassCard schoolClass={mockSchoolClass} />
        </div>
    );
}

export function GradeClassCardStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">GradeClassCard</h2>
            <GradeClassCard gradeClass={mockGradeClass} />
        </div>
    );
}

// Subject Cards
export function SubjectCardStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">SubjectCard</h2>
            <SubjectCard subject={mockSubject} />
        </div>
    );
}

export function SubjectGroupeCardStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">SubjectGroupeCard</h2>
            <SubjectGroupeCard subjectGroupe={mockSubjectGroupe} />
        </div>
    );
}

// Exam Cards
export function ExamCardStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">ExamCard</h2>
            <ExamCard exam={mockExam} />
        </div>
    );
}

export function ExamGroupeCardStory() {
    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">ExamGroupeCard</h2>
            <ExamGroupeCard examGroupe={mockExamGroupe} />
        </div>
    );
}

// All Cards
export function AllCards() {
    return (
        <div className="p-4 space-y-8">
            <h2 className="text-2xl font-bold">すべてのCardコンポーネント</h2>

            <section>
                <h3 className="text-xl font-semibold mb-4">User関連</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <UserCard user={mockUser} />
                    <UserSettingCard setting={mockUserSetting} />
                    <StudentInfoCard info={mockStudentInfo} />
                    <TeacherInfoCard info={mockTeacherInfo} />
                </div>
            </section>

            <section>
                <h3 className="text-xl font-semibold mb-4">Organization関連</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <SchoolCard school={mockSchool} />
                    <DepartmentCard department={mockDepartment} />
                    <SyllabusDepartmentCard syllabusDepartment={mockSyllabusDepartment} />
                    <SchoolClassCard schoolClass={mockSchoolClass} />
                    <GradeClassCard gradeClass={mockGradeClass} />
                </div>
            </section>

            <section>
                <h3 className="text-xl font-semibold mb-4">Subject関連</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <SubjectCard subject={mockSubject} />
                    <SubjectGroupeCard subjectGroupe={mockSubjectGroupe} />
                </div>
            </section>

            <section>
                <h3 className="text-xl font-semibold mb-4">Exam関連</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <ExamCard exam={mockExam} />
                    <ExamGroupeCard examGroupe={mockExamGroupe} />
                </div>
            </section>
        </div>
    );
}
