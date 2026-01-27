<script setup>
import { reactive } from "vue"
import { useDoctorStore } from "@/stores/doctor.store"
import BaseInput from "@/components/Form/BaseInput.vue"
import Btn from "@/components/common/Btn.vue"

const store = useDoctorStore()

const form = reactive({
  qualification: store.doctorProfile?.qualification,
  specialization: store.doctorProfile?.specialization
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
      <h6>Education & Specialization</h6>
      <BaseInput label="Qualification" v-model="form.qualification" />
      <BaseInput label="Specialization" v-model="form.specialization" />
      <Btn class="btn btn-primary mt-3" label="Save" @click="save" />
    </div>
  </div>
</template>
