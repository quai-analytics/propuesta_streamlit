/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        quai: {
          navy: "#061729",
          blue: "#0E3D91",
          teal: "#19B3B8",
          sand: "#F6E7D8"
        }
      }
    }
  },
  plugins: []
};


