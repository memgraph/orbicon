<template>
  <div class="toolbar-block">
    <v-hover v-slot="{ hover }">
      <v-toolbar
        :elevation="hover ? 16 : 2"
        class="toolbar"
        @click="onSuggestionClicked"
      >
        <p>{{ username }}</p>
      </v-toolbar>
    </v-hover>
  </div>
</template>

<style scoped>
.toolbar {
  display: flex;
  justify-content: center;
  align-content: center;
  align-items: center;
  margin-bottom: 3px;
}

p {
  font-weight: 300;
  font-size: 20px;
}
</style>


<script>
export default {
  name: "SuggestionItemComponent",
  props: ["username"],
  methods: {
    onSuggestionClicked() {
      this.$emit("suggestionClicked", this.username);
    },
  },
};
</script>
