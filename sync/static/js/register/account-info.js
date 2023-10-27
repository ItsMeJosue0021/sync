function checkPasswordMatch() {
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;
    const errorSpan = document.querySelector(".error");
    
    if (password !== confirmPassword) {
        errorSpan.style.display = "block";
        document.getElementById("confirmPassword").style.border = "1px solid red";
        errorSpan.textContent = "Passwords do not match";
    } else {
        errorSpan.style.display = "none";
        document.getElementById("confirmPassword").style.border = "1px solid #ced4da";
        document.querySelector("form").submit();
    }
}

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

function toggleConfirmPassword(inputId) {
    const inputField = document.getElementById(inputId);
    const btn = document.getElementById('showConfirmPassword');
    if (inputField.type === "password") {
        inputField.type = "text";
        btn.textContent = "Hide";
    } else {
        inputField.type = "password";
        btn.textContent = "Show";
    }
}