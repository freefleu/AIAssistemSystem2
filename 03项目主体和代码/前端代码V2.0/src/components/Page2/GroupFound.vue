<template>
    <div>
        <div style="border:1px solid;background-color:#FFFFFF;box-shadow: 2px 2px 5px #888888;overflow: hidden;border-radius:5px;">
            <div style="background-color:#20A0FF;padding:5px;color:white;">
                组建队伍
            </div>
            <br/>

            <el-form ref="form" :model="form" :inline=true label-width="70px" label-position="left" style="margin-left: 5%">
                <el-row :gutter="10">
                    <el-col :xs="24" :sm="7" :md="7" :lg="8">
                        <el-form-item label="队伍名称" prop="id">
                            <el-input v-model="form.name"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>


                <el-form-item style="float:right">
                    <el-button type="primary" v-on:click="build">组建</el-button>
                </el-form-item>

            </el-form>
        </div>
    </div>
</template>

<style>

</style>

<script type="text/ecmascript-6">
    import bus from './bus.js'
    export default {
        data() {
            return {
                //提交的表单
                form: {

                    name: ''
                },
            }
        },
        methods: {
            build:function(){
                bus.$emit("event",this.form.name)
            }
        }
    }


</script>