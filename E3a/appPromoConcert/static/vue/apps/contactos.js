// en static/tu_app/vue/apps/contactos.js
new Vue({
    el: '#app',
    data: {
        contactos: ["Mikel","kile@opendeusto.es","7876989786"],
        nuevoContacto: {
            nombre: '',
            email: '',
            telefono: ''
        }
    },
    created() {
        this.obtenerContactos();
    },
    methods: {
        obtenerContactos() {
            // Hacer una petición AJAX para obtener los contactos desde el servidor
            axios.get('/contactos/')  // Ajusta la URL según tu configuración de Django
                .then(response => {
                    this.contactos = response.data;
                })
                .catch(error => {
                    console.error('Error al obtener contactos:', error);
                });
        },
        eliminarContacto(id) {
            // Hacer una petición AJAX para eliminar el contacto con el ID proporcionado
            axios.delete(`/eliminar_contacto/${id}/`)  // Ajusta la URL según tu configuración de Django
                .then(response => {
                    console.log(response.data.message);
                    this.obtenerContactos();  // Actualizar la lista después de eliminar
                })
                .catch(error => {
                    console.error('Error al eliminar contacto:', error);
                });
        },
        crearContacto() {
            const formData = new FormData();
            formData.append('nombre', this.nuevoContacto.nombre);
            formData.append('email', this.nuevoContacto.email);
            formData.append('telefono', this.nuevoContacto.telefono);
        
            axios.post('/crear_contacto/', formData)
                .then(response => {
                    console.log(response.data.message);
                    this.obtenerContactos();
                    this.nuevoContacto = {};
                })
                .catch(error => {
                    console.error('Error al crear contacto:', error);
                });
        }
        
    }
});
