import Vue from 'vue';

export const API_URL = 'http://localhost/5000';

export const apiClient = {
  getMemberGraph: () => {
    return Vue.axios.get(`${API_URL}/memberGraph`);
  },
  getUsernames: () => {
    return Vue.axios.get(`${API_URL}/usernames`);
  },
  getUserByUsername: (username) => {
    return Vue.axios.get(`${API_URL}/usernames/${username}`);
  },
  getRecentActivities: () => {
    return Vue.axios.get(`${API_URL}/activities`);
  },
}