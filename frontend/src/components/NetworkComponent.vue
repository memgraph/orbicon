<template>
  <div>
    <div class="lightGrey sidebar scrollbar" id="style-5">
      <div class="title-images">
        <img
          src="https://assets-global.website-files.com/6090f2cbfb550680d4288567/60916d2d77cab34ad9d7666f_Logo.svg"
          width="88px"
          height="34px"
          loading="lazy"
          alt=""
        />
        <img
          src="https://uploads-ssl.webflow.com/5e7ceb09657a69bdab054b3a/5e7ceb09657a6937ab054bba_Black_Original%20_Logo.png"
          width="88px"
          height="34px"
          alt=""
          class="nav-logo"
        />
      </div>
      <p class="app-title title-custom danger--text">ORBICON</p>

      <p class="powered-by danger--text">Your DEV community tracker</p>
      <SearchBarComponent />
      <div v-if="activities.length">
        <p class="activities-title title-custom danger--text">
          LATEST ACTIVITIES
        </p>
        <ActivityComponent
          v-for="(activity, i) in activities"
          :key="i"
          :activity="activity"
        />
      </div>
      <div v-else>
        <v-progress-circular
          color="danger"
          :size="50"
          indeterminate
        ></v-progress-circular>
        <p class="loading-bar-text">Loading activities...</p>
      </div>
    </div>
    <div class="network-bar">
      <div class="memgraph-background-image"></div>
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
            color="dangerHover"
            indeterminate
          ></v-progress-circular>
          <p class="loading-bar-text big-text">{{ dynamicalLoadingMessage }}</p>
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
  width: 350px;
  position: fixed;
  height: 100%;
  overflow: auto;
}

.title-images {
  display: flex;
  justify-content: space-around;
  margin-bottom: 10px;
}

.ampersand {
  font-size: 20px;
  font-weight: 700;
}

.app-title {
  font-weight: 600;
  font-size: 30px;
  margin-bottom: 0px;
  letter-spacing: 2px;
}

.network-bar {
  margin-left: 351px;
  padding: 1px 16px;
  position: relative;
}

.memgraph-background-image {
  position: absolute;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
  background-image: linear-gradient(
    45deg,
    #ff0092,
    #df2000 17%,
    #ffc500 100%,
    #fff 0,
    #fff
  );
  opacity: 0.6;
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
  left: 350px;
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
  background-color: var(--v-blue-base);
  background-image: linear-gradient(
    45deg,
    #ff0092,
    #df2000 17%,
    #ffc500 100%,
    #fff 0,
    #fff
  );
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}

.vis-tooltip {
  background-color: var(--v-blue-base) !important;
  color: var(--v-blue-base) !important;
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
      loadingMessage: "Loading member graph",
      loadingStep: 0,
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
    dynamicalLoadingMessage() {
      let currentStep = this.loadingStep;
      const dots = ".".repeat(currentStep);
      return `${this.loadingMessage}${dots}`;
    },
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
  created() {
    let self = this;
    window.setInterval(() => {
      self.computeMessage();
    }, 500);
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
    computeMessage() {
      this.loadingStep = (this.loadingStep + 1) % 4;
    },
  },
};
</script>
