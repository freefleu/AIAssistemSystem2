<template>
    <div>
        <div style="border:1px solid;margin-top:5px;background-color:#FFFFFF;border-radius:5px">
            <GroupList></GroupList>
        </div>
    </div>
</template>

<script type="text/ecmascript-6">
    import GroupList from './GroupList.vue'
    export default {
        data() {
            return {}
        },

        components: {
            GroupList: GroupList
        }
    }

</script>