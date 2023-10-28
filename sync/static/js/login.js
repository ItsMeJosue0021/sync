function togglePassword(inputId) {
    const inputField = document.getElementById(inputId);
    const btn = document.getElementById('showPassword');
    if (inputField.type === "password") {
        inputField.type = "text";
        btn.textContent = "Hide";
        
    } else {
        inputField.type = "password";
        btn.textContent = "Show";
    }
}