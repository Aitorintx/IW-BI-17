function showNotification() {
    alert('Nuevo Festival Registrado!');
}

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("bttn").addEventListener("click", function() {
        showNotification();
    });
});