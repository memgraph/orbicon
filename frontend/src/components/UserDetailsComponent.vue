<template>
  <div class="user-details">
    <v-card
      v-if="userDetails !== null && userDetails.username !== undefined"
      class="user-card"
      elevation="2"
    >
      <div class="user-card-heading">
        <v-list-item-avatar size="80" color="grey" class="avatar"
          ><v-img :src="userDetails.avatar"></v-img
        ></v-list-item-avatar>
        <div>
          <div align="left" class="title-custom text-h5 user-username">
            {{ userDetails.username }}
          </div>
          <div class="user-description">{{ userDescriptionFormatted }}</div>
        </div>
        <v-btn text class="x-btn" @click="onXClick"
          ><v-icon>mdi-close</v-icon></v-btn
        >
      </div>
      <v-divider class="divider"></v-divider>
      <v-list class="transparent">
        <v-list-item>
          <v-list-item-title align="left">
            <v-icon>mdi-format-letter-starts-with</v-icon><span>&nbsp; Name</span>
          </v-list-item-title>
          <v-list-item-subtitle>{{ userDetails.name }}</v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title align="left"
            ><v-icon>mdi-domain</v-icon><span>&nbsp; Company</span></v-list-item-title
          >
          <v-list-item-subtitle
            >{{ userDetails.company }}
          </v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title align="left"
            ><v-icon>mdi-handshake-outline</v-icon
            ><span>&nbsp; Hireable</span></v-list-item-title
          >
          <v-list-item-subtitle>
            <v-icon class="success--text" v-if="userDetails.hireable"
              >mdi-thumb-up</v-icon
            >
            <v-icon class="danger--text" v-else>mdi-thumb-down</v-icon>
          </v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title align="left"
            ><v-icon>mdi-crosshairs-gps</v-icon
            ><span>&nbsp; Location</span></v-list-item-title
          >
          <v-list-item-subtitle
            >{{ userDetails.location }}
          </v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title align="left"
            ><v-icon>mdi-cards-heart</v-icon
            ><span>&nbsp; Memgraph Love</span></v-list-item-title
          >
          <v-list-item-subtitle>{{ userDetails.love }} </v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title align="left"
            ><v-icon>mdi-star</v-icon
            ><span>&nbsp; Pagerank Score</span></v-list-item-title
          >
          <v-list-item-subtitle
            >{{ userDetails.importance }}/100
          </v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title align="left"
            ><v-icon>mdi-account-group</v-icon
            ><span>&nbsp; Community</span></v-list-item-title
          >
          <v-list-item-subtitle
            >{{ userDetails.community }}
          </v-list-item-subtitle>
        </v-list-item>
        <v-list-item>
          <v-list-item-title align="left"
            ><v-icon>mdi-github</v-icon><span>&nbsp; Github</span></v-list-item-title
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
            ><v-icon class="arrow-icon">mdi-twitter</v-icon
            ><span>&nbsp; Twitter</span></v-list-item-title
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
span {
  white-space: pre;
}

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
  width: 500px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  opacity: 1;
  padding: 10px;
  position: relative;
}

.user-card-heading {
  display: flex;
}

.avatar {
  margin-left: 5px;
}

.user-username {
  margin-top: 10px;
}

.user-description {
  color: var(--v-grey-base);
  text-align: left;
  font-size: 14px;
  margin-top: 5px;
  margin-bottom: 10px;
}

.divider {
  margin-top: 10px;
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

.v-icon {
  color: var(--v-dangerHover-base) !important
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
  data: () => {
    return {
      userDescription:
        "Hello, I'm  $name, $whatKindOf developer with a history of $projectAdjective projects. My skills include $skill1, $skill2 and $skill3. My interest is $interest1.",
      articleAdjectives: [
        "an aspiring",
        "an enthusiastic",
        "an ambitious",
        "a loveable",
        "a full-stack",
        "a frontend",
        "a backend",
      ],
      projectsAdjectives: [
        "enterprise",
        "mission critical",
        "agency",
        "student",
        "university",
        "self-learning",
      ],
      interestTopics: [
        "Machine Learning",
        "Mobile Development",
        "Web Development",
        "Blockchain",
        "NLP",
        "Genetic Algorithms",
        "Security",
        "Low Level Programming",
        "System Design",
        "System Administration",
        "Devops",
      ],
      currentSkills: [
        "Java",
        "Python",
        "Databases",
        "Javascript",
        "C++",
        "C#",
        "Graph Databases",
        "SQL Databases",
        "GO",
        "Scala",
        "Kubernetes",
        "Docker",
        "Ansible",
      ],
    };
  },
  methods: {
    onXClick() {
      this.$store.dispatch("disposeUserDetails");
    },
  },
  computed: {
    ...mapGetters(["showUserDetails", "userDetails", "isFetchingUserDetails"]),
    userDescriptionFormatted() {
      return this.userDescription
        .replace("$name", this.userDetails.name)
        .replace("$whatKindOf", this.articleAdjectives.sample())
        .replace("$projectAdjective", this.projectsAdjectives.sample())
        .replace("$skill1", this.currentSkills.sample())
        .replace("$skill2", this.currentSkills.sample())
        .replace("$skill3", this.currentSkills.sample())
        .replace("$interest1", this.interestTopics.sample());
    },
  },
};
</script>
