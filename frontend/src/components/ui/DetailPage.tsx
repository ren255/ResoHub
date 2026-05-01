import { Link } from "react-router-dom";

interface DetailField {
    label: string;
    value: React.ReactNode;
}

interface DetailSectionProps {
    title?: string;
    fields: DetailField[];
    columns?: 1 | 2;
}

export const DetailSection = ({ title, fields, columns = 2 }: DetailSectionProps) => (
    <div className="mb-8">
        {title && <h2 className="text-2xl font-bold mb-4">{title}</h2>}
        <div className={`grid gap-4 ${columns === 2 ? "grid-cols-1 md:grid-cols-2" : "grid-cols-1"}`}>
            {fields.map((field, index) => (
                <div key={index} className="bg-base-200 p-4 rounded-lg">
                    <p className="text-sm text-gray-500 mb-1">{field.label}</p>
                    <div className="font-medium">{field.value}</div>
                </div>
            ))}
        </div>
    </div>
);

interface DetailPageProps {
    title: string;
    children?: React.ReactNode;
    loading?: boolean;
    error?: string | null;
}

export const DetailPage = ({ title, children, loading, error }: DetailPageProps) => {
    if (loading) {
        return (
            <div className="flex justify-center items-center py-12">
                <span className="loading loading-spinner loading-lg"></span>
            </div>
        );
    }

    if (error) {
        return (
            <div className="alert alert-error">
                <span>{error}</span>
            </div>
        );
    }

    return (
        <div className="p-8 max-w-4xl mx-auto">
            <h1 className="text-3xl font-bold mb-8">{title}</h1>
            {children}
        </div>
    );
};

interface LinkFieldProps {
    to: string;
    children: React.ReactNode;
}

export const LinkField = ({ to, children }: LinkFieldProps) => (
    <Link to={to} className="link link-primary hover:underline">
        {children}
    </Link>
);

interface ExternalLinkFieldProps {
    href: string;
    children: React.ReactNode;
}

export const ExternalLinkField = ({ href, children }: ExternalLinkFieldProps) => (
    <a
        href={href}
        target="_blank"
        rel="noopener noreferrer"
        className="link link-primary hover:underline"
    >
        {children}
    </a>
);
