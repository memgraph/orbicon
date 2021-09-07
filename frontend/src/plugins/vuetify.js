import Vue from 'vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import '@mdi/font/css/materialdesignicons.css'


Vue.use(Vuetify);


export default new Vuetify({
  theme: {
    options: {
      customProperties: true
    },
    themes: {
      light: {
        primary: '#000',
        secondary: '#000',
        accent: '#000',
        error: '#000',
        lightGrey: '#f9f9f9',
        danger: '#d22',
        dangerHover: '#fb6e00'
      },
    },
  },
});
