<template>
  <div class="card-container">
    <v-card elevation="16">
      <v-list-item three-line>
        <v-list-item-content>
          <div class="text-overline mb-4">
            <v-list-item-subtitle>
              {{ activity.action }}
            </v-list-item-subtitle>
          </div>
          <v-list-item-title class="title text-h5 mb-1">
            {{ activity.username }}
          </v-list-item-title>
          <v-card-text class="card-date">
            {{ dateFormatted }}
          </v-card-text>
        </v-list-item-content>

        <v-list-item-avatar size="80" color="grey"
          ><v-img :src="activity.avatar"></v-img
        ></v-list-item-avatar>
      </v-list-item>
      <v-list-item class="btn-list-item">
        <v-btn align="left" @click="onBtnClick">Check user</v-btn>
        <v-btn align="right" :href="activity.url" target="_blank">
          Check activity
        </v-btn>
      </v-list-item>
    </v-card>
  </div>
</template>

<style scoped>
.card-container {
  margin-bottom: 15px;
  margin-left: 10px;
  margin-right: 10px;
}

.btn-list-item {
  display: flex;
  justify-content: space-between;
}

.card-date {
  font-weight: 500;
  font-size: 16px;
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
    dateFormatted() {
      const date = this.activity.date;
      const lastDotIndex = date.lastIndexOf(".");
      const noMilisecondDate = date.substring(0, lastDotIndex);
      const formattedTimeDate = noMilisecondDate
        .replace("T", " @ ")
        .replaceAll("-", "/");
      return formattedTimeDate;
    },
  },
};
</script>
