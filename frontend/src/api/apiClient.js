import Vue from 'vue';

export const API_URL = process.env.VUE_APP_API_URL;

export const apiRoutes = {
  memberGraphRoute() {
    return `${API_URL}/memberGraph`
  },
  usernamesRoute() {
    return `${API_URL}/usernames`
  },
  usernamesWithPrefixRoute(prefix) {
    return `${API_URL}/usernamesWithPrefix/${prefix}`
  },
  userDetailsRoute(username) {
    return `${API_URL}/userDetails/${username}`
  },
  activitiesRoute() {
    return `${API_URL}/activities`
  },
  legendRoute() {
    return `${API_URL}/legend`
  },
}

export const apiClient = {
  getMemberGraph: () => {
    return Vue.axios.get(apiRoutes.memberGraphRoute());
  },
  getUsernames: () => {
    return Vue.axios.get(apiRoutes.usernamesRoute());
  },
  getUsernamesWithPrefix: (prefix) => {
    return Vue.axios.get(apiRoutes.usernamesWithPrefixRoute(prefix));
  },
  getUserDetails: (username) => {
    return Vue.axios.get(apiRoutes.userDetailsRoute(username));
  },
  getActivities: () => {
    return Vue.axios.get(apiRoutes.activitiesRoute());
  },
  getLegend: () => {
    return Vue.axios.get(apiRoutes.legendRoute());
  }
}