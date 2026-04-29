import { useState, useEffect } from "react";
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
import {
    userList,
    userSettingList,
    studentInfoList,
    teacherInfoList,
    schoolList,
    departmentList,
    syllabusDepartmentList,
    schoolClassList,
    gradeClassList,
    subjectList,
    subjectGroupeList,
    examList,
    examGroupeList,
} from "@/types/api/sdk.gen";
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

type ObjectType =
    | "user"
    | "userSetting"
    | "studentInfo"
    | "teacherInfo"
    | "school"
    | "department"
    | "syllabusDepartment"
    | "schoolClass"
    | "gradeClass"
    | "subject"
    | "subjectGroupe"
    | "exam"
    | "examGroupe";

interface ObjectTypeOption {
    value: ObjectType;
    label: string;
}

const objectTypeOptions: ObjectTypeOption[] = [
    { value: "user", label: "ユーザー" },
    { value: "userSetting", label: "ユーザー設定" },
    { value: "studentInfo", label: "生徒情報" },
    { value: "teacherInfo", label: "教師情報" },
    { value: "school", label: "学校" },
    { value: "department", label: "学部" },
    { value: "syllabusDepartment", label: "シラバス学部" },
    { value: "schoolClass", label: "クラス" },
    { value: "gradeClass", label: "学年クラス" },
    { value: "subject", label: "教科" },
    { value: "subjectGroupe", label: "教科グループ" },
    { value: "exam", label: "試験" },
    { value: "examGroupe", label: "試験グループ" },
];

