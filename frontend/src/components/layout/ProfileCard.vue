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
  <div 
    class=" department-card h-100  rounded-1 shadow-sm animate-up-2"
    @click="emit('select')"
  >
    <div class="card-body text-center">
      <div class="icon-wrapper mb-3">
        <component  :is="icon"  class="text-primary" style="width: 32px; height: 32px;"/>
      </div>

      <h6 class="fw-semibold mb-1">
        {{ props.profile.name }}
      </h6>

    </div>
  </div>
</template>

<style scoped>
.department-card {
  cursor: pointer;
  background-color: #f0f2f4;
  border-left: 4px solid #151616;
  transition: all 0.2s ease;
}



.icon-wrapper {
  width: 56px;
  height: 56px;
  
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
}
</style>