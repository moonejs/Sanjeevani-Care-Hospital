<script setup>
  import { capitalize, reactive, ref, watch } from "vue"
  import { useDoctorStore } from "@/stores/doctor.store"

  import BaseInput from "@/components/Form/BaseInput.vue"
  import BaseLabel from "@/components/Form/BaseLabel.vue"
  import Btn from "@/components/common/Btn.vue"
  import Badge from "@/components/common/Badge.vue"

  import { useField } from '@/reusable/useField';
  import { required,minLength, maxLength,postive,maxValue } from "@/utils/validators"
  import { useFormValidation } from '@/reusable/useFormValidation';

  const doctorStore = useDoctorStore()


  const form = reactive({
    education: [
      { degree: "", institution: "", year: "" }
    ],
    specializations: []
  })

  const newSpecialization = ref("")

  watch(() => doctorStore.doctorProfile,(d) => {
      if (!d) return

      if (d.qualification) {
        try {
          form.education = JSON.parse(d.qualification)
        } catch {
          form.education = [{ degree: "", institution: "", year: "" }]
        }
      }

      form.specializations = d.specialization
        ? d.specialization.split(",")
        : []
    },
    { immediate: true }
  )

  function addEducation() {
    form.education.push({ degree: "", institution: "", year: "" })
  }

  function removeEducation(index) {
    if (form.education.length > 1) {
      form.education.splice(index, 1)
    }
  }

  function addSpecialization() {
    const value = newSpecialization.value.trim()
    if (!value) return
    if (!form.specializations.includes(value)) {
      form.specializations.push(value)
    }
    newSpecialization.value = ""
  }

  function removeSpecialization(index) {
    form.specializations.splice(index, 1)
  }


  async function save() {
    const fd = new FormData()
    fd.append("qualification", JSON.stringify(form.education))
    fd.append("specialization", form.specializations.join(","))

    await doctorStore.updateDoctorProfile(fd)
  }
</script>

<template>
  <div class="card">
    <div class="card-body">

      <h3 class="mb-3">Education and Specializations</h3>

      <div v-for="(edu, index) in form.education" :key="index" class="border rounded p-3 mb-3"
      >
        <div class="row">
          <div class="col-4">
            <BaseLabel label="Degree" />
            <BaseInput v-model.trim="edu.degree" placeholder="MBBS"  />
          </div>

          <div class="col-4">
            <BaseLabel label="Institution" />
            <BaseInput v-model.capitalize.trim="edu.institution" placeholder="AIIMS Delhi" />
          </div>

          <div class="col-2">
            <BaseLabel label="Year" />
            <BaseInput type="number" v-model.trim="edu.year" placeholder="2016" />
          </div>

          <div class="col-2 d-flex align-items-end">
            <Btn v-if="form.education.length > 1" class="btn btn-outline-danger" label="Remove" @click="removeEducation(index)"
            />
          </div>
        </div>
      </div>

      <Btn class="btn btn-outline-primary mb-4" @click="addEducation" label="+ Add Education"/>
      
      <hr>
      <h5 class="mt-4  me-2 d-inline">Specializations</h5>
      <span class="font-small" >(Add specialization and press <mark class="font-monospace">Enter</mark> )</span>

      <div class="d-flex flex-wrap mt-2 gap-2 mb-3">
        <Badge v-for="(s, index) in form.specializations" :key="index" :label="s " :cross="true" color="primary" @click="removeSpecialization(index)"/>
        
      </div>

      <BaseInput v-model="newSpecialization" placeholder="Add specialization and press Enter" @keyup.enter="addSpecialization"
      />

     
      <Btn
        class="btn btn-primary mt-4"
        label="Save Education & Specialization"
        @click="save"
      />

    </div>
  </div>
</template>
