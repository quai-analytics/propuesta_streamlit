import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173
  },
  // Servimos la carpeta ../image como "public" para poder usar tu logo existente
  publicDir: "../image"
});


