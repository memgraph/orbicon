<template>
  <div class="user-details">
    <v-card
      v-if="userDetails !== null && userDetails.username !== undefined"
      class="user-card"
      elevation="2"
    >
      <v-list-item three-line>
        <v-list-item-avatar size="80" color="grey"
          ><v-img :src="userDetails.avatar"></v-img
        ></v-list-item-avatar>
        <v-list-item-content>
          <v-card-title class="title-custom text-h5">{{
            userDetails.username
          }}</v-card-title>
        </v-list-item-content>
        <v-btn text class="x-btn" @click="onXClick"
          ><v-icon>mdi-close</v-icon></v-btn
        >
      </v-list-item>
      <v-list class="transparent">
        <v-list-item>
          <v-list-item-title align="left">
            <v-icon>mdi-format-letter-starts-with</v-icon> Name
          </v-list-item-title>
          <v-list-item-subtitle>{{ userDetails.name }}</v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title align="left"
            ><v-icon>mdi-domain</v-icon> Company</v-list-item-title
          >
          <v-list-item-subtitle
            >{{ userDetails.company }}
          </v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title align="left"
            ><v-icon>mdi-handshake-outline</v-icon> Hireable</v-list-item-title
          >
          <v-list-item-subtitle>
            
            <v-icon class="success--text" v-if="userDetails.hireable">mdi-thumb-up</v-icon>
            <v-icon class="danger--text" v-else>mdi-thumb-down</v-icon>
          </v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title align="left"
            ><v-icon>mdi-crosshairs-gps</v-icon> Location</v-list-item-title
          >
          <v-list-item-subtitle
            >{{ userDetails.location }}
          </v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title align="left"
            ><v-icon>mdi-cards-heart</v-icon> Memgraph Love</v-list-item-title
          >
          <v-list-item-subtitle>{{ userDetails.love }} </v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title align="left"
            ><v-icon>mdi-star</v-icon> PageRank Score</v-list-item-title
          >
          <v-list-item-subtitle
            >{{ userDetails.importance }}/100
          </v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title align="left"
            ><v-icon>mdi-github</v-icon> Github</v-list-item-title
          >
          <v-list-item-subtitle>
            <a
              class="link-to-social-network"
              v-if="userDetails.githubAccount !== null"
              :href="userDetails.githubAccount"
              target="_blank"
            >
              <span
                >Go to Github
                <v-icon class="arrow-icon">mdi-chevron-right</v-icon></span
              >
            </a>
            <div v-else>Unknown</div>
          </v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title align="left"
            ><v-icon class="arrow-icon">mdi-twitter</v-icon>
            Twitter</v-list-item-title
          >
          <v-list-item-subtitle>
            <a
              class="link-to-social-network"
              v-if="userDetails.twitterAccount !== null"
              :href="userDetails.twitterAccount"
              target="_blank"
            >
              <span>Go to Twitter <v-icon>mdi-chevron-right</v-icon></span>
            </a>
            <div v-else>Unknown</div>
          </v-list-item-subtitle>
        </v-list-item>
      </v-list>
    </v-card>
    <v-card v-else-if="!isFetchingUserDetails" class="user-card">
      <v-list-item three-line>
        <v-list-item-title
          ><v-icon>mdi-alert</v-icon>
          Username not found!
        </v-list-item-title>
        <v-btn text class="x-btn" @click="onXClick">X</v-btn>
      </v-list-item>
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
  width: 400px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  opacity: 1;
  padding: 10px;
  position: relative;
}

.v-sheet.v-card {
  border-radius: 10px;
}

.x-btn {
  position: absolute;
  top: 0px;
  right: 0px;
}

.link-to-social-network {
  text-decoration: none;
}

.arrow-icon {
  position: relative;
  top: -2px;
}

a,
a * {
  color: var(--v-danger-base) !important;
}

a:hover,
a:hover * {
  color: var(--v-dangerHover-base) !important;
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
    ...mapGetters(["showUserDetails", "userDetails", "isFetchingUserDetails"]),
  },
};
</script>
