// /** @type {import('tailwindcss').Config} */
// export default {
//   content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
//   theme: {
//     darkmode: "class",
//     extend: {
//       fontFamily: {
//         inter: ["Inter", "serif"],
//       },
//     },
//   },
//   plugins: [],
// };

const withMT = require("@material-tailwind/react/utils/withMT");

module.exports = withMT({
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    darkmode: "class",
    extend: {
      fontFamily: {
        inter: ["Inter", "serif"],
      },
    },
  },
  plugins: [],
});
