import Vue from 'vue';

export const API_URL = 'http://localhost:3000';

export const apiClient = {
  getMemberGraph: () => {
    return Vue.axios.get(`${API_URL}/memberGraph`);
  },
  getUsernames: () => {
    return Vue.axios.get(`${API_URL}/usernames`);
  },
  getUsernamesWithPrefix: (prefix) => {
    return Vue.axios.get(`${API_URL}/usernamesWithPrefix/${prefix}`);
  },
  getUserDetails: (username) => {
    return Vue.axios.get(`${API_URL}/userDetails/${username}`);
  },
  getActivities: () => {
    return Vue.axios.get(`${API_URL}/activities`);
  },
}