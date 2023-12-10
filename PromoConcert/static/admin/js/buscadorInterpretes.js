document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("filtroInterpretes").addEventListener("input", function() {
        var filtro = this.value.toLowerCase();
        var interpretes = document.getElementsByClassName("interprete-item");

        for (var i = 0; i < interpretes.length; i++) {
            var nombreInterprete = interpretes[i].querySelector("span[itemprop='name']").innerText.toLowerCase();
            var urlInterprete = interpretes[i].querySelector("a").getAttribute("href");

            if (nombreInterprete.indexOf(filtro) > -1) {
                    interpretes[i].style.display = "";
            } else {
                    interpretes[i].style.display = "none";
            }
        }
    });
});
