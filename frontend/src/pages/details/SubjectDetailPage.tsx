import { useParams } from "react-router-dom";
import { SubjectDetail } from "@features/subject/SubjectDetail";

export default function SubjectDetailPage() {
    const { id } = useParams<{ id: string }>();

    if (!id) {
        return (
            <div className="alert alert-error">
                <span>教科IDが指定されていません</span>
            </div>
        );
    }

    return <SubjectDetail id={Number(id)} />;
}
