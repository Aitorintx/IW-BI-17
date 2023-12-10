<template>
  <div class="add-contact-container" itemscope itemtype="http://schema.org/Person">
    <h1>Add Contact</h1>
    <form @submit.prevent="addContact" class="add-contact-form">
      <label for="inputName" itemprop="name">Name: </label>
      <input v-model="name" id="inputName" required />
      <label for="inputEmail" itemprop="email">Email: </label>
      <input v-model="email" type="email" id="inputEmail" required />
      <label for="inputPhone" itemprop="telephone">Phone: </label>
      <input v-model="phone" id="inputPhone" required />
      <button type="submit" class="add-button">Add Contact</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: "",
      email: "",
      phone: "",
    };
  },
  methods: {
    addContact() {
      const newContact = {
        name: this.name,
        email: this.email,
        phone: this.phone,
      };
      this.$store.dispatch("addContact", newContact);
      this.clearForm();
    },
    clearForm() {
      this.name = "";
      this.email = "";
      this.phone = "";
    },
  },
};
</script>

<style scoped>
.add-contact-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f8f8f8;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.add-contact-form {
  display: flex;
  flex-direction: column;
  margin-top: 20px;
}

label {
  margin-bottom: 8px;
}

input {
  padding: 8px;
  margin-bottom: 16px;
}

.add-button {
  background-color: #4caf50;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.add-button:hover {
  background-color: #45a049;
}
</style>
