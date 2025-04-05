const globals = require("globals");
const pluginJs = require("@eslint/js");

module.exports = [
  {
    ignores: [
        "**/.venv/**",
        "**/venv/**",
        "**/node_modules/**",
    ]
  },
  {
    files: ["*.js"], // Only look at JavaScript files in the root directory
    languageOptions: {
      sourceType: "commonjs",
      globals: {
        ...globals.node, // Enable Node.js globals like __dirname and __filename
      }
    },
  },
  {
    languageOptions: {
      globals: globals.browser, // Set browser globals
    }
  },
  pluginJs.configs.recommended, // Use ESLint's recommended config
];