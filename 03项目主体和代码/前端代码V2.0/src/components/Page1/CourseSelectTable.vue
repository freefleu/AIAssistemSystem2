<template>
    <div style="box-shadow: 2px 2px 5px #888888;border-radius:5px;">
        <div style="background-color:#20A0FF;padding:5px;color:white;overflow:hidden;border-radius:5px 5px 0 0">
            <span class="demonstration" style="float:left;padding:5px">已选课程</span>
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
                       >
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
                       >
                </el-table-column>

                <el-table-column
                        prop="location"
                        label="时间地点"
                        align="center"
                        sortable>
                </el-table-column>

                <el-table-column
                        prop="college"
                        label="学院"
                        align="center"
                        >
                </el-table-column>

                <el-table-column
                        prop="num"
                        label="选课人数"
                        align="center"
                        sortable>
                </el-table-column>

                <el-table-column
                        prop="review"
                        label="历史评分"
                        align="center"
                        sortable>
                </el-table-column>

                <el-table-column
                        prop="ave"
                        label="学生平均分"
                        align="center"
                        sortable>
                </el-table-column>

                <el-table-column
                        prop="unpass"
                        label="未通过率"
                        align="center"
                        sortable>
                </el-table-column>


                <el-table-column
                        prop="select"
                        label="选课情况"
                        align="center"
                >
                    <template slot-scope="scope">
                        <el-button type="primary" v-if="!scope.row.editing" @click="handleDelete(scope.$index, scope.row)" >退课</el-button>
                    </template>
                </el-table-column>

                <el-table-column
                        prop="group"
                        label="组队情况"
                        align="center"
                >
                    <template>
                        <el-button  type="primary" v-on:click="togroup()" >组队</el-button>
                    </template>
                </el-table-column>

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
                        id: 3,
                        name: '数据结构',
                        // sex: '男',
                        type: 0,
                        teacher: '王一一',
                        location: '周三56-六教211',
                        college:'计算机学院',
                        num: 40,
                        review:94,
                        ave:76,
                        unpass:0.13,
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
                        location: '周四56-理教216',
                        college:'智能学院',
                        num: 53,
                        review:90,
                        ave:80,
                        unpass:0.10,
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
                totalNum: 2,

                //每页显示数据数量
                pageSize: 10,
            }
        },

        methods: {
            handleDelete(index){ //删除行数
                this.tableData.splice(index, 1)
            },
            open(){
                this.$message("退课成功！")
            },
            togroup(){
                this.$router.push('/Page2')
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
                            id: 3,
                            name: '数据结构',
                            sex: '男',
                            type: 0,
                            teacher: '王一一',
                            location: '周三56-六教211',
                            college:'计算机学院',
                            num: 40,
                            review:94,
                            ave:76,
                            unpass:0.13,
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
                            location: '周四56-理教216',
                            college:'智能学院',
                            num: 53,
                            review:90,
                            ave:80,
                            unpass:0.10,
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
