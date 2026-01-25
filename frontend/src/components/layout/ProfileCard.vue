<script setup>
    import { departmentIcons } from "@/utils/departmentIcons"
    import { computed ,ref} from "vue";
    const props=defineProps({
        profile:Object,
        type:String
    })
    const icon = computed(() => {
        if (props.type !== "department") return null
        return departmentIcons.find(i => i.key === props.profile?.icon)?.component
    })

    const emit = defineEmits(['select'])
</script>

<template>
    <div class=" custom-card bg-info round d-flex justify-content-center align-items-center animate-up-2" @click="emit('select')" >
        <div v-if="type=='department'" class="">
            
            <component :is="icon" class="custom-card-icon text-primary mt-4" />
            <h5 class="text-center">{{ props.profile.name }}</h5>
        </div>
    </div>
    
</template>