export default function ObjectSearchPage() {
    const [selectedType, setSelectedType] = useState<ObjectType>("user");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    // Data states
    const [users, setUsers] = useState<User[]>([]);
    const [userSettings, setUserSettings] = useState<UserSetting[]>([]);
    const [studentInfos, setStudentInfos] = useState<StudentInfo[]>([]);
    const [teacherInfos, setTeacherInfos] = useState<TeacherInfo[]>([]);
    const [schools, setSchools] = useState<School[]>([]);
    const [departments, setDepartments] = useState<Department[]>([]);
    const [syllabusDepartments, setSyllabusDepartments] = useState<SyllabusDepartment[]>([]);
    const [schoolClasses, setSchoolClasses] = useState<SchoolClass[]>([]);
    const [gradeClasses, setGradeClasses] = useState<GradeClass[]>([]);
    const [subjects, setSubjects] = useState<Subject[]>([]);
    const [subjectGroupes, setSubjectGroupes] = useState<SubjectGroupe[]>([]);
    const [exams, setExams] = useState<Exam[]>([]);
    const [examGroupes, setExamGroupes] = useState<ExamGroupe[]>([]);

    useEffect(() => {
        const fetchData = async () => {
            setLoading(true);
            setError(null);

            try {
                switch (selectedType) {
                    case "user": {
                        const { data } = await userList();
                        if (data) setUsers(data);
                        break;
                    }
                    case "userSetting": {
                        const { data } = await userSettingList();
                        if (data) setUserSettings(data);
                        break;
                    }
                    case "studentInfo": {
                        const { data } = await studentInfoList();
                        if (data) setStudentInfos(data);
                        break;
                    }
                    case "teacherInfo": {
                        const { data } = await teacherInfoList();
                        if (data) setTeacherInfos(data);
                        break;
                    }
                    case "school": {
                        const { data } = await schoolList();
                        if (data) setSchools(data);
                        break;
                    }
                    case "department": {
                        const { data } = await departmentList();
                        if (data) setDepartments(data);
                        break;
                    }
                    case "syllabusDepartment": {
                        const { data } = await syllabusDepartmentList();
                        if (data) setSyllabusDepartments(data);
                        break;
                    }
                    case "schoolClass": {
                        const { data } = await schoolClassList();
                        if (data) setSchoolClasses(data);
                        break;
                    }
                    case "gradeClass": {
                        const { data } = await gradeClassList();
                        if (data) setGradeClasses(data);
                        break;
                    }
                    case "subject": {
                        const { data } = await subjectList();
                        if (data) setSubjects(data);
                        break;
                    }
                    case "subjectGroupe": {
                        const { data } = await subjectGroupeList();
                        if (data) setSubjectGroupes(data);
                        break;
                    }
                    case "exam": {
                        const { data } = await examList();
                        if (data) setExams(data);
                        break;
                    }
                    case "examGroupe": {
                        const { data } = await examGroupeList();
                        if (data) setExamGroupes(data);
                        break;
                    }
                }
            } catch (err) {
                setError("データの取得に失敗しました");
                console.error("Error fetching data:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, [selectedType]);

    const renderCards = () => {
        switch (selectedType) {
            case "user":
                return users.map((user) => (
                    <a key={user.uuid} href="#" onClick={(e) => e.preventDefault()}>
                        <UserCard user={user} />
                    </a>
                ));
            case "userSetting":
                return userSettings.map((setting) => (
                    <a key={setting.id} href="#" onClick={(e) => e.preventDefault()}>
                        <UserSettingCard setting={setting} />
                    </a>
                ));
            case "studentInfo":
                return studentInfos.map((info) => (
                    <a key={info.id} href="#" onClick={(e) => e.preventDefault()}>
                        <StudentInfoCard info={info} />
                    </a>
                ));
            case "teacherInfo":
                return teacherInfos.map((info) => (
                    <a key={info.id} href="#" onClick={(e) => e.preventDefault()}>
                        <TeacherInfoCard info={info} />
                    </a>
                ));
            case "school":
                return schools.map((school) => (
                    <a key={school.id} href="#" onClick={(e) => e.preventDefault()}>
                        <SchoolCard school={school} />
                    </a>
                ));
            case "department":
                return departments.map((department) => (
                    <a key={department.id} href="#" onClick={(e) => e.preventDefault()}>
                        <DepartmentCard department={department} />
                    </a>
                ));
            case "syllabusDepartment":
                return syllabusDepartments.map((sd) => (
                    <a key={sd.id} href="#" onClick={(e) => e.preventDefault()}>
                        <SyllabusDepartmentCard syllabusDepartment={sd} />
                    </a>
                ));
            case "schoolClass":
                return schoolClasses.map((sc) => (
                    <a key={sc.id} href="#" onClick={(e) => e.preventDefault()}>
                        <SchoolClassCard schoolClass={sc} />
                    </a>
                ));
            case "gradeClass":
                return gradeClasses.map((gc) => (
                    <a key={gc.id} href="#" onClick={(e) => e.preventDefault()}>
                        <GradeClassCard gradeClass={gc} />
                    </a>
                ));
            case "subject":
                return subjects.map((subject) => (
                    <a key={subject.id} href="#" onClick={(e) => e.preventDefault()}>
                        <SubjectCard subject={subject} />
                    </a>
                ));
            case "subjectGroupe":
                return subjectGroupes.map((sg) => (
                    <a key={sg.id} href="#" onClick={(e) => e.preventDefault()}>
                        <SubjectGroupeCard subjectGroupe={sg} />
                    </a>
                ));
            case "exam":
                return exams.map((exam) => (
                    <a key={exam.id} href="#" onClick={(e) => e.preventDefault()}>
                        <ExamCard exam={exam} />
                    </a>
                ));
            case "examGroupe":
                return examGroupes.map((eg) => (
                    <a key={eg.id} href="#" onClick={(e) => e.preventDefault()}>
                        <ExamGroupeCard examGroupe={eg} />
                    </a>
                ));
            default:
                return null;
        }
    };

    const getItemCount = () => {
        switch (selectedType) {
            case "user":
                return users.length;
            case "userSetting":
                return userSettings.length;
            case "studentInfo":
                return studentInfos.length;
            case "teacherInfo":
                return teacherInfos.length;
            case "school":
                return schools.length;
            case "department":
                return departments.length;
            case "syllabusDepartment":
                return syllabusDepartments.length;
            case "schoolClass":
                return schoolClasses.length;
            case "gradeClass":
                return gradeClasses.length;
            case "subject":
                return subjects.length;
            case "subjectGroupe":
                return subjectGroupes.length;
            case "exam":
                return exams.length;
            case "examGroupe":
                return examGroupes.length;
            default:
                return 0;
        }
    };

    return (
        <div className="p-8">
            <h2 className="text-2xl font-bold mb-6">オブジェクト検索</h2>

            {/* Object Type Selector */}
            <div className="mb-6">
                <label className="label">
                    <span className="label-text">オブジェクトタイプ</span>
                </label>
                <select
                    className="select select-bordered w-full max-w-xs"
                    value={selectedType}
                    onChange={(e) => setSelectedType(e.target.value as ObjectType)}
                >
                    {objectTypeOptions.map((option) => (
                        <option key={option.value} value={option.value}>
                            {option.label}
                        </option>
                    ))}
                </select>
            </div>

            {/* Error Message */}
            {error && (
                <div className="alert alert-error mb-6">
                    <span>{error}</span>
                </div>
            )}

            {/* Loading */}
            {loading && (
                <div className="flex justify-center items-center py-12">
                    <span className="loading loading-spinner loading-lg"></span>
                </div>
            )}

            {/* Results */}
            {!loading && !error && (
                <div>
                    <p className="text-sm text-gray-500 mb-4">
                        {objectTypeOptions.find((o) => o.value === selectedType)?.label}: {getItemCount()}件
                    </p>
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
                        {renderCards()}
                    </div>
                </div>
            )}
        </div>
    );
}
