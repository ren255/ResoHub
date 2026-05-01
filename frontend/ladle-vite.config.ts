// ladle-vite.config.ts
import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";
import { resolve } from "path";

export default defineConfig({
  plugins: [react()],
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
    watch: {
      usePolling: true,
      interval: 1000,
    },
  },
});
