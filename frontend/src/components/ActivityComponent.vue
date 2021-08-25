<template>
  <div class="card-container">
    <v-card elevation="16">
      <v-card-title>
        {{ activity.username }}
      </v-card-title>
      <v-card-subtitle align="left">
        {{ activity.action }}
      </v-card-subtitle>
      <v-card-text>
        {{ activity.description }}
      </v-card-text>
      <v-card-text align="right">
        {{ activity.date }}
      </v-card-text>
    </v-card>
  </div>
</template>

<style scoped>
.card-container {
  margin-bottom: 10px;
  margin-left: 10px;
  margin-right: 10px;
}
</style>


<script>
export default {
  name: "ActivityComponent",
  props: ["activity"],
};
</script>
