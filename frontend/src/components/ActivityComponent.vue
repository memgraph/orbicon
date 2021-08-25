<template>
  <div class="card-container">
    <v-card elevation="16">
      <v-list-item three-line>
        <v-list-item-content>
          <div class="text-overline mb-4">{{ activity.action }}</div>
          <v-list-item-title class="text-h5 mb-1">
            {{ activity.username }}
          </v-list-item-title>
          <v-list-item-subtitle>{{
            activity.description
          }}</v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-avatar tile size="80" color="grey"
          ><v-img
            src="https://avatars.githubusercontent.com/u/4950251?s=88&v=4"
          ></v-img
        ></v-list-item-avatar>
      </v-list-item>
      <v-list-item one-line>
        <v-btn align="left">Find more!</v-btn>
        <v-card-text align="right">
          {{ activity.date }}
        </v-card-text>
      </v-list-item>
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
