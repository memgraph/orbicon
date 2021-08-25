<template>
  <div class="hello">
    <p>{{ msg }}</p>
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
    ...mapGetters(["memberGraph"]),
  },
  mounted() {
    try {
      this.$store.dispatch("getMemberGraph");
    } catch (error) {
      this.msg = "Server error :(";
    }
  },
};
</script>
