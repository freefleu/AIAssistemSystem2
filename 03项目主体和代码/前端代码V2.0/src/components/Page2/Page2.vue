<template>
    <div>
        <div style="border:1px solid;margin-top:5px;background-color:#FFFFFF;border-radius:5px">
            <GroupJoin></GroupJoin>
        </div>
        <br/>

        <div style="border-radius:5px;">
            <GroupFound></GroupFound>
        </div>
    </div>
</template>
<script type="text/ecmascript-6">
    import GroupJoin from './GroupJoin.vue'
    import GroupFound from'./GroupFound.vue'
    export default {
        data() {
            return {}
        },

        components: {
            GroupJoin: GroupJoin,
            GroupFound:GroupFound
        }
    }
</script>