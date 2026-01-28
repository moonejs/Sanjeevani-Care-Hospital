<script setup>
  import { reactive, watch, ref, computed } from "vue"
  import { useDoctorStore } from "@/stores/doctor.store"

  import BaseInput from "@/components/Form/BaseInput.vue"
  import BaseLabel from "@/components/Form/BaseLabel.vue"
  import BaseCheckbox from "@/components/Form/BaseCheckbox.vue"
  import Btn from "@/components/common/Btn.vue"

  import { useField } from "@/reusable/useField"
  import { required, minLength, postive } from "@/utils/validators"
  import { useFormValidation } from "@/reusable/useFormValidation"

  const doctorStore = useDoctorStore()
  const loading = ref(false)

  const form = reactive({
    opd_timing: "",
    room_number: "",
    consultation_fee: "",
    emergency_available: false
  })

  
  watch(() => doctorStore.doctorProfile,(d) => {
      if (!d) return
      form.opd_timing = d.opd_timing || ""
      form.room_number = d.room_number || ""
      form.consultation_fee = d.consultation_fee || ""
      form.emergency_available = !!d.emergency_available
    },{ immediate: true })

  
  const opdField = useField(computed(() => form.opd_timing),[required("OPD timing is required"), minLength(10)])

  const roomField = useField(computed(() => form.room_number),[required("Room number is required")])

  const feeField = useField(computed(() => form.consultation_fee),[required("Consultation fee required"), postive("Fee must be positive")])

  const { isValid } = useFormValidation({
    fields: [opdField, roomField, feeField],
    loading: computed(() => loading.value)
  })

  
  async function save() {
    const fd = new FormData()

    fd.append("opd_timing", form.opd_timing)
    fd.append("room_number", form.room_number)
    fd.append("consultation_fee", form.consultation_fee)
    fd.append("emergency_available",form.emergency_available ? "true" : "false")

    loading.value = true
    try {
      await doctorStore.updateDoctorProfile(fd)
    } finally {
      loading.value = false
    }
  }
</script>
<template>
  <div class="card">
    <div class="card-body">

      <h3 class="mb-2">Clinic & Consultation</h3>
      <p class="text-muted mb-4">
        Set your availability, consultation fees, and clinic details.
      </p>

      
      <div class="row mb-3">
        <div class="col-6">
          <BaseLabel label="OPD Timing" required />
          <BaseInput v-model.trim="form.opd_timing" placeholder="Mon - Sat | 10:00 AM - 4:00 PM" :error="opdField.error.value" :valid="opdField.valid.value" :show="opdField.show.value"/>
        </div>
      </div>

      <div class="row mb-3">
        <div class="col-4">
          <BaseLabel label="Room Number" required />
          <BaseInput v-model.trim="form.room_number" placeholder="Room 203 / OPD-5" :error="roomField.error.value" :valid="roomField.valid.value" :show="roomField.show.value"
          />
        </div>

        <div class="col-4">
          <BaseLabel label="Consultation Fee (₹)" required />
          <BaseInput type="number" v-model.trim="form.consultation_fee" placeholder="500" :error="feeField.error.value" :valid="feeField.valid.value" :show="feeField.show.value"
          />
        </div>
      </div>

      <div class="row mb-3">
        <div class="col-6 d-flex align-items-center gap-2">
          <BaseCheckbox v-model="form.emergency_available" id="emergency" />
          <BaseLabel for="emergency" label="Available for Emergency Consultation" />
        </div>
      </div>

      <div class="alert alert-info">
        Emergency availability helps patients know if you can be contacted outside OPD hours.
      </div>

    
      <Btn class="btn btn-primary mt-4" label="Save Clinic Details" :disabled="!isValid" :loading="loading" @click="save"
      />

    </div>
  </div>
</template>
