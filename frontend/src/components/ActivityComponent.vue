<template>
  <div class="card-container">
    <v-card elevation="16">
      <v-list-item three-line>
        <v-list-item-content>
          <div class="text-overline mb-4">{{ activity.action }}</div>
          <v-list-item-title class="text-h5 mb-1">
            {{ activity.username }}
          </v-list-item-title>
          <v-btn :href="activity.url" target="_blank">
            Check out activity!
          </v-btn>
        </v-list-item-content>

        <v-list-item-avatar size="80" color="grey"
          ><v-img :src="activity.avatar"></v-img
        ></v-list-item-avatar>
      </v-list-item>
      <v-list-item one-line>
        <v-btn align="left" @click="onBtnClick">Check user!</v-btn>
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
import { mapActions, mapGetters } from "vuex";

export default {
  name: "ActivityComponent",
  props: ["activity"],
  methods: {
    ...mapActions(["showUserDetails", "setIsFetchingUserDetails"]),
    onBtnClick() {
      let self = this;
      this.$store
        .dispatch("setIsFetchingUserDetails", true)
        .then(() => {
          self.$store.dispatch("showUserDetails", self.activity.username);
        })
        .then(() => {
          self.$store.dispatch("setIsFetchingUserDetails", false);
        });
    },
  },
  computed: {
    ...mapGetters(["isFetchingUserDetails"]),
  },
};
</script>
