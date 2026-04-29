// .ladle/components.tsx
import "src/layouts/tailwind.css";
import { BrowserRouter } from "react-router-dom";
import type { Story } from "@ladle/react";

export const Provider = ({ children }: { children: React.ReactNode }) => (
    <BrowserRouter>
        {children}
    </BrowserRouter>
);
