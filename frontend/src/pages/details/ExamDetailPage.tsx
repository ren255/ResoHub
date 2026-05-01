import { useParams } from "react-router-dom";
import { ExamDetail } from "@features/exam/ExamDetail";

export default function ExamDetailPage() {
    const { id } = useParams<{ id: string }>();

    if (!id) {
        return (
            <div className="alert alert-error">
                <span>試験IDが指定されていません</span>
            </div>
        );
    }

    return <ExamDetail id={Number(id)} />;
}
