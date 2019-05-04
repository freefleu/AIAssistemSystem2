<template>
    <div>
        <div style="border-radius:5px;">
            <CourseForm></CourseForm>
        </div>

        <br/>

        <div style="border:1px solid;margin-top:5px;background-color:#FFFFFF;border-radius:5px">
            <CourseTable :searchflag="search"></CourseTable>
        </div>
    </div>
</template>

<script type="text/ecmascript-6">
    import CourseForm from './CourseForm.vue'
    import CourseTable from './CourseTable.vue'
    export default {
        data () {
            return {

            }
        },

        components: {
            CourseForm: CourseForm,
            CourseTable: CourseTable
        },

        computed: {
            search(){
                return this.$store.state.course.courseQueryFlag;
            }
        }
    }
</script>

<style>

</style>
