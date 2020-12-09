module.exports = {
  env: {
    browser: true,
    es2021: true
  },
  extends: [],
  plugins: [
    'myproject',
  ],
  parserOptions: {
    ecmaVersion: 12,
    sourceType: 'module'
  },
  rules: {
    'myproject/no-template-literals': 2
  }
}
