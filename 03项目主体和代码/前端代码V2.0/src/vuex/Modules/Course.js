/*
 * 学生基本信息
 */
const state = {
    //查询学生基本信息的表单
    courseForm: {
        id: '',
        name: '',
        type: '',
    },

    //是否进行查询
    courseQueryFlag: false,

}

const actions = {
    //存入搜索船舶基本资料form值
    changeCourseFormAction({commit}, payload) {
        commit('changeCourseFormMutation', payload)
    },

    //更改是否搜索标识
    changeCourseQueryFlagAction ({commit}, payload){
        commit('changeCourseQueryFlagMutation', payload)
    },

}

//mutations，真正用来修改state的方法集
const mutations = {
    changeCourseFormMutation (state, payload) {
        state.courseForm = payload
    },

    changeCourseQueryFlagMutation (state, payload) {
        state.courseQueryFlag = payload
    },
}

const getter = {

}

const moduleCourse = {
    state: state,
    mutations: mutations,
    actions: actions,
    getter: getter
}

export default moduleCourse;
