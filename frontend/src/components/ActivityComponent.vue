<template>
  <div>
    {{ activity.username }}
  </div>
</template>

<style scoped>
</style>


<script>
export default {
  name: "ActivityComponent",
  props: ["activity"],
};
</script>
