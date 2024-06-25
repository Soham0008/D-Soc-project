const togglePassword = document.querySelector('.toggle-password');
const passwordInput = document.querySelector('.password-input');

togglePassword.addEventListener('click', function () {
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);
    }
);