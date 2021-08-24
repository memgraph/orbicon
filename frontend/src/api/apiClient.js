import axios from 'axios';

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