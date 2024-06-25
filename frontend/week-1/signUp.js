        const togglePasswords = document.querySelectorAll('.toggle-password');
        const passwordInputs = document.querySelectorAll('.password-input');

        togglePasswords.forEach((togglePassword, index) => {
            togglePassword.addEventListener('click', function () {
                const type = passwordInputs[index].getAttribute('type') === 'password' ? 'text' : 'password';
                passwordInputs[index].setAttribute('type', type);
                }
            );
        }
    );