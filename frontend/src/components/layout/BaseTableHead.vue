<script setup>
    defineProps({
        tHead: Array,
        tHeadClasses: {
            type: Array,
            default: () => []
        }
    })
</script>
<template>
    <tr>
        <th class="text-muted" scope="col">#</th>
        <th scope="col" v-for="(h,i) in tHead" :key="i" :class="tHeadClasses[i]" class=" text-muted">{{ h }}</th>
    </tr>
</template>