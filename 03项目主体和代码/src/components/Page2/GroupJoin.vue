<template>
    <div>
        <div style="border:1px solid;background-color:#FFFFFF;box-shadow: 2px 2px 5px #888888;overflow: hidden;border-radius:5px;">
            <div style="background-color:#20A0FF;padding:5px;color:white;">
                加入队伍
            </div>
            <br/>

            <el-form ref="form" :model="form" :inline=true label-width="70px" label-position="left" style="margin-left: 5%">
                <el-row :gutter="10">
                    <el-col :xs="24" :sm="7" :md="7" :lg="8">
                        <el-form-item label="组ID" prop="id">
                            <el-input v-model="form.id"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>

                <el-dropdown @command="handleCommand">
                        <span class="el-dropdown-link">
                          队员位置<i class="el-icon-arrow-down el-icon--right"></i>
                        </span>
                     <el-dropdown-menu slot="dropdown">
                             <el-dropdown-item command="mem1">成员1</el-dropdown-item>
                            <el-dropdown-item command="mem2">成员2</el-dropdown-item>
                            <el-dropdown-item command="mem3">成员3</el-dropdown-item>
                            <el-dropdown-item command="mem4">成员4</el-dropdown-item>
                     </el-dropdown-menu>
                </el-dropdown>

                <el-form-item style="float:right">
                    <el-button type="primary" >加入</el-button>
                </el-form-item>

            </el-form>
        </div>
    </div>
</template>

<style>
    .el-dropdown-link {
        cursor: pointer;
        color: #409EFF;
    }
    .el-icon-arrow-down {
        font-size: 12px;
    }
</style>

<script type="text/ecmascript-6">
    //import { mapActions } from 'vuex'
    export default {
        methods: {
            handleCommand(command) {
                this.$message('click on item ' + command)
            }
        },
        data() {
            return {
                //提交的表单
                form: {

                    id: ''
                },
            }
        }
    }


</script>