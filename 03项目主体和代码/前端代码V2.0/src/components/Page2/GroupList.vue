<template>
    <div style="box-shadow: 2px 2px 5px #888888;border-radius:5px;">
        <div style="background-color:#20A0FF;padding:5px;color:white;overflow:hidden;border-radius:5px 5px 0 0">
            <span class="demonstration" style="float:left;padding:5px">我加入的队伍</span>
        </div>

        <div style="margin:1%">
            <el-table
                    :data="tableData"
                    border
                    style="width: 100%"
                    :default-sort = "{prop: 'name', order: 'descending'}"
            >
                <el-table-column
                        prop="courseName"
                        label="课程名称"
                        align="center"
                        sortable>
                </el-table-column>
                <el-table-column
                        prop="groupID"
                        label="组ID"
                        align="center"
                        sortable>
                </el-table-column>

                <el-table-column
                        prop="groupName"
                        label="组名称"
                        align="center"
                        sortable>
                </el-table-column>

                <el-table-column
                        prop="groupLeader"
                        label="组长"
                        align="center"
                        sortable>
                </el-table-column>

                <el-table-column
                        prop="mem1"
                        label="成员1"
                        align="center"
                        sortable>
                </el-table-column>

                <el-table-column
                        prop="mem2"
                        label="成员2"
                        align="center"
                        sortable>
                </el-table-column>

                <el-table-column
                        prop="mem3"
                        label="成员3"
                        align="center"
                        sortable>
                </el-table-column>

                <el-table-column
                        prop="mem4"
                        label="成员4"
                        align="center"
                        sortable>
                </el-table-column>

                <el-table-column
                        prop="select"
                        label="操作栏"
                        align="center"
                >
                    <template>
                        <el-button size="small"  type="primary" @click="quit" >退组</el-button>
                    </template>
                </el-table-column>

                <el-table-column
                        prop="select"
                        label="可加入"
                        align="center"
                >
                    <template>

                        <el-upload
                                ref="upload"
                                class="upload-demo"
                                action="https://jsonplaceholder.typicode.com/posts/"
                                :on-preview="handlePreview"
                                :limit="1"
                                :auto-upload="false"
                                :on-change="handleChange"
                                :show-file-list="true"
                                :file-list="fileList"
                                :on-error="handleError"
                                :on-success="handleSuccess">

                            <el-button size="small" type="primary">文件上传</el-button>
                        </el-upload>
                    </template>
                </el-table-column>

            </el-table>
        </div>

        <div class="block" align="center">
            <el-pagination
                    @size-change="handleSizeChange"
                    @current-change="handleCurrentChange"
                    :current-page="currentPage"
                    layout="total, prev, pager, next, jumper"
                    :total="totalNum">
            </el-pagination>
        </div>
    </div>
</template>

<script>
    import { mapActions } from 'vuex'
    export default {
        props:['searchflag'],
        data () {
            return {

                //表格数据
                tableData:[
                    {
                        id: 1,
                        groupID: '01',
                        courseName: '操作系统',
                        type: 0,
                        groupLeader: '李雷',
                        groupName:'最强王者',
                        mem1:'张三',
                        math: 97,
                        verbal: 78,
                        specialize: 82
                    },
                    {
                        id: 2,
                        groupID: '02',
                        courseName: '计算机组成原理',
                        type: 0,
                        groupLeader:'韩梅梅',
                        groupName:'好',
                        mem1:'Tony Stark',
                        mem2:'张三',
                        math: 80,
                        verbal: 90,
                        specialize: 84
                    },

                ],

                fileList: [
                ],
                bool: true,


                //详情页可见性
                detailDialogVisible: false,

                //被点击当前船舶信息
                nowShipInfo:'',

                //表格当前页
                currentPage: 1,

                //表格数据总量
                totalNum: 2,


            }
        },

        methods: {
            quit(){

            },
            upload(){

            },
            //加载表格ajax
            loadData(){
                var id = this.$store.state.course.CourseForm.id;
                var tabledata = [];
                console.log(id)
                if(id != ''){
                    this.tableData.forEach((item) => {
                        if(item.id == id)
                            tabledata.push(item)
                    })
                    this.tableData = tabledata;
                }
                else{
                    this.tableData=[
                        {
                            id: 1,
                            groupID: '01',
                            courseName: '操作系统',
                            type: 0,
                            groupLeader: '李雷',
                            groupName:'最强王者',
                            math: 97,
                            verbal: 78,
                            specialize: 82
                        },
                        {
                            id: 2,
                            groupID: '02',
                            courseName: '计算机组成原理',
                            type: 0,
                            groupLeader:'韩梅梅',
                            groupName:'好',
                            math: 80,
                            verbal: 90,
                            specialize: 84
                        },
                    ]
                }

                this.totalNum = this.tableData.length;
            },

            //每页显示数据变更响应
            handleSizeChange(val) {
                this.loadData();
            },


            handleCurrentChange(val) {
                this.currentPage = val;
                this.loadData();
            },

            ...mapActions({
                search: 'changeCourseQueryFlagAction'
            }),
        },

        mounted () {
            this.loadData();
        },

        handleRemove(file, fileList) {
            console.log(file, fileList);
        },
        handlePreview(file) {
            console.log(file);
        },
        handleError(err, file) {
            alert('失败')
            this.fileList = []
        },
        handleSuccess(res, file) {
            alert('成功')
            this.fileList = []
        },
        handleExceed(files, fileList) {},
        async handleChange() {
            const isSubmit = await this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                return false
            }).catch(() => {
                return true
            });

            if (isSubmit) {
                this.$refs.upload.submit()
            } else {
                this.fileList = []
            }
        },
        watch: {
            searchflag(newval,oldval){
                if(newval){
                    this.loadData();
                    this.search(false);
                }
            }
        }
    }
</script>

<style>

</style>
