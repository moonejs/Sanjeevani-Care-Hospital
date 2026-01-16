<script setup>
    defineProps({
        tHead:Array
    })
</script>
<template>
    <tr>
        <th scope="col">S No.</th>
        <th scope="col" v-for="(h,i) in tHead" :key="i">{{ h }}</th>
    </tr>
</template>