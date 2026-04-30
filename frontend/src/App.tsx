import { Route, Routes } from "react-router-dom";
import LayoutDefault from "@/layouts/LayoutDefault";
import ErrorPage from "@/pages/ErrorPage";
import IndexPage from "@/pages/IndexPage";
import UsersPage from "@/pages/UsersPage";
import ObjectSearchPage from "@/pages/ObjectSearchPage";

// Detail pages
import ProfilePage from "@/pages/details/ProfilePage";
import SchoolDetailPage from "@/pages/details/SchoolDetailPage";
import DepartmentDetailPage from "@/pages/details/DepartmentDetailPage";
import SyllabusDepartmentDetailPage from "@/pages/details/SyllabusDepartmentDetailPage";
import SchoolClassDetailPage from "@/pages/details/SchoolClassDetailPage";
import GradeClassDetailPage from "@/pages/details/GradeClassDetailPage";
import SubjectDetailPage from "@/pages/details/SubjectDetailPage";
import SubjectGroupeDetailPage from "@/pages/details/SubjectGroupeDetailPage";
import ExamDetailPage from "@/pages/details/ExamDetailPage";
import ExamGroupeDetailPage from "@/pages/details/ExamGroupeDetailPage";

export default function App() {
    return (
        <Routes>
            <Route element={<LayoutDefault />}>
                <Route path="/" element={<IndexPage />} />
                <Route path="/users" element={<UsersPage />} />
                <Route path="/obj-search" element={<ObjectSearchPage />} />

                {/* Detail pages */}
                <Route path="/profile/:uuid" element={<ProfilePage />} />
                <Route path="/schools/:id" element={<SchoolDetailPage />} />
                <Route path="/departments/:id" element={<DepartmentDetailPage />} />
                <Route path="/syllabus-departments/:id" element={<SyllabusDepartmentDetailPage />} />
                <Route path="/school-classes/:id" element={<SchoolClassDetailPage />} />
                <Route path="/grade-classes/:id" element={<GradeClassDetailPage />} />
                <Route path="/subjects/:id" element={<SubjectDetailPage />} />
                <Route path="/subject-groupes/:id" element={<SubjectGroupeDetailPage />} />
                <Route path="/exams/:id" element={<ExamDetailPage />} />
                <Route path="/exam-groupes/:id" element={<ExamGroupeDetailPage />} />

                <Route path="*" element={<ErrorPage />} />
            </Route>
        </Routes>
    );
}
