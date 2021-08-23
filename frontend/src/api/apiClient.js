import axios from 'axios';

export const fetchMessage = async function (){
  const response = await axios.get('/message')
  return response.data.message;
}
