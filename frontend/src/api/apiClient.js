import axios from 'axios';
import Vue from 'vue';

export const API_URL = 'http://localhost/5000';

export const fetchMessage = async function (){
  const response = await axios.get('/message')
  return response.data.message;
}

export const fetchNetwork = async function (){
  const response = await axios.get('/network')
  return response.data.network;
}

export const fetchNodes = async function (){
  const response = await axios.get('/nodes')
  return response.data.nodes;
}

export const fetchLinks = async function (){
  const response = await axios.get('/links')
  return response.data.links;
}

export const apiClient = {
  getMemberGraph: () => {
    return Vue.axios.get(`${API_URL}/memberGraph`);
  },
  getTwitterGraph: () => {
    return Vue.axios.get(`${API_URL}/twitterGraph`);
  },
  getGithubGraph: () => {
    return Vue.axios.get(`${API_URL}/githubGraph`);
  },
}