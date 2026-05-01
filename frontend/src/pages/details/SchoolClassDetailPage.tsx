import { useParams } from "react-router-dom";
import { SchoolClassDetail } from "@features/organization/SchoolClassDetail";

export default function SchoolClassDetailPage() {
    const { id } = useParams<{ id: string }>();

    if (!id) {
        return (
            <div className="alert alert-error">
                <span>クラスIDが指定されていません</span>
            </div>
        );
    }

    return <SchoolClassDetail id={Number(id)} />;
}
