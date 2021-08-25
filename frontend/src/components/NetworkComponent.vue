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
  </div>
</template>

<style scoped>
.sidebar {
  margin: 0;
  padding: 0;
  width: 400px;
  background-color: #f1f1f1;
  position: fixed;
  height: 100%;
  overflow: auto;
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
    ...mapGetters(["memberGraph", "usernames", "userDetails", "activities"]),
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
};
</script>
