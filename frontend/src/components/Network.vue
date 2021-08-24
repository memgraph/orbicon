<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<style scoped></style>

<script>
import { fetchNetwork } from "@/api/apiClient";

export default {
  name: "Network",
  data: function () {
    return {
      msg: "Loading...",
    };
  },
  async created() {
    try {
      this.msg = await fetchNetwork();
    } catch (error) {
      this.msg = "Server error :(";
    }
  },
};
</script>
