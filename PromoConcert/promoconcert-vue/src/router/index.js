// promoconcert-vue/src/router/index.js

import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  { path: '/', component: () => import('@/views/HomePage.vue') },
  { path: '/about', component: () => import('@/views/AboutPage.vue') },
  // Agrega más rutas según sea necesario
];

const router = new VueRouter({
  routes,
});

export default router;
