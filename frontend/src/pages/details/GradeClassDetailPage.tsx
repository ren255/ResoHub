import { useParams } from "react-router-dom";
import { GradeClassDetail } from "@features/organization/GradeClassDetail";

export default function GradeClassDetailPage() {
    const { id } = useParams<{ id: string }>();

    if (!id) {
        return (
            <div className="alert alert-error">
                <span>学年クラスIDが指定されていません</span>
            </div>
        );
    }

    return <GradeClassDetail id={Number(id)} />;
}
