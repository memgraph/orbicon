<template>
  <div class="hello">
    <p>{{ msg }}</p>
    <p>{{ usernames }}</p>
    <p>{{ userDetails.firstName }}</p>
    <p>{{ activities[1].username }}</p>
    <network
      ref="network"
      :nodes="memberGraph.nodes"
      :edges="memberGraph.edges"
      :options="options"
    ></network>
  </div>
</template>


<script>
import { Network } from "vue-vis-network";
import { mapGetters } from "vuex";

export default {
  name: "NetworkComponent",
  components: {
    Network,
  },
  data: function () {
    return {
      msg: "All good!",
      options: {
        height: "1000px",
        width: "1000px",
      },
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
