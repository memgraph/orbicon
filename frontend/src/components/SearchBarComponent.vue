<template>
  <div>
    <div class="sidebar-search">
      <v-toolbar dense floating>
        <v-text-field
          v-model="usernameInput"
          placeholder="Search for contributors"
          hide-details
          prepend-icon="mdi-magnify"
          single-line
          @keyup="search($event)"
          @keyup.enter.native="onEnterClicked"
          @focus="onFocus"
        ></v-text-field>
      </v-toolbar>
      <div v-if="showSuggestions" class="suggestions">
        <SuggestionItemComponent
          v-for="(username, i) in usernames"
          :key="i"
          :username="username"
          @suggestionClicked="updateSearchBarWithSuggestion"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.sidebar-search {
  margin-bottom: 10px;
  position: relative;
}
.suggestions {
  display: block;
  z-index: 2;
  position: absolute;
  top: 55px;
  left: 1.5rem;
  right: 1.5rem;
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
      showSuggestions: false,
      timeout: null,
    };
  },
  methods: {
    ...mapActions(["showUserDetails", "getUsernamesWithPrefix"]),
    onEnterClicked() {
      if (this.usernameInput.length === 0) {
        return;
      }

      let self = this;
      this.$store
        .dispatch("setIsFetchingUserDetails", true)
        .then(() => {
          self.$store.dispatch("showUserDetails", self.usernameInput);
        })
        .then(() => {
          self.$store.dispatch("setIsFetchingUserDetails", false);
        });
    },
    updateSearchBarWithSuggestion(value) {
      console.log(value);
      this.usernameInput = value;
      this.showSuggestions = false;
    },
    search(event) {
      if (event.keyCode === 13) {
        return;
      }
      if (this.usernameInput.length === 0) {
        this.showSuggestions = false;
        return;
      }

      this.showSuggestions = true;

      clearTimeout(this.timeout);
      var self = this;
      this.timeout = setTimeout(function () {
        self.$store.dispatch("getUsernamesWithPrefix", self.usernameInput);
      }, 500);
    },
    onFocus() {
      if (this.usernameInput.length) {
        this.showSuggestions = true;
      }
    },
  },
  computed: {
    ...mapGetters(["usernames"]),
  },
};
</script>

