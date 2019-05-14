import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Register from './components/navi/Register.vue'
import router from './router/index'
import store from './vuex/index'
import login from './components/navi/login.vue'
import navi from './components/navi/navi.vue'
import father from './components/navi/father.vue'


Vue.use(ElementUI)

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(father)
})
