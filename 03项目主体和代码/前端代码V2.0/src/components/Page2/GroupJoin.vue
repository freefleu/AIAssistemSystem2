<!--<template>
 div>
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
</template> -->

<template>
    <div style="box-shadow: 2px 2px 5px #888888;border-radius:5px;">
        <div style="background-color:#20A0FF;padding:5px;color:white;overflow:hidden;border-radius:5px 5px 0 0">
            <span class="demonstration" style="float:left;padding:5px">课程已有队伍</span>
        </div>

        <div style="margin:1%">
            <el-table
                    :data="tableData"
                    border
                    style="width: 100%"
                    :default-sort = "{prop: 'name', order: 'descending'}"
                    @row-click="handleSelectionChange"
            >
                <el-table-column
                    prop="groupName"
                    label="组名称"
                    align="center"
                    sortable
                   >
                </el-table-column>

                <el-table-column
                        prop="groupID"
                        label="组ID"
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
                        label="我要加入"
                        align="center"
                        fixed
                >
                    <template>
                        <el-button type="primary" >加入</el-button>
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
    import bus from './bus.js'
    var temps;
    var id;
    var data;
    export default {
        props:['searchflag'],
        data () {
            return {
                //表格数据
                tableData:[
                    {
                        id: 1,
                        groupID: '01',
                        type: 0,
                        groupLeader: '马秦',
                        groupName:'最强王者',
                        mem1:'张小虎',
                        mem2:'',
                        math: 97,
                        verbal: 78,
                        specialize: 82
                    },
                    {
                        id: 2,
                        groupID: '02',
                        type: 0,
                        groupLeader:'韩梅梅',
                        groupName:'好',
                        mem1:'Tony Stark',
                        mem2:'陈彼得',
                        mem3:'张玛丽',
                        mem4:'王可',
                        math: 80,
                        verbal: 90,
                        specialize: 84
                    },



                ],
                  msg:'默认',
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
            handleSelectionChange(row,event,column){
                if(row['mem4'] === undefined){
                    temps = 0;
                }else{
                    temps = 1;
                }
                if ( temps === 0 ){
                    this.$message({
                        message: '加入成功！',
                        type: 'success'
                    });
                    row['mem2']='zhangsan';
                }
                else {
                    this.$message({
                        message: '成员已满，无法加入！',
                        type: 'warning'
                    });
                }
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
                            type: 0,
                            groupLeader: '马秦',
                            groupName:'最强王者',
                            mem1:'张小虎',
                            mem2:'',
                            mem3:'',
                            mem4:'',
                            math: 97,
                            verbal: 78,
                            specialize: 82
                        },
                        {
                            id: 2,
                            groupID: '02',
                            type: 0,
                            groupLeader:'韩梅梅',
                            groupName:'好',
                            mem1:'Tony Stark',
                            mem2:'陈彼得',
                            mem3:'张玛丽',
                            mem4:'王可',
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
            var self = this;
            var groupnames;
            bus.$on("event",function(msg){
              //  alert(msg);
               groupnames= msg;
                data = {
                    groupID: '03',
                    courseName: '机器学习',
                    type: 0,
                    groupLeader: '张三',
                    groupName:groupnames,
                    mem1:'',
                    math: 97,
                    verbal: 78,
                    specialize: 82
                };
                console.log(data);
                self.tableData.push(data);
            });
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
