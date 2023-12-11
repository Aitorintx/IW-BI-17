function showNotification() {
    alert('Nuevo Interprete Registrado!');
}

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("button").addEventListener("click", function() {
        showNotification();
    });
});