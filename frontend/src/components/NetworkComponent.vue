<template>
  <div class="hello">
    <p>{{ msg }}</p>
    <network
      ref="network"
      :nodes="nodes"
      :edges="links"
      :options="options"
    ></network>
  </div>
</template>


<script>
import { Network } from "vue-vis-network";

export default {
  name: "NetworkComponent",
  components: {
    Network
  },
  data: function () {
    return {
      msg: "All good!",
      memberGraph: {},
      options: {
        height: "1000px",
        width: "1000px"
      },
    };
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
