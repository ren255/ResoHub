import { useParams } from "react-router-dom";
import { SchoolDetail } from "@features/organization/SchoolDetail";

export default function SchoolDetailPage() {
    const { id } = useParams<{ id: string }>();

    if (!id) {
        return (
            <div className="alert alert-error">
                <span>学校IDが指定されていません</span>
            </div>
        );
    }

    return <SchoolDetail id={Number(id)} />;
}
