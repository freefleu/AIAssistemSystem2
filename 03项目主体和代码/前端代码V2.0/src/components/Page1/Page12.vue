<template>
    <div>
       <!-- <div style="border-radius:5px;">
        <CourseDropForm></CourseDropForm>
        </div>
        <br/> -->
        <div style="border:1px solid;margin-top:5px;background-color:#FFFFFF;border-radius:5px">
            <CourseSelectTable :searchflag="search"></CourseSelectTable>
        </div>

    </div>
</template>

<script type="text/ecmascript-6">
    import CourseSelectTable from './CourseSelectTable.vue'
    import CourseDropForm from './CourseDropForm.vue'
    export default {
        data() {
            return {}
        },


        components: {
            CourseSelectTable: CourseSelectTable,
            CourseDropForm:CourseDropForm
        },


    }
</script>