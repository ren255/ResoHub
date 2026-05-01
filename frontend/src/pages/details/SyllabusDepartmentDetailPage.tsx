import { useParams } from "react-router-dom";
import { SyllabusDepartmentDetail } from "@features/organization/SyllabusDepartmentDetail";

export default function SyllabusDepartmentDetailPage() {
    const { id } = useParams<{ id: string }>();

    if (!id) {
        return (
            <div className="alert alert-error">
                <span>シラバス学部IDが指定されていません</span>
            </div>
        );
    }

    return <SyllabusDepartmentDetail id={Number(id)} />;
}
