<template>
  <div>
    <div class="sidebar">
      <SearchBarComponent />
      <p class="activities-title">ACTIVITIES</p>
      <ActivityComponent
        v-for="(activity, i) in activities"
        :key="i"
        :activity="activity"
      />
    </div>
    <div class="network-bar">
      <network
        class="wrapper"
        ref="network"
        :nodes="memberGraph.nodes"
        :edges="memberGraph.edges"
        :options="options"
      ></network>
    </div>
    <div v-if="showUserDetails" class="user-details">
      <v-card class="user-card" elevation="2">
        <v-card-text>Hello</v-card-text>
        <v-btn @click="onXClick">X</v-btn>
      </v-card>
    </div>
  </div>
</template>

<style scoped>
.sidebar {
  margin: 0;
  padding: 0;
  width: 400px;
  color: #f1f1f1;
  position: fixed;
  height: 100%;
  overflow: auto;
}

.sidebar p {
  color: #555;
}

.network-bar {
  margin-left: 400px;
  padding: 1px 16px;
}

.wrapper {
  min-height: 100vh;
  padding: 10px;
  height: 100vh;
}

.activities-title {
  font-weight: 700;
  font-size: 20px;
}

.user-details {
  position: absolute;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
  background-color: rgba(22, 22, 22, 0.8);
}

.user-card {
  width: 500px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  opacity: 1;
}
</style>

<script>
import { Network } from "vue-vis-network";
import { mapGetters } from "vuex";
import SearchBarComponent from "./SearchBarComponent";
import ActivityComponent from "./ActivityComponent";

export default {
  name: "NetworkComponent",
  components: {
    Network,
    SearchBarComponent,
    ActivityComponent,
  },
  data: function () {
    return {
      msg: "All good!",
      options: {},
    };
  },
  computed: {
    ...mapGetters(["memberGraph", "usernames", "userDetails", "activities", "showUserDetails"]),
  },
  mounted() {
    try {
      this.$store.dispatch("getMemberGraph");
      this.$store.dispatch("getUsernames");
      this.$store.dispatch("getUserDetails");
      this.$store.dispatch("getActivities");
    } catch (error) {
      this.msg = "Server error :(";
      console.log(error);
    }
  },
  methods: {
    onXClick() {
      this.$store.dispatch("disposeUserDetails");
    }
  }
};
</script>
