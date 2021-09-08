<template>
  <v-card>
    <p class="title-custom">Communities</p>
    <div v-for="(legendPart, idx) in legend" :key="idx">
      <div class="color-section">
        <div class="color-box" :style="{'background-color': legendPart.color}"></div>
        <div class="community-field">{{legendPart.community}}</div>
      </div>
    </div>
  </v-card>
</template>


<style scoped>
.v-card {
  padding: 10px !important;
}

.color-section {
  display: flex;
  justify-content: space-between;
  margin-top: 5px;
  margin-bottom: 5px;
}

.color-box {
  width: 20px;
  height: 20px;
  border-radius: 10px;
  border: 1px solid black;
}

.community-field {
  margin-left: 20px;
}

p {
  text-align: left;
  font-size: 20px;
  font-weight: 400;
  color: var(--v-danger-base);
}
</style>


<script>
import { mapGetters } from "vuex";

export default {
  name: "LegendComponent",
  mounted() {
    this.$store.dispatch("getLegend");
  },
  computed: {
    ...mapGetters(["legend"]),
  },
};
</script>
