// .ladle/components.tsx
import type { GlobalProvider } from "@ladle/react";
import "../layouts/tailwind.css";

export const Provider: GlobalProvider = ({ children }) => {
  return <>{children}</>;
};
