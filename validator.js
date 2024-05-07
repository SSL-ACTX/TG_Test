document.addEventListener('DOMContentLoaded', function() {
    const passwordInputs = document.querySelectorAll('input[type="password"]');
    passwordInputs.forEach(function(input) {
        input.addEventListener('input', function(event) {
            const password = event.target.value;
            if (password.length < 6) {
                event.target.setCustomValidity('Password must be at least 6 characters long.');
            } else {
                event.target.setCustomValidity('');
            }
        });
    });

    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const passwordInputs = document.querySelectorAll('input[type="password"]');
        passwordInputs.forEach(function(input) {
            const password = input.value;
            // Check for server-side scripting
            if (password.includes('<script>') || password.includes('<?php')) {
                event.preventDefault();
                alert('Password cannot contain server-side scripting.');
                return;
            }
            // Check for illegal characters
            const illegalCharacters = ['<', '>', '&', '"', '\''];
            for (let char of illegalCharacters) {
                if (password.includes(char)) {
                    event.preventDefault();
                    alert('Password contains illegal characters.');
                    return;
                }
            }
        });
    });
});
