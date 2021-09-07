<template>
  <div>
    <div class="sidebar scrollbar" id="style-5">
      <p class="app-title title-custom">ORBICON</p>
      <p class="powered-by">Memgraph's activity tracker</p>
      <SearchBarComponent />
      <div v-if="activities.length">
        <p class="activities-title title-custom">LATEST ACTIVITIES</p>
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
    <transition name="fade">
      <div v-if="showUserDetails">
        <UserDetailsComponent />
      </div>
    </transition>
  </div>
</template>

<style scoped>
.sidebar {
  margin: 0;
  padding: 0;
  padding-top: 20px;
  width: 400px;
  color: #f1f1f1;
  position: fixed;
  height: 100%;
  overflow: auto;
}

.sidebar p {
  color: #555;
}

.app-title {
  font-weight: 600;
  font-size: 30px;
  margin-bottom: 0px;
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

/*
 *  STYLE 5
 */

#style-5::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  background-color: #f5f5f5;
}

#style-5::-webkit-scrollbar {
  width: 10px;
  background-color: #f5f5f5;
}

#style-5::-webkit-scrollbar-thumb {
  background-color: #0ae;
  background-image: -webkit-gradient(
    linear,
    0 0,
    0 100%,
    color-stop(0.5, rgba(255, 255, 255, 0.2)),
    color-stop(0.5, transparent),
    to(transparent)
  );
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
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
      this.$store.dispatch("getActivities");
      this.$store.dispatch("getUsernames");
      this.$store.dispatch("getMemberGraph");
    } catch (error) {
      console.log(error);
    }

    let self = this;
    window.setInterval(() => {
      self.$store.dispatch("getActivities");
    }, 15000);
  },
  methods: {
    onDoubleClick(event) {
      if (event.nodes.length !== 1) {
        return;
      }
      const nodeId = event.nodes[0];
      const networkNodes = this.$refs.network.getNode();
      const selectedNode = networkNodes.filter((x) => x.id === nodeId)[0];
      const username = selectedNode.label;
      this.$store.dispatch("showUserDetails", username);
    },
  },
};
</script>
