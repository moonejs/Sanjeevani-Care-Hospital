<script setup>
import { reactive } from "vue"
import { useDoctorStore } from "@/stores/doctor.store"
import BaseInput from "@/components/Form/BaseInput.vue"
import Btn from "@/components/common/Btn.vue"

const store = useDoctorStore()

const form = reactive({
  registration_number: store.doctorProfile?.registration_number
})

async function save() {
  const fd = new FormData()
  fd.append("registration_number", form.registration_number)
  await store.updateDoctorProfile(fd)
}
</script>

<template>
  <div class="card">
    <div class="card-body">
      <h6>Registration</h6>
      <BaseInput label="Medical Registration Number" v-model="form.registration_number" />
      <Btn class="btn btn-primary mt-3" label="Save" @click="save" />
    </div>
  </div>
</template>
