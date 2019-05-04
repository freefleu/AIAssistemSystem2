<template>
    <div>
        <div style="border:1px solid;background-color:#FFFFFF;box-shadow: 2px 2px 5px #888888;overflow: hidden;border-radius:5px;">
            <div style="background-color:#20A0FF;padding:5px;color:white;">
                退课
            </div>
            <br/>

            <el-form ref="form" :model="form" :inline=true label-width="70px" label-position="left" style="margin-left: 5%">
                <el-row :gutter="10">
                    <el-col :xs="24" :sm="7" :md="7" :lg="8">
                        <el-form-item label="id" prop="id">
                            <el-input v-model="form.id"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>

                <el-form-item style="float:right">
                    <el-button type="primary" >退课</el-button>
                </el-form-item>

            </el-form>
        </div>
    </div>
</template>

<script type="text/ecmascript-6">
    //import { mapActions } from 'vuex'
    export default {
        data () {
            return {
                //提交的表单
                form: {

                    id:''
                },
            }
        },
 /*
        methods: {
            ...mapActions({
                saveFormVal: 'changeCourseFormAction',
                search: 'changeCourseQueryFlagAction'
            }),

            //重置表单
            resetForm(formName) {
                this.$refs[formName].resetFields();
            },

            //提交表单
            submitForm: function() {
                this.search(true);
            },
        },

        mounted () {
            this.saveFormVal(this.form);
        },

        computed: {
            courseTypeList(){
                return this.$store.state.Navi.courseTypeList;
            }
        } */
    }
</script>