<template>
  <v-app>
    <NetworkComponent />
  </v-app>
</template>

<script>
import NetworkComponent from "./components/NetworkComponent.vue";

export default {
  name: "App",
  components: {
    NetworkComponent,
  },
  metaInfo: {
    title: "Orbicon",
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
