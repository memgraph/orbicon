<template>
  <div>
    <div class="sidebar">
      <SearchBarComponent />
      <div v-if="activities.length">
        <p class="activities-title">ACTIVITIES</p>
        <ActivityComponent
          v-for="(activity, i) in activities"
          :key="i"
          :activity="activity"
        />
      </div>
      <div v-else>
        <v-progress-circular
          :size="50"
          color="primary"
          indeterminate
        ></v-progress-circular>
        <p class="loading-bar-text">Loading activities...</p>
      </div>
    </div>
    <div class="network-bar">
      <network
        v-if="memberGraph.nodes.length"
        class="wrapper"
        ref="network"
        :nodes="memberGraph.nodes"
        :edges="memberGraph.edges"
        :options="options"
        @double-click="onDoubleClick($event)"
      ></network>
      <div class="loading-container" v-else>
        <div class="loading-bar">
          <v-progress-circular
            :size="200"
            color="primary"
            indeterminate
          ></v-progress-circular>
          <p class="loading-bar-text big-text">Loading member graph...</p>
        </div>
      </div>
    </div>
    <div v-if="showUserDetails">
      <UserDetailsComponent />
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

.loading-container {
  position: absolute;
  left: 400px;
  top: 0px;
  bottom: 0px;
  right: 0px;
}

.loading-bar {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.loading-bar-text {
  margin-top: 20px;
}

.big-text {
  font-weight: 500;
  font-size: 30px;
}
</style>

<script>
import { Network } from "vue-vis-network";
import { mapGetters } from "vuex";
import SearchBarComponent from "./SearchBarComponent";
import ActivityComponent from "./ActivityComponent";
import UserDetailsComponent from "./UserDetailsComponent";

export default {
  name: "NetworkComponent",
  components: {
    Network,
    SearchBarComponent,
    ActivityComponent,
    UserDetailsComponent,
  },
  data: function () {
    return {
      msg: "All good!",
      options: {},
    };
  },
  computed: {
    ...mapGetters([
      "memberGraph",
      "usernames",
      "userDetails",
      "activities",
      "showUserDetails",
    ]),
  },
  mounted() {
    try {
      this.$store.dispatch("getMemberGraph");
      this.$store.dispatch("getUsernames");
      this.$store.dispatch("getActivities");
    } catch (error) {
      this.msg = "Server error :(";
      console.log(error);
    }
  },
  methods: {
    onDoubleClick(event) {
      if (event.nodes.length !== 1) {
        return;
      }
      const nodeId = event.nodes[0];
      console.log(nodeId);
      this.$store.dispatch("showUserDetails");
    },
  },
};
</script>
