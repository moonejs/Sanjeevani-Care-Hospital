<script setup>
    import Badge from '../common/Badge.vue';
    import { computed } from 'vue';
    const props=defineProps({
        doctor: {
            type: Object,
            required: true
        }
    })
    const bookable=computed(()=>{
            return props.doctor.is_bookable
    })
    const emit=defineEmits(['select'])
</script>

<template>
  <div class="doctor-row border-bottom " @click="emit('select')">
    <img :src="doctor.profile_image || '/doctor-placeholder.png'" class="avatar" />

    <div class="flex-grow-1">
      <div class="fw-medium">
        Dr. {{ doctor.name }}
      </div>
      <div class="text-muted tiny">
        {{ doctor.specialization }}
      </div>
    </div>

    <Badge :label="bookable ? 'Open' : 'Closed'" :color="bookable ? 'success' : 'danger'"/>
    
  </div>
</template>

<style scoped>
.doctor-row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 0;
  cursor: pointer;
  border-bottom: 1px solid #f1f5f9;
  transition: background 0.15s ease;
} 
.doctor-row:hover {
  background: var(--hms-card-hover);
}

.avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
}
</style>