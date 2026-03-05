<script setup>
    
    import { ref } from 'vue';
    defineProps({
        navArray:Array
    })
    const activeTab = ref('today')
    const emit=defineEmits(['todayOrWeek'])
</script>
<template>
    <div class="nav nav-tabs">
        <li class="nav-item">
            <button class="nav-link rounded-top-1 " :class="{active: activeTab==='today'}"  @click="activeTab='today'; emit('todayOrWeek','today')"  >
                Today
            </button>
            </li>
            <li class="nav-item">
            <button class="nav-link rounded-top-1" :class="{active: activeTab==='week'}" @click="activeTab='week' ; emit('todayOrWeek','week')" >
                This Week
            </button>
        </li>
        
    </div>
</template>

