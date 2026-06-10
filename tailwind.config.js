module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        accent: '#5E5CE6',
        emerald: {
          950: '#064e3b',
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        'instrument-serif': ['Instrument Serif', 'serif'],
      },
    },
  },
  plugins: [],
}
