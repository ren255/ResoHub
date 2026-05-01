import { useParams } from "react-router-dom";
import { DepartmentDetail } from "@features/organization/DepartmentDetail";

export default function DepartmentDetailPage() {
    const { id } = useParams<{ id: string }>();

    if (!id) {
        return (
            <div className="alert alert-error">
                <span>学部IDが指定されていません</span>
            </div>
        );
    }

    return <DepartmentDetail id={Number(id)} />;
}
