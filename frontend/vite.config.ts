import tailwindcss from "@tailwindcss/vite";
import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";
import { resolve } from "path";

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": resolve(__dirname, "./src"),
      "@features": resolve(__dirname, "./src/components/features"),
      "@layouts": resolve(__dirname, "./src/components/layouts"),
      "@stories": resolve(__dirname, "./src/components/stories"),
      "@ui": resolve(__dirname, "./src/components/ui"),
    },
  },
  build: {
    target: "es2022",
  },
  server: {
    proxy: {
      "/api": {
        target: "http://resohub-backend:8000",
        changeOrigin: true,
      },
    },
    allowedHosts: ["resohub.rentoda.com"],
  },
});