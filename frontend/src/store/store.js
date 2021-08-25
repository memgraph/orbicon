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
  searchUsernames: [],
  userDetails: {},
  activities: [],
}

const mutations = {
  SET_MEMBER_GRAPH(state, memberGraph) {
    state.memberGraph = memberGraph;
  },
  SET_USERNAMES(state, usernames) {
    state.memberGraph = usernames
  },
  SET_USER_DETAILS(state, userDetails) {
    state.userDetails = userDetails
  },
  SET_ACTIVITIES(state, activities) {
    state.activities = activities;
  }
}

const actions = {
  getMemberGraph(context) {
    apiClient.getMemberGraph()
      .then((resp) => {
        context.commit(MUTATION_CONSTANTS.SET_MEMBER_GRAPH, resp.data.memberGraph);
      })
  },
  getUsernames(context) {
    apiClient.getUsernames()
      .then((resp) => {
        context.commit(MUTATION_CONSTANTS.SET_USERNAMES, resp.data.usernames);
      })
  },
  getUserDetails(context) {
    apiClient.getUserDetails()
      .then((resp) => {
        context.commit(MUTATION_CONSTANTS.SET_USER_DETAILS, resp.data.userDetails);
      })
  },
  getActivities(context) {
    apiClient.getActivities()
      .then((resp) => {
        context.commit(MUTATION_CONSTANTS.SET_ACTIVITIES, resp.data.activities);
      })
  }
}

const getters = {
  memberGraph: state => state.memberGraph,
  usernames: state => state.usernames,
  userDetails: state => state.userDetails,
  activities: state => state.activities,
}


export const store = new Vuex.Store({
  state,
  mutations,
  actions,
  getters,
});