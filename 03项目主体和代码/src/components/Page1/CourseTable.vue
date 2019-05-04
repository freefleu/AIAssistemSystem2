<template>
    <div style="box-shadow: 2px 2px 5px #888888;border-radius:5px;">
        <div style="background-color:#20A0FF;padding:5px;color:white;overflow:hidden;border-radius:5px 5px 0 0">
            <span class="demonstration" style="float:left;padding:5px">课程列表</span>
        </div>

        <div style="margin:1%">
            <el-table
                    :data="tableData"
                    border
                    style="width: 100%"
                    :default-sort = "{prop: 'name', order: 'descending'}"
            >
                <el-table-column
                        prop="name"
                        label="名称"
                        align="center"
                        sortable>
                </el-table-column>

                <el-table-column
                        prop="id"
                        label="id"
                        align="center"
                        sortable>
                </el-table-column>

                <el-table-column
                        prop="teacher"
                        label="教师"
                        align="center"
                        sortable>
                </el-table-column>

               <!-- <el-table-column
                        prop="sex"
                        label="选课情况"
                        align="center"
                >
                    <template>
                        <el-button type="primary" >选课</el-button>
                    </template>
                </el-table-column>  -->

            </el-table>
        </div>

        <div class="block" align="center">
            <el-pagination
                    @size-change="handleSizeChange"
                    @current-change="handleCurrentChange"
                    :current-page="currentPage"
                    :page-sizes="[10, 20, 30, 40]"
                    :page-size="pageSize"
                    layout="total, sizes, prev, pager, next, jumper"
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
                        name: '操作系统',
                        //sex: '男',
                        type: 0,
                        teacher: '张明明',
                        math: 97,
                        verbal: 78,
                        specialize: 82
                    },
                    {
                        id: 2,
                        name: '计算机组成原理',
                        //sex: '女',
                        type: 0,
                        teacher:'李黎',
                        math: 80,
                        verbal: 90,
                        specialize: 84
                    },
                    {
                        id: 3,
                        name: '数据结构',
                       // sex: '男',
                        type: 0,
                        teacher: '王一一',
                        math: 94,
                        verbal: 99,
                        specialize: 97
                    },
                    {
                        id: 4,
                        name: '机器学习',
                       // sex: '女',
                        type: 0,
                        teacher: '黎明',
                        math: 100,
                        verbal: 90,
                        specialize: 85
                    }
                ],

                //详情页可见性
                detailDialogVisible: false,

                //被点击当前船舶信息
                nowShipInfo:'',

                //表格当前页
                currentPage: 1,

                //表格数据总量
                totalNum: 0,

                //每页显示数据数量
                pageSize: 10,
            }
        },

        methods: {
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
                            name: '操作系统',
                            sex: '男',
                            type: 0,
                            teacher: '张明明',
                            math: 97,
                            verbal: 78,
                            specialize: 82
                        },
                        {
                            id: 2,
                            name: '计算机组成原理',
                            sex: '女',
                            type: 0,
                            teacher: '李黎',
                            math: 80,
                            verbal: 90,
                            specialize: 84
                        },
                        {
                            id: 3,
                            name: '数据结构',
                            sex: '男',
                            type: 0,
                            teacher: '王一一',
                            math: 94,
                            verbal: 99,
                            specialize: 97
                        },
                        {
                            id: 4,
                            name: '机器学习',
                            sex: '女',
                            type: 0,
                            teacher: '黎明',
                            math: 100,
                            verbal: 90,
                            specialize: 85
                        }
                    ]
                }

                this.totalNum = this.tableData.length;
            },

            //每页显示数据变更响应
            handleSizeChange(val) {
                this.pageSize = val;
                this.loadData();
            },

            //换页响应
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
