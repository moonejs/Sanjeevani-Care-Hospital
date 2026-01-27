<script setup>
import { reactive } from "vue"
import { useDoctorStore } from "@/stores/doctor.store"
import BaseInput from "@/components/Form/BaseInput.vue"
import BaseCheckbox from "@/components/Form/BaseCheckbox.vue"
import Btn from "@/components/common/Btn.vue"

const store = useDoctorStore()

const form = reactive({
  opd_timing: store.doctorProfile?.opd_timing,
  emergency_available: store.doctorProfile?.emergency_available,
  room_number: store.doctorProfile?.room_number
})

async function save() {
  const fd = new FormData()
  Object.entries(form).forEach(([k, v]) => fd.append(k, v))
  await store.updateDoctorProfile(fd)
}
</script>

<template>
  <div class="card">
    <div class="card-body">
      <h6>Clinic & Timings</h6>
      <BaseInput label="OPD Timing" v-model="form.opd_timing" />
      <BaseInput label="Room Number" v-model="form.room_number" />
      <BaseCheckbox v-model="form.emergency_available" /> Emergency Available
      <Btn class="btn btn-primary mt-3" label="Save" @click="save" />
    </div>
  </div>
</template>
