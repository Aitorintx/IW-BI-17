// promoconcert-vue/src/main.js

import Vue from 'vue';
import App from './App.vue';
import router from './router'; // Importa tu configuración de router

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  router, // Agrega la configuración del router a la instancia de Vue
}).$mount('#app');
