import Vue from 'vue'
import App from './App'
import router from './router'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    token: undefined,
    secret: undefined
  },
  mutations: {
    setToken (state, token) {
      state.token = token
    },
    setSecret (state, secret) {
      state.secret = secret
    },
  }
})

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
