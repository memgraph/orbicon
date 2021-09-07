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
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Encode+Sans&display=swap');

#app {
  font-family: Roboto !important;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.title {
  font-family: Encode-Sans !important;
}
</style>
