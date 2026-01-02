export default [
    {
        files: ["**/*.js"],
        languageOptions: {
            ecmaVersion: "latest",
            sourceType: "script",
            globals: {
                // Browser globals
                window: "readonly",
                document: "readonly",
                console: "readonly",
                fetch: "readonly",
                localStorage: "readonly",
                sessionStorage: "readonly",
                navigator: "readonly",
                location: "readonly",
                history: "readonly",
                alert: "readonly",
                confirm: "readonly",
                prompt: "readonly",
                setTimeout: "readonly",
                clearTimeout: "readonly",
                setInterval: "readonly",
                clearInterval: "readonly",
                // Browser APIs
                FormData: "readonly",
                XMLHttpRequest: "readonly",
                URL: "readonly",
                URLSearchParams: "readonly",
                // External libraries
                Stripe: "readonly",
                bootstrap: "readonly",
                // defined in other scripts
                updateWishlistCount: "readonly",
                // Django template variables (injected into JS context)
                stripePublicKey: "readonly",
                clientSecret: "readonly"
            }
        },
        rules: {
            // Code quality rules
            "no-unused-vars": ["warn", { 
                "argsIgnorePattern": "^_",
                "varsIgnorePattern": "^(updateCartItem)$" // Allow updateCartItem to be unused
            }],
            "no-undef": "error",
            "no-console": "off", // Allow console for debugging in static JS
            "no-debugger": "error",
            
            // Best practices
            "eqeqeq": "error",
            "no-eval": "error",
            "no-implied-eval": "error",
            "no-new-func": "error",
            "prefer-const": "warn",
            "no-var": "warn",
            
            // Style rules
            "indent": ["error", 4],
            "quotes": ["error", "single", { "allowTemplateLiterals": true }],
            "semi": ["error", "always"],
            "comma-dangle": ["error", "never"],
            "no-trailing-spaces": "error",
            
            // Additional helpful rules
            "no-unused-expressions": "error",
            "no-unreachable": "error",
            "no-duplicate-case": "error",
            "no-empty": "warn",
            "consistent-return": "warn"
        }
    },
    {
        // Specific overrides for static JS files
        files: ["static/**/*.js"],
        rules: {
            "no-console": "off", // Allow console.log in static files for debugging
            "no-unused-vars": ["warn", { 
                "varsIgnorePattern": "^(updateCartItem|addToCart|showToast|copyKey)$", // Allow functions exposed to window/HTML
                "argsIgnorePattern": "^_" // Allow unused parameters prefixed with underscore
            }]
        }
    }
];