import Vue from 'vue'
import VueRouter from 'vue-router'
import Page1 from '../components/Page1/Page1.vue'
import Page12 from '../components/Page1/Page12.vue'
import Page13 from '../components/Page1/Page13.vue'
import Page2 from '../components/Page2/Page2.vue'
import Page22 from '../components/Page2/Page22.vue'
import login from '../components/navi/login.vue'
import Register from '../components/navi/Register.vue'
import navi from  '../components/navi/navi.vue'
import father from '../components/navi/father.vue'

Vue.use(VueRouter)

const router = new VueRouter({
    routes:[{
        path: '/', redirect: 'login'
    },{
        path: '/Register', name:Register, component: Register
    },
        {path: '/login', name: login, component: login
    }, {
        path: '/navi', component: navi,
            children: [
                {path: '/Page1', component: Page1},
                { path: '/Page12', component: Page12},
                {path: '/Page2', component: Page2},
                { path: '/Page22', component: Page22},
            ]
        }],
})

export default router;
