import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import ContactList from '../components/ContactList.vue'
import AddContact from '../components/AddContact.vue'
import DeleteContact from '../components/DeleteContact.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView // Asigna el componente AboutView a la ruta '/about'
  },
  {
    path: '/contacts',
    name: 'contacts',
    component: ContactList
  },
  {
    path: '/add-contact',
    name: 'add-contact',
    component: AddContact
  },
  {
    path: '/delete-contact',
    name: 'delete-contact',
    component: DeleteContact
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
