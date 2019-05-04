import Vue from 'vue'
import VueRouter from 'vue-router'
import Page1 from '../components/Page1/Page1.vue'
import Page12 from '../components/Page1/Page12.vue'
import Page13 from '../components/Page1/Page13.vue'
import Page2 from '../components/Page2/Page2.vue'
import Page22 from '../components/Page2/Page22.vue'
import login from '../components/navi/login.vue'

Vue.use(VueRouter)

const router = new VueRouter({
    routes:[{
        path: '/Page1', component: Page1
    },{
        path: '/Page12', component: Page12
    },{
        path: '/Page13', component: Page13
    },{
        path: '/Page22', component: Page22
    },{
        path: '/Page2', component: Page2
    },{
        path: '/login', component: login
    }]
})

export default router;
