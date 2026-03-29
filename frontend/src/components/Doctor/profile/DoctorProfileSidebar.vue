<script setup>
  import Btn from '@/components/common/Btn.vue';
    const sections = [
      { key: "personal", label: "Personal & Contact Details" },
      { key: "education", label: "Education & Specialization" },
      { key: "registration", label: "Registration & Documents" },
      { key: "clinics", label: "Clinics (Fees & Timings)" },
    ]
    defineProps({
      section:String
    })
    const emit=defineEmits(['select'])
</script>

<template>
  <div class=" date ">
    <div v-for="s in sections" :key="s.key" :class="`action ${section === s.key ? 'active':''}`" class="pointer py-3 px-2 fw-bold border-bottom" @click="emit('select',s.key)">
      {{ s.label }}
    </div>
  </div>
</template>

<style scoped>
.date :hover{
  background-color: #ECECEC;
}
.active{
  background:#ECECEC;
  border-left:3px solid #242E4C;
}
</style>
