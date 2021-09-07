import axios from 'axios';
import VueAxios from 'vue-axios';
import Vue from 'vue';
import Vuex from 'vuex';
import { apiClient } from '../api/apiClient';
import { MUTATION_CONSTANTS } from './mutationConstants';

Vue.use(VueAxios, axios)
Vue.use(Vuex);

const state = {
  memberGraph: {
    nodes: [],
    edges: []
  },
  usernames: [],
  isFetchingUserDetails: false,
  userDetails: {},
  activities: [],
  showUserDetails: false,
}

const mutations = {
  SET_MEMBER_GRAPH(state, memberGraph) {
    state.memberGraph = memberGraph;
  },
  SET_USERNAMES(state, usernames) {
    state.usernames = usernames.map(x => x.username);
  },
  SET_USER_DETAILS(state, userDetails) {
    state.userDetails = userDetails
  },
  SET_ACTIVITIES(state, activities) {
    state.activities = activities;
  },
  SHOW_USER_DETAILS(state) {
    state.showUserDetails = true;
  },
  DISPOSE_USER_DETAILS(state) {
    state.showUserDetails = false;
  },
  SET_IS_FETCHING_USER_DETAILS(state, isFetchingUserDetails) {
    state.isFetchingUserDetails = isFetchingUserDetails;
  }
}

const actions = {
  async getMemberGraph(context) {
    apiClient.getMemberGraph()
      .then((resp) => {
        context.commit(MUTATION_CONSTANTS.SET_MEMBER_GRAPH, resp.data);
      })
  },
  async getUsernames(context) {
    apiClient.getUsernames()
      .then((resp) => {
        context.commit(MUTATION_CONSTANTS.SET_USERNAMES, resp.data.usernames);
      })
  },
  async getUsernamesWithPrefix(context, prefix) {
    apiClient.getUsernamesWithPrefix(prefix)
      .then((resp) => {
        context.commit(MUTATION_CONSTANTS.SET_USERNAMES, resp.data.usernames);
      })
  },
  getActivities(context) {
    apiClient.getActivities()
      .then((resp) => {
        context.commit(MUTATION_CONSTANTS.SET_ACTIVITIES, resp.data.activities);
      })
  },
  async showUserDetails(context, usernameInput) {
    apiClient.getUserDetails(usernameInput)
      .then((resp) => {
        context.commit(MUTATION_CONSTANTS.SET_USER_DETAILS, resp.data);
      })
      .then(() => {
        context.commit(MUTATION_CONSTANTS.SHOW_USER_DETAILS)
      })
  },
  disposeUserDetails(context) {
    context.commit(MUTATION_CONSTANTS.DISPOSE_USER_DETAILS)
  },
  async setIsFetchingUserDetails(context, isFetchingUserDetails) {
    context.commit(MUTATION_CONSTANTS.SET_IS_FETCHING_USER_DETAILS, isFetchingUserDetails);
  }
}

const getters = {
  memberGraph: state => state.memberGraph,
  usernames: state => state.usernames,
  userDetails: state => state.userDetails,
  activities: state => state.activities,
  showUserDetails: state => state.showUserDetails,
  isFetchingUserDetails: state => state.isFetchingUserDetails,
}


export const store = new Vuex.Store({
  state,
  mutations,
  actions,
  getters,
});