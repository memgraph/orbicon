import axios from 'axios';

export const fetchMessage = async function (){
  const response = await axios.get('/message')
  return response.data.message;
}

export const fetchNetwork = async function (){
  const response = await axios.get('/network')
  return response.data.network;
}