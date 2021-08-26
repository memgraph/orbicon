import Vue from 'vue';

export const API_URL = 'http://localhost:3000';

export const apiClient = {
  getMemberGraph: () => {
    return Vue.axios.get(`${API_URL}/memberGraph`);
  },
  getUsernames: () => {
    return Vue.axios.get(`${API_URL}/usernames`);
  },
  getUserDetails: (username) => {
    console.log(username)
    return Vue.axios.get(`${API_URL}/userDetails`);
  },
  getActivities: () => {
    return Vue.axios.get(`${API_URL}/activities`);
  },
}