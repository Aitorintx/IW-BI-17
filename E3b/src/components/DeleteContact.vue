<template>
  <div class="delete-contact-container">
    <h1>Delete Contact</h1>
    <form @submit.prevent="deleteContact" class="delete-contact-form">
      <label for="selectContact">Select Contact to Delete: </label>
      <select v-model="selectedContact" id="selectContact">
        <option v-for="(contact, index) in contacts" :key="index">
          {{ contact.name }}
        </option>
      </select>
      <button type="submit" class="delete-button">Delete Contact</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedContact: null,
    };
  },
  computed: {
    contacts() {
      return this.$store.getters.getContacts;
    },
  },
  methods: {
    deleteContact() {
      const index = this.contacts.findIndex(
        (contact) => contact.name === this.selectedContact
      );
      if (index !== -1) {
        this.$store.dispatch("deleteContact", index);
        this.selectedContact = null;
      }
    },
  },
};
</script>

<style scoped>
.delete-contact-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f4f4f4;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.delete-contact-form {
  display: flex;
  flex-direction: column;
  margin-top: 20px;
}

label {
  margin-bottom: 8px;
}

select {
  padding: 8px;
  margin-bottom: 16px;
}

.delete-button {
  background-color: #ff0000;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.delete-button:hover {
  background-color: #cc0000;
}
</style>
