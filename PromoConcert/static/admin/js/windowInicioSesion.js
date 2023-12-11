function showConfirmation() {
    var username = document.getElementById('usernameField').value;

    // Display confirmation message in a new window
    var confirmationMessage = `Buenas ${username}, has iniciado sesión!`;
    var win = window.open("", "ConfirmationWindow", "width=400, height=200");
    win.document.body.innerHTML = `<h1>${confirmationMessage}</h1>`;
    
    // Submit the form after showing the confirmation
    document.getElementById('loginForm').submit();
}