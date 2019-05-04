/*
 * 导航页
 */
const state = {
    //学生类型
    courseTypeList:[],

}

const actions = {
    //存入交通类型数据
    changeCourseTypeListAction({commit}, payload) {
        commit('changeCourseTypeListMutation', payload)
    },
}

//mutations，真正用来修改state的方法集
const mutations = {
    changeCourseTypeListMutation (state, payload) {
        state.courseTypeList = payload
    },
}

const getter = {

}

const moduleNavi = {
    state: state,
    mutations: mutations,
    actions: actions,
    getter: getter
}

export default moduleNavi;
