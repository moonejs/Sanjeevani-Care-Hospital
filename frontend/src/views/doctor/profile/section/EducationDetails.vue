<script setup>
  import {  reactive, ref, watch,computed } from "vue"
  import { useDoctorStore } from "@/stores/doctor.store"

  import BaseInput from "@/components/Form/BaseInput.vue"
  import BaseLabel from "@/components/Form/BaseLabel.vue"
  import Btn from "@/components/common/Btn.vue"
  import Badge from "@/components/common/Badge.vue"



  const doctorStore = useDoctorStore()
  const loading=ref(false)

  const form = reactive({
    education: [
      { degree: "", institution: "", year: "" }
    ],
    specializations: [],
    experience_years:""
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

      form.specializations = d.specialization? d.specialization.split(","): []
      form.experience_years=d.experience_years
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

  const isValid =computed(()=>{
    return form.specializations.length
  })

  async function save() {
    const fd = new FormData()
    fd.append("qualification", JSON.stringify(form.education))
    fd.append("specialization", form.specializations.join(","))
    fd.append("experience_years",form.experience_years)
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
      <div class="row">
        <div class="col-6">
          <h5 class="mt-4  me-2 d-inline">Specializations</h5>

          <span class="font-small" >(Add specialization and press <mark class="font-monospace">Enter</mark> )</span>
        </div>
        <div class="col-6">
          <h5>Year of Experience</h5>
        </div>
      </div>
      <div class="row">
        <div class="col-6">
          
          
          <div class="d-flex flex-wrap mt-2 gap-2 mb-3">
            <Badge v-for="(s, index) in form.specializations" :key="index" :label="s " :cross="true" color="primary" @click="removeSpecialization(index)"/>
            
          </div>
          <small v-if="!form.specializations.length" class="text-danger">
            At least one specialization is required
          </small>
          <BaseInput v-model="newSpecialization" placeholder="Add specialization and press Enter" @keyup.enter="addSpecialization"
          />
        </div>
        
        <div class="col-2 mt-4">
          <BaseInput type="number" v-model.trim="form.experience_years" placeholder="2" group="Year" :end="true"  />
        </div>
      </div>

     
      <Btn class="btn btn-primary mt-4" :disabled="!isValid" label="Save Education & Specialization" @click="save"/>

    </div>
  </div>
</template>
