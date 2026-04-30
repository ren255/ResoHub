import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
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
                    <Link key={user.uuid} to={`/profile/${user.uuid}`} className="block hover:opacity-80 transition-opacity">
                        <UserCard user={user} />
                    </Link>
                ));
            case "userSetting":
                return userSettings.map((setting) => (
                    <Link key={setting.id} to={`/profile/${setting.user}`} className="block hover:opacity-80 transition-opacity">
                        <UserSettingCard setting={setting} />
                    </Link>
                ));
            case "studentInfo":
                return studentInfos.map((info) => (
                    <Link key={info.id} to={`/profile/${info.user}`} className="block hover:opacity-80 transition-opacity">
                        <StudentInfoCard info={info} />
                    </Link>
                ));
            case "teacherInfo":
                return teacherInfos.map((info) => (
                    <Link key={info.id} to={`/profile/${info.user}`} className="block hover:opacity-80 transition-opacity">
                        <TeacherInfoCard info={info} />
                    </Link>
                ));
            case "school":
                return schools.map((school) => (
                    <Link key={school.id} to={`/schools/${school.id}`} className="block hover:opacity-80 transition-opacity">
                        <SchoolCard school={school} />
                    </Link>
                ));
            case "department":
                return departments.map((department) => (
                    <Link key={department.id} to={`/departments/${department.id}`} className="block hover:opacity-80 transition-opacity">
                        <DepartmentCard department={department} />
                    </Link>
                ));
            case "syllabusDepartment":
                return syllabusDepartments.map((sd) => (
                    <Link key={sd.id} to={`/syllabus-departments/${sd.id}`} className="block hover:opacity-80 transition-opacity">
                        <SyllabusDepartmentCard syllabusDepartment={sd} />
                    </Link>
                ));
            case "schoolClass":
                return schoolClasses.map((sc) => (
                    <Link key={sc.id} to={`/school-classes/${sc.id}`} className="block hover:opacity-80 transition-opacity">
                        <SchoolClassCard schoolClass={sc} />
                    </Link>
                ));
            case "gradeClass":
                return gradeClasses.map((gc) => (
                    <Link key={gc.id} to={`/grade-classes/${gc.id}`} className="block hover:opacity-80 transition-opacity">
                        <GradeClassCard gradeClass={gc} />
                    </Link>
                ));
            case "subject":
                return subjects.map((subject) => (
                    <Link key={subject.id} to={`/subjects/${subject.id}`} className="block hover:opacity-80 transition-opacity">
                        <SubjectCard subject={subject} />
                    </Link>
                ));
            case "subjectGroupe":
                return subjectGroupes.map((sg) => (
                    <Link key={sg.id} to={`/subject-groupes/${sg.id}`} className="block hover:opacity-80 transition-opacity">
                        <SubjectGroupeCard subjectGroupe={sg} />
                    </Link>
                ));
            case "exam":
                return exams.map((exam) => (
                    <Link key={exam.id} to={`/exams/${exam.id}`} className="block hover:opacity-80 transition-opacity">
                        <ExamCard exam={exam} />
                    </Link>
                ));
            case "examGroupe":
                return examGroupes.map((eg) => (
                    <Link key={eg.id} to={`/exam-groupes/${eg.id}`} className="block hover:opacity-80 transition-opacity">
                        <ExamGroupeCard examGroupe={eg} />
                    </Link>
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
