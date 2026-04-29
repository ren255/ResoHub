import { Route, Routes } from "react-router-dom";
import LayoutDefault from "@/layouts/LayoutDefault";
import ErrorPage from "@/pages/ErrorPage";
import IndexPage from "@/pages/IndexPage";
import UsersPage from "@/pages/UsersPage";
import ObjectSearchPage from "@/pages/ObjectSearchPage";

export default function App() {
    return (
        <Routes>
            <Route element={<LayoutDefault />}>
                <Route path="/" element={<IndexPage />} />
                <Route path="/users" element={<UsersPage />} />
                <Route path="/obj-search" element={<ObjectSearchPage />} />
                <Route path="*" element={<ErrorPage />} />
            </Route>
        </Routes>
    );
}
