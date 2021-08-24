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
import { fetchNetwork, fetchNodes, fetchLinks } from "@/api/apiClient";
import { Network } from "vue-vis-network";

export default {
  name: "NetworkComponent",
  components: {
    Network
  },
  data: function () {
    return {
      msg: "Loading...",
      nodes: [],
      links: [],
      options: {
        height: "1000px",
        width: "1000px"
      },
    };
  },
  async created() {
    try {
      this.msg = await fetchNetwork();
      this.nodes = await fetchNodes();
      this.links = await fetchLinks();
    } catch (error) {
      this.msg = "Server error :(";
    }
  },
};
</script>
