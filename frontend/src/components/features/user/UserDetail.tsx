import { useEffect, useState } from "react";
import { userRetrieve } from "@/types/api/sdk.gen";
import type { User } from "@/types/api/types.gen";
import { DetailPage, DetailSection, LinkField } from "@ui/DetailPage";

interface UserDetailProps {
    uuid: string;
}

export const UserDetail = ({ uuid }: UserDetailProps) => {
    const [user, setUser] = useState<User | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchUser = async () => {
            try {
                setLoading(true);
                setError(null);
                const { data } = await userRetrieve({ path: { uuid } });
                if (data) {
                    setUser(data);
                }
            } catch (err) {
                setError("ユーザー情報の取得に失敗しました");
                console.error("Error fetching user:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchUser();
    }, [uuid]);

    if (!user && !loading && !error) {
        return (
            <div className="alert alert-error">
                <span>ユーザーが見つかりません</span>
            </div>
        );
    }

    const basicFields = [
        { label: "UUID", value: <span className="font-mono text-sm">{user?.uuid}</span> },
        { label: "ユーザー名", value: user?.username },
        { label: "メール", value: user?.email || "-" },
        { label: "役割", value: <span className="badge badge-primary">{user?.role}</span> },
    ];

    if (user?.date_joined) {
        basicFields.push({
            label: "登録日",
            value: new Date(user.date_joined).toLocaleDateString("ja-JP"),
        });
    }

    if (user?.is_staff) {
        basicFields.push({
            label: "権限",
            value: <span className="badge badge-secondary">スタッフ</span>,
        });
    }

    return (
        <DetailPage
            title={user?.name || user?.username || "ユーザー詳細"}
            loading={loading}
            error={error}
        >
            <DetailSection fields={basicFields} />
        </DetailPage>
    );
};
