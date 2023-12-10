<template>
  <div class="contact-list-container" itemscope itemtype="http://schema.org/ItemList">
    <h1>Contact List</h1>
    <ul class="contact-list" itemprop="itemListElement" itemscope itemtype="http://schema.org/Person">
      <li v-for="(contact, index) in contacts" :key="index" class="contact-item" itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem">
        <span itemprop="name">{{ contact.name }}</span> -
        <span itemprop="email">{{ contact.email }}</span> -
        <span itemprop="telephone">{{ contact.phone }}</span>
        <button @click="deleteContact(index)" class="delete-button">Delete</button>
        <meta itemprop="position" :content="index + 1" /> 
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  computed: {
    contacts() {
      return this.$store.getters.getContacts;
    },
  },
  methods: {
    deleteContact(index) {
      this.$store.dispatch("deleteContact", index);
    },
  },
};
</script>

<style scoped>
.contact-list-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.contact-list {
  list-style: none;
  padding: 0;
}

.contact-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #ddd;
}

.delete-button {
  background-color: #e74c3c;
  color: #fff;
  padding: 8px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.delete-button:hover {
  background-color: #c0392b;
}
</style>
