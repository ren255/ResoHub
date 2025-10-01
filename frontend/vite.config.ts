import tailwindcss from "@tailwindcss/vite";
import react from "@vitejs/plugin-react";
import vike from "vike/plugin";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [vike(), react(), tailwindcss()],
  build: {
    target: "es2022",
  },
  server: {
    proxy: {
      "/api": {
        target: "http://resohub-backend:8000",
        changeOrigin: true,        
    }}
}});