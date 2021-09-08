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
        blacky: "#000",
        primary: '#000',
        secondary: '#000',
        accent: '#000',
        error: '#000',
        lightGrey: '#f9f9f9',
        grey: '#857f97',
        danger: '#d22',
        dangerHover: '#fb6e00',
        success: "#00a400",
        blue: "#0ae",
      },
    },
  },
});
