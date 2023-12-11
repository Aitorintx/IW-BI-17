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
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('promotorInfo').innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", promotorId, true);
    xhttp.send();
}