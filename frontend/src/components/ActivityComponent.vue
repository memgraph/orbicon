<template>
  <div class="card-container">
    <v-card elevation="15">
      <v-list-item three-line>
        <v-list-item-content>
          <div class="text-overline mb-4">
            <v-list-item-subtitle align="left">
              {{ activity.action }}
            </v-list-item-subtitle>
          </div>
          <v-list-item-subtitle
            class="blacky--text title text-h5 mb-1"
            align="left"
          >
            {{ activity.username }}
          </v-list-item-subtitle>
          <v-list-item-subtitle class="card-date" align="left">
            {{ dateFormatted }}
          </v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-avatar size="50" color="grey"
          ><v-img :src="activity.avatar"></v-img
        ></v-list-item-avatar>
      </v-list-item>
      <v-list-item class="btn-list-item">
        <a @click="onBtnClick" align="left"
          ><span>Check user </span><v-icon>mdi-chevron-right</v-icon></a
        >
        <a
          class="check-activity-link"
          align="right"
          :href="activity.url"
          target="_blank"
          ><span>Check activity <v-icon>mdi-chevron-right</v-icon></span></a
        >
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

.v-sheet.v-card {
  border-radius: 8px;
}

.check-activity-link {
  text-decoration: none;
}

a,
a * {
  color: var(--v-danger-base) !important;
}

a:hover,
a:hover * {
  color: var(--v-dangerHover-base) !important;
}

a >>> * {
  font-size: 20px;
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
