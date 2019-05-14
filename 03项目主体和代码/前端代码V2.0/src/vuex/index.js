import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import Navi from './Modules/Navi'
import course from './Modules/Course'

export default new Vuex.Store({
    modules: {
        Navi: Navi,
        course: course
    }
})
