<template>
  <div class="user-details">
    <v-card class="user-card" elevation="2">
      <v-list-item three-line>
        <v-list-item-avatar size="80" color="grey"
          ><v-img
            src="https://avatars.githubusercontent.com/u/4950251?s=88&v=4"
          ></v-img
        ></v-list-item-avatar>
        <v-list-item-content>
          <v-card-title class="text-h5">{{
            userDetails.username
          }}</v-card-title>
        </v-list-item-content>
        <v-btn text class="x-btn" @click="onXClick">X</v-btn>
      </v-list-item>
      <v-list class="transparent">
        <v-list-item>
          <v-list-item-title>Name </v-list-item-title>
          <v-list-item-subtitle>{{ userDetails.name }}</v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title>Company</v-list-item-title>
          <v-list-item-subtitle
            >{{ userDetails.company }}
          </v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title
            >Memgraph Love<v-icon>mdi-cards-heart</v-icon></v-list-item-title
          >
          <v-list-item-subtitle>{{ userDetails.love }} </v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title>Importance</v-list-item-title>
          <v-list-item-subtitle
            >{{ userDetails.importance }}
          </v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title> Github </v-list-item-title>
          <v-list-item-subtitle>
            <v-btn :href="userDetails.githubAccount" target="_blank">
              {{ userDetails.githubUsername }}
            </v-btn>
          </v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title> Twitter </v-list-item-title>
          <v-list-item-subtitle>
            <v-btn :href="userDetails.twitterAccount" target="_blank">
              {{ userDetails.twitterUsername }}
            </v-btn>
          </v-list-item-subtitle>
        </v-list-item>
      </v-list>
    </v-card>
  </div>
</template>

<style scoped>
.user-details {
  z-index: 6;
  position: absolute;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
  background-color: rgba(22, 22, 22, 0.8);
}

.user-card {
  width: 600px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  opacity: 1;
  padding: 15px;
}

.x-btn {
  margin-top: 10px;
  margin-bottom: 10px;
}
</style>


<script>
import { mapGetters } from "vuex";
export default {
  name: "UserDetailsComponent",
  methods: {
    onXClick() {
      this.$store.dispatch("disposeUserDetails");
    },
  },
  computed: {
    ...mapGetters(["showUserDetails", "userDetails"]),
  },
};
</script>
