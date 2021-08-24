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
  twitterGraph: {},
  githubGraph: {},

}

const mutations = {
  SET_MEMBER_GRAPH(state, memberGraph) {
    state.memberGraph = memberGraph;
  },
  SET_TWITTER_GRAPH(state, twitterGraph) {
    state.twitterGraph = twitterGraph
  },
  SET_GITHUB_GRAPH(state, githubGraph) {
    state.githubGraph = githubGraph
  }
}

const actions = {
  loadMemberGraph(context) {
    apiClient.getMemberGraph()
      .then((resp) => {
        context.commit(MUTATION_CONSTANTS.SET_MEMBER_GRAPH, resp.data.memberGraph);
      })
  },
  loadTwitterGraph(context) {
    apiClient.getTwitterGraph()
      .then((resp) => {
        context.commit(MUTATION_CONSTANTS.SET_TWITTER_GRAPH, resp.data.twitterGraph);
      })
  },
  loadGithubGraph(context) {
    apiClient.getGithubGraph()
      .then((resp) => {
        context.commit(MUTATION_CONSTANTS.SET_GITHUB_GRAPH, resp.data.githubGraph);
      })
  }
}

const getters = {
  memberGraph: state => state.memberGraph,
  githubGraph: state => state.githubGraph,
  twitterGraph: state => state.twitterGraph,
}


export const store = new Vuex.Store({
  state,
  mutations,
  actions,
  getters,
});