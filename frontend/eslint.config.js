const reactPlugin = require('eslint-plugin-react');
const typescriptEslintParser = require('@typescript-eslint/parser');
const typescriptEslintPlugin = require('@typescript-eslint/eslint-plugin');

module.exports = {
  ignorePatterns: ['node_modules/**'], // Ignore node_modules
  overrides: [
    {
      files: ['**/*.{js,jsx,ts,tsx}'], // Apply to JavaScript and TypeScript files
      parserOptions: {
        ecmaVersion: 2021, // Use ECMAScript 2021
        sourceType: 'module', // Use ES modules
        ecmaFeatures: {
          jsx: true, // Enable JSX
        },
      },
      env: {
        browser: true,
        node: true,
      },
      plugins: ['react'],
      rules: {
        'react/react-in-jsx-scope': 'off', // Disable rule that requires React to be in scope
      },
      settings: {
        react: {
          version: 'detect', // Automatically detect the React version
        },
      },
    },
    {
      files: ['**/*.ts', '**/*.tsx'], // Apply to TypeScript files
      parser: '@typescript-eslint/parser', // Use TypeScript parser
      plugins: ['@typescript-eslint'],
      extends: ['plugin:@typescript-eslint/recommended'], // Use recommended rules from the @typescript-eslint/eslint-plugin
      rules: {
        // Add TypeScript specific rules here
      },
    },
  ],
};