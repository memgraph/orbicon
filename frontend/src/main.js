import Vue from 'vue'
import VueMeta from 'vue-meta';
import App from './App.vue'
import vuetify from './plugins/vuetify';
import { store } from './store/store.js';

Vue.config.productionTip = false
Vue.use(VueMeta)

if (process.env.VUE_APP_NODE_ENV === 'development') {
  const { worker } = require('./mocks/browser')
  worker.start()
}

Array.prototype.sample = function() {
  return this[Math.floor(Math.random()*this.length)];
}

new Vue({
  vuetify,
  store,
  render: h => h(App),
}).$mount('#app')
