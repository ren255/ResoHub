import { useParams } from "react-router-dom";
import { SubjectGroupeDetail } from "@features/subject/SubjectGroupeDetail";

export default function SubjectGroupeDetailPage() {
    const { id } = useParams<{ id: string }>();

    if (!id) {
        return (
            <div className="alert alert-error">
                <span>教科グループIDが指定されていません</span>
            </div>
        );
    }

    return <SubjectGroupeDetail id={Number(id)} />;
}
