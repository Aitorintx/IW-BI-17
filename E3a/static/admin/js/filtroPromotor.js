document.getElementById('promotorDropdown').addEventListener('change', function() {
    var selectedPromotorId = this.value;
    if (selectedPromotorId) {
        loadPromotorDetails(selectedPromotorId);
    } else {
        document.getElementById('promotorInfo').innerHTML = '';
    }
});

function loadPromotorDetails(promotorId) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                document.getElementById('promotorInfo').innerHTML = this.responseText;
            } else {
                console.error("Error al cargar los detalles del promotor");
            }
        }
    };
    xhttp.open("GET", `/promotores/${promotorId}/`, true); // Ajusta la URL según tu estructura de ruta en Django
    xhttp.send();
}