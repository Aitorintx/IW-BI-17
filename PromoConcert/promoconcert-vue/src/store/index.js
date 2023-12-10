// store/index.js
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    contacts: []
  },
  getters: {
    getContacts: state => state.contacts
  },
  mutations: {
    ADD_CONTACT(state, contact) {
      state.contacts.push(contact);
    },
    DELETE_CONTACT(state, index) {
      state.contacts.splice(index, 1);
    }
  },
  actions: {
    addContact({ commit }, contact) {
      commit('ADD_CONTACT', contact);
    },
    deleteContact({ commit }, index) {
      commit('DELETE_CONTACT', index);
    }
  }
})
