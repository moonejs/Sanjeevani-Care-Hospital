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
  <div class="list-group list-group-flush gap-4">
    <Btn v-for="s in sections" :key="s.key" :class="`list-group-item list-group-item-action ${section === s.key ? 'active':''}`" :label="s.label" @click="emit('select',s.key)"/>
  </div>
</template>
