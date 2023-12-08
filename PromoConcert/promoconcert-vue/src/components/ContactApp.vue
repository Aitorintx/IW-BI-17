<template>
  <div>
    <h2>Listado de interpretes</h2>
    <div class="interpretes-grid" v-if="lista_interpretes.length > 0">
      <div v-for="inte in lista_interpretes" class="interpretes-item">
        <router-link :to="'/interpretes/' + inte.idInterprete">{{ inte.nameInterprete}}</router-link>
      </div>
      <div>
        <router-link to="/formularioInterprete/">Añadir intérprete</router-link>
      </div>
    </div>

    <p v-else>No hay cantantes/grupos.</p>
    <div>
      <router-link to="/formularioInterprete/">Añadir intérprete</router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      lista_interpretes: [
        { idInterprete: 1, nameInterprete: 'Interprete 1' },
        { idInterprete: 2, nameInterprete: 'Interprete 2' },
        // Agrega más interpretes según sea necesario
      ],
    };
  },
  // Resto de la configuración de tu componente
};
</script>

<style scoped>
/* Estilos específicos para este componente si es necesario */
</style>
