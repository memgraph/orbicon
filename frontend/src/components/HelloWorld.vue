<template>
  <div class="hello">
    <p>{{ msg }}</p>
  </div>
</template>

<style scoped></style>

<script>
import { fetchMessage } from "@/api/apiClient";

export default {
  name: "HelloWorld",
  data: function () {
    return {
      msg: "Loading...",
    };
  },
  async created() {
    try {
      this.msg = await fetchMessage();
    } catch (error) {
      this.msg = "Server error :(";
    }
  },
};
</script>
