<script setup>
  import { reactive,computed,ref } from "vue"
  import { useDoctorStore } from "@/stores/doctor.store"
  import BaseInput from "@/components/Form/BaseInput.vue"
  import BaseLabel from "@/components/Form/BaseLabel.vue"
  import Btn from "@/components/common/Btn.vue"

  import { useField } from '@/reusable/useField';
  import { required,minLength, maxLength,hasAlpha } from "@/utils/validators"
  import { useFormValidation } from '@/reusable/useFormValidation';

  


  const store = useDoctorStore()
  const loading=ref(false)
  const form = reactive({
    registration_number: store.doctorProfile?.registration_number
  })

  const registrationField = useField(computed(() => form.registration_number),[required(),minLength(13,"Invalid Registration Number"),maxLength(13,"Invalid Registration Number"),hasAlpha("HMS","Invalid Registration Number")])

  const { isValid } = useFormValidation({
    fields: [registrationField],
    loading: computed(() => loading.value)
  })

  async function save() {
    const fd = new FormData()
    fd.append("registration_number", form.registration_number)
    await store.updateDoctorProfile(fd)
  }
</script>

<template>
  <div class="row ">
    <div class="col-4">
      <h6><BaseLabel label=" Medical Registration Number" :required="true"/></h6>
      <BaseInput  v-model.trim="form.registration_number" :error="registrationField.error.value" :valid="registrationField.valid.value" :show="registrationField.show.value" placeholder="HMS123456..." />
      <Btn class="btn btn-primary mt-3" label="Save" :disabled="!isValid" @click="save" />
    </div>
  </div>
</template>
