import { useParams } from "react-router-dom";
import { ExamGroupeDetail } from "@features/exam/ExamGroupeDetail";

export default function ExamGroupeDetailPage() {
    const { id } = useParams<{ id: string }>();

    if (!id) {
        return (
            <div className="alert alert-error">
                <span>試験グループIDが指定されていません</span>
            </div>
        );
    }

    return <ExamGroupeDetail id={Number(id)} />;
}
