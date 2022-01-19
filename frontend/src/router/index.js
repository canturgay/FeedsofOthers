import Vue from 'vue'
import Router from 'vue-router'
/* eslint-disable no-new */
const routerOptions = [
  { path: '/', component: 'twitterAuth' },
  { path: '/shareGet', component: 'shareGet' }
]
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})
