<template>
  <div>
    <div class="sidebar-search">
      <v-toolbar dense floating>
        <v-text-field
          hide-details
          prepend-icon="mdi-magnify"
          single-line
        ></v-text-field>
      </v-toolbar>
    </div>
  </div>
</template>

<style scoped>
.sidebar-search {
  margin-top: 10px;
  margin-bottom: 50px;
}
</style>

<script>
export default {
  name: "SearchBarComponent",
  components: {},
};
</script>
