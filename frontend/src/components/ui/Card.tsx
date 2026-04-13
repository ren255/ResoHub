export const Card = ({
  title = "カードタイトル",
  description = "説明文説明文説明文説明文説明文説明文説明文説明文説明文説明文説明文説明文説明文説明文説明文説明文",
}: {
  title?: string;
  description?: string;
}) => (
  <div className="border border-gray-300 rounded-lg p-6 max-w-md shadow-sm">
    <h2 className="text-2xl font-bold mb-3">{title}</h2>
    <p className="text-base text-gray-700">{description}</p>
  </div>
);
