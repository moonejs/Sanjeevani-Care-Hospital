<script setup>
    import TableNavigaionBox from '../common/TableNavigaionBox.vue';
    defineProps({
        title:String,
        navArray:Array
    })
</script>
<template>
    <div>
        <h1>{{ title }}</h1>
    </div>
    <div>
        <div>
            <TableNavigaionBox :nav-array="navArray"/>
        </div>
        <div>
            
        </div>
    </div>
 
</template>