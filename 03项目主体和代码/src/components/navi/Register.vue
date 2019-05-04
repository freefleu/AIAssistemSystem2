<template>
    <el-main>
        <el-form
                :model="ReginForm"
                ref="ReginForm"
                :rules="rule"
                class="regform"
                label-width="0">

            <h3>用户注册</h3>

            <el-form-item prop="StuID">
                <el-input
                        type="text"
                        v-model="ReginForm.StuID"
                        placeholder="学号">
                </el-input>
            </el-form-item>

            <el-form-item prop="Password">
                <el-input
                        type="Password"
                        v-model="ReginForm.Password"
                        placeholder="密码">
                </el-input>
            </el-form-item>

            <el-form-item prop="StuName">
                <el-input
                        type="email"
                        v-model="ReginForm.StuName"
                        placeholder="姓名">
                </el-input>
            </el-form-item>

            <el-form-item prop="Sex">
                <el-input
                        type="text"
                        v-model.number="ReginForm.Sex"
                        placeholder="性别">
                </el-input>
            </el-form-item>

            <el-form-item prop="Department">
                <el-input
                        type="text"
                        v-model="ReginForm.Department"
                        placeholder="学院">
                </el-input>
            </el-form-item>

            <div style="margin-top: 20px">
                <el-button type="text" disabled>是否爱合作</el-button>
                <el-radio-group border size="small">
                    <el-radio label="1" border >是</el-radio>
                    <el-radio label="2" border >否</el-radio>
                </el-radio-group>
            </div>

            <el-button type="text" disabled>是否爱钻研</el-button>
            <el-radio-group  size="small">
                <el-radio label="3" border>是</el-radio>
                <el-radio label="4" border>否</el-radio>
            </el-radio-group>

            <el-button type="text" disabled>是否爱实践</el-button>
            <el-radio-group  size="small">
                <el-radio label="5" border>是</el-radio>
                <el-radio label="6" border>否</el-radio>
            </el-radio-group>

            <el-button type="text" disabled>是否英语好</el-button>
            <el-radio-group  size="small">
                <el-radio label="7" border>是</el-radio>
                <el-radio label="8" border>否</el-radio>
            </el-radio-group>

            <el-button type="text" disabled>是否写作能力强</el-button>
            <el-radio-group size="small">
                <el-radio label="9" border>是</el-radio>
                <el-radio label="10" border>否</el-radio>
            </el-radio-group>

            <el-button type="text" disabled>是否交流能力强</el-button>
            <el-radio-group  size="small">
                <el-radio label="11" border>是</el-radio>
                <el-radio label="12" border>否</el-radio>
            </el-radio-group>

            <el-form-item >
                <el-button
                        type="success"
                        class="submitBtn"
                        round
                        @click.native.prevent="submit"
                        :loading="logining">
                    注册
                </el-button>
                <el-button
                        type="primary"
                        class="resetBtn"
                        round
                        @click.native.prevent="reset">
                    重置
                </el-button>
                <hr>
                <p>已经有账号，马上去<span class="to" @click="tologin">登录</span></p>
            </el-form-item>
        </el-form>
    </el-main>
</template>
<script>
    export default {
        data () {

            let confirmpasswordCheck = (rule, value, callback) => {
                if (value === '') {
                    return callback(new Error('密码是必须的'))
                } else if (value !== this.ReginForm.password) {
                    return callback(new Error('两次输入的密码不一致'))
                } else {
                    return callback()
                }
            }
            let telCheck = (rule, value, callback) => {
                if (value === '') {
                    return callback(new Error('电话号码是必须的'))
                } else if (!Number.isInteger(value)) {
                    return callback(new Error('电话号码必须是数字'))
                } else if (value.toString().length !== 11) {
                    return callback(new Error('电话号码必须是11位数字'))
                } else {
                    callback()
                }
            }
            return {
                ReginForm: {
                    StuID: '',
                    Password: '',
                    StuName: '',
                    Sex: '',
                    Department: '',
                },
                logining: false,
                rule: {
                    StuID: [
                        {
                            required: true,
                            max: 10,
                            min: 10,
                            message: '学号是必须的，长度为10位',
                           // trigger: 'blur'
                        }
                    ],
                    Password: [
                        {
                            required: true,
                            message: '密码是必须的！',
                            trigger: 'blur'
                        }
                    ],

                    /*tel: [
                        {
                            required: true,
                            validator: telCheck,
                            trigger: 'blur'
                        }
                    ], */
                    StuName: [
                        {
                            required: true,
                            message: '请输入您的姓名',
                        }
                    ],
                    Sex: [
                        {
                            required: true,
                            message: '请输入您的性别',
                        }
                    ],
                    Department: [
                        {
                            required: true,
                            message: '请输入您所在的学院',
                        }
                    ],
                }
            }
        },
        methods: {
            // ...
            submit () {
                this.$refs.ReginForm.validate(valid => {
                    if (valid) {
                        this.logining = true
                        console.log('开始写入后台数据！')
                    } else {
                        console.log('submit err')
                    }
                })
            },
            reset () {
                this.$refs.ReginForm.resetFields()
            },
            tologin () {
                this.$router.push('/login')
            }
        }
    }
</script>

<style scoped>
    .regform {
        margin: 20px auto;
        width: 310px;
        background: #fff;
        box-shadow: 0 0 10px #B4BCCC;
        padding: 30px 30px 0 30px;
        border-radius: 25px;
    }
    .submitBtn {
        width: 65%;
    }
    .to {
        color: #FA5555;
        cursor: pointer;
    }
</style>
