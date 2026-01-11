// ladle-vite.config.ts
import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [react()],
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