<template>
  <div>
    <div class="sidebar-search">
      <v-toolbar dense floating>
        <v-text-field
          v-model="usernameInput"
          hide-details
          prepend-icon="mdi-magnify"
          single-line
          @keyup.enter.native="onEnterClicked"
        ></v-text-field>
      </v-toolbar>
    </div>
    <div v-if="usernameInput.length !== 0" class="suggestions">
      <SuggestionItemComponent
        v-for="(username, i) in sortedUsernames"
        :key="i"
        :username="username"
        @suggestionClicked="updateSearchBarWithSuggestion"
      />
    </div>
  </div>
</template>

<style scoped>
.sidebar-search {
  margin-top: 10px;
  margin-bottom: 50px;
}
.suggestions {
  display: block;
  margin: auto;
  z-index: 2;
  position: absolute;
  top: 60px;
  left: 20px;
  width: 350px;
}
</style>
<script>
import { mapActions, mapGetters } from "vuex";
import SuggestionItemComponent from "./SuggestionItemComponent";
export default {
  name: "SearchBarComponent",
  components: {
    SuggestionItemComponent,
  },
  data: () => {
    return {
      usernameInput: "",
    };
  },
  methods: {
    ...mapActions(["showUserDetails"]),
    onEnterClicked() {
      if (this.usernameInput.length === 0) {
        return;
      }

      this.$store.dispatch("showUserDetails");
    },
    updateSearchBarWithSuggestion(value) {
      this.usernameInput = value;
    },
  },
  computed: {
    ...mapGetters(["usernames"]),
    sortedUsernames() {
      const filtered = this.usernames.filter((x) =>
        x.toLowerCase().startsWith(this.usernameInput)
      ).slice(0, 5);

      return filtered;
    },
  },
};
</script>
