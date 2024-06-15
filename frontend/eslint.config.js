const reactPlugin = require('eslint-plugin-react');
const typescriptEslintParser = require('@typescript-eslint/parser');
const typescriptEslintPlugin = require('@typescript-eslint/eslint-plugin');

module.exports = [
  {
    ignores: ['node_modules/**'], // Ignore node_modules
  },
  {
    files: ['**/*.{js,jsx,ts,tsx}'], // Apply to JavaScript and TypeScript files
    languageOptions: {
      ecmaVersion: 2021, // Use ECMAScript 2021
      sourceType: 'module', // Use ES modules
      parserOptions: {
        ecmaFeatures: {
          jsx: true, // Enable JSX
        },
      },
      globals: {
        window: 'readonly',
        document: 'readonly',
        navigator: 'readonly',
        console: 'readonly',
        module: 'writable',
        require: 'readonly',
      },
    },
    plugins: {
      react: reactPlugin,
    },
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
    files: ['*.ts', '*.tsx'], // Apply to TypeScript files
    languageOptions: {
      parser: typescriptEslintParser, // Use TypeScript parser
    },
    plugins: {
      '@typescript-eslint': typescriptEslintPlugin,
    },
    rules: {
      // Add TypeScript specific rules here
    },
  },
];
