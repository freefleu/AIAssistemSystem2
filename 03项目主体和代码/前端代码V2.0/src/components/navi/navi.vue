<template>
    <div style="background-color: #EBEBEB;min-height:800px">
        <div style="width:100%;background-color:#20A0FF; overflow: hidden">
            <span class="demonstration" style="float:left;padding-top:10px;color:white;margin-left:1%">
                学习辅助系统 Your Personal Assistant
            </span>
            <span class="demonstration" style="float:left;padding:5px;color:white;margin-left:2%;width:15%">
                 <el-input
                         placeholder="Search here"
                         icon="search"
                         v-model="searchCriteria"
                         :on-icon-click="handleIconClick">
                </el-input>
            </span>

            <span class="demonstration" style="float:right;padding-top:10px;margin-right:1%">
                <el-dropdown trigger="click">
                  <span class="el-dropdown-link" style="color:white">
                    张三 <i class="el-icon-caret-bottom el-icon--right"></i>
                  </span>
                  <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item @click.native="toregis" >个人信息</el-dropdown-item>
                    <el-dropdown-item  @click.native="tologin">退出登录</el-dropdown-item>
                  </el-dropdown-menu>
                </el-dropdown>
            </span>
        </div>

        <div style="margin-top:5px">
            <el-row :gutter="10">
                <el-col :xs="4" :sm="4" :md="4" :lg="4">
                    <div>
                    <el-menu router :default-active="$route.path"   class="el-menu-vertical-demo"
                            style="min-height:900px" @select="handleSelect" >
                        <el-submenu index="1">
                            <template slot="title">
                                <i class="el-icon-location"></i>
                                <span>选课</span>
                            </template>
                            <el-menu-item-group>

                                <el-menu-item index="Page1">网上选课</el-menu-item>
                                <el-menu-item index="Page12">选课结果</el-menu-item>
                               <!-- <el-menu-item index="Page13">提交作业</el-menu-item> -->
                            </el-menu-item-group>
                            <!-- <el-menu-item-group title="分组2">
                                 <el-menu-item index="1-3">选项3</el-menu-item>
                             </el-menu-item-group>
                             <el-submenu index="1-4">
                                 <template slot="title">选项4</template>
                                 <el-menu-item index="1-4-1">选项1</el-menu-item>
                             </el-submenu>-->
                        </el-submenu>
                        <el-submenu index="2">
                            <template slot="title">
                                <i class="el-icon-location"></i>
                                <span>组队</span>
                            </template>
                            <el-menu-item-group>
                                <el-menu-item index="Page2">我要组队</el-menu-item>
                                <el-menu-item index="Page22">我的队伍</el-menu-item>
                            </el-menu-item-group>
                        </el-submenu>
                    </el-menu>
                    </div>
                </el-col>

                <el-col :xs="20" :sm="20" :md="20" :lg="20">
                    <div>
                        <div style="border: 1px solid #A6A6A6; border-radius:6px; padding:5px; margin:2px; background-color: white">
                            <el-breadcrumb separator="/">
                                <el-breadcrumb-item v-for="item in breadcrumbItems">{{item}}</el-breadcrumb-item>
                            </el-breadcrumb>
                        </div>
                    </div>
                    <div style="margin-top:10px">
                        <router-view></router-view>
                    </div>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script type="text/ecmascript-6">
    import { mapActions } from 'vuex'
    export default {
        data() {
            return {
                searchCriteria: '',
                breadcrumbItems: ['Welcome'],
            };
        },

        methods:{
            tologin(){
                this.$router.push('/login')
            },
            toregis(){
                this.$router.push('/Register')
            },
           handleIconClick(ev) {
               console.log(ev);
            },

            handleSelect(key, keyPath){
                switch(key){
                    case '1':
                        this.$router.push('/Page1');
                        this.breadcrumbItems  = ['选课']
                        break;
                    case '2':
                        this.$router.push('/Page2')
                        this.breadcrumbItems  = ['组队']
                        break;
                   /* case '3':
                        this.$router.push('/Page3')
                        this.breadcrumbItems  = ['查询']
                        break;*/
                }
            },

            ...mapActions({
                initStudentType: 'changeStudentTypeListAction'
            }),

        },


    }
</script>
