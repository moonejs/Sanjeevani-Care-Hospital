<script setup>
import { ref, computed,reactive, capitalize } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth.store';
import { usePatientStore } from '@/stores/patient.store';
import { useField } from '@/reusable/useField';
import { required,minLength, maxLength,postive,maxValue } from "@/utils/validators"
import { useFormValidation } from '@/reusable/useFormValidation';

import BaseInput from "@/components/Form/BaseInput.vue"
import BaseLabel from "@/components/Form/BaseLabel.vue"
import BaseTextarea from "@/components/Form/BaseTextarea.vue"
import Btn from "@/components/common/Btn.vue"

const loading=ref(false)
const router=useRouter()
const auth=useAuthStore()
const patientStore=usePatientStore()

const form = reactive({
  name: "",
  age: "",
  gender: "",
  contact: "",
  address: "",
  height_cm: "",
  weight_kg: "",
  blood_group: "",
  emergency_contact_name: "",
  emergency_contact_number: "",
  profile_image: null
})

const nameField = useField( computed(() => form.name),[required(), minLength(3),maxLength(40)])
const ageField = useField(computed(() => form.age),[required(),postive("Age must be postive"),maxValue(120,"Please enter a valid age.")])
const contactField = useField(computed(()=> form.contact),[postive("Please enter a valid Phone Number"),minLength(10,"Please enter a valid Phone Number"),maxLength(10,"Please enter a valid Phone Number")])
const addressField = useField(computed(() => form.address),[required(), minLength(8,"Address Length must be greater then 8")])
const heightField = useField(computed(() => form.height_cm),[postive("Please Enter a valid Height"), minLength(2,"Please Enter a valid Height"),maxLength(3,"Please Enter a valid Height")])
const weightField = useField(computed(() => form.weight_kg),[postive("Please Enter a valid Weight"), minLength(2,"Please Enter a valid Weight"),maxLength(3,"Please Enter a valid Weight")])
const emgNameField = useField( computed(() => form.emergency_contact_name),[required(), minLength(3),maxLength(40)])
const emgContactField = useField(computed(()=> form.emergency_contact_number),[postive("Please enter a valid Phone Number"),minLength(10,"Please enter a valid Phone Number"),maxLength(10,"Please enter a valid Phone Number")])

const { isValid } = useFormValidation({
  fields: [nameField, ageField, contactField, addressField,heightField,weightField,contactField,emgContactField,emgNameField],
  requiredValues: [
    computed(() => form.gender)
  ],
  loading: computed(() => loading.value)
})




function onImageChange(e) {
  const file = e.target.files[0]
  if (!file) return
  form.profile_image = file
}

async function submitForm() {
    const formData= new FormData()

    Object.entries(form).forEach(([k,v])=>{
        if(v){
            formData.append(k,v)
        }
    })

  try {
    loading.value = true
    await patientStore.updatepatientProfile(formData)
    await auth.fetchMe()
    router.push("/patient/dashboard")
  } finally {
    loading.value = false
  }
}




</script>

<template>
<div class="container mt-4">
    <h4>Edit Profile</h4>

    <div class="row">
      <div class="col-3">
        <BaseLabel label="Full Name" :required="true" />
        <BaseInput v-model.capitalize.trim="form.name":error="nameField.error.value":valid="nameField.valid.value":show="nameField.show.value" placeholder="Chintu Kumar" />
      </div>

      <div class="col-2">
        <BaseLabel label="Age" :required="true" />
        <BaseInput type="Number" v-model.trim="form.age" :error="ageField.error.value" :valid="ageField.valid.value" :show="ageField.show.value" placeholder="25"/>
      </div>
        <div class="col-3">
            <BaseLabel label="Height" />
            <BaseInput type="Number" v-model.trim="form.height_cm" :error="heightField.error.value" :valid="heightField.valid.value" :show="heightField.show.value" placeholder="130" group="cm" :end="true"/>
        </div>
        <div class="col-3">
            <BaseLabel label="Weight" />
            <BaseInput type="Number" v-model.trim="form.weight_kg" :error="weightField.error.value" :valid="weightField.valid.value" :show="weightField.show.value" placeholder="50" group="kg" :end="true"/>
        </div>
        
    </div>

    <div class="row mt-3">
        <div class="col-3">
            <BaseLabel label="Blood Group" />
            <select class="form-select" v-model.trim="form.blood_group">
                <option value="">Select Blood Group</option>
                <option value="A+">A+</option>
                <option value="A-">A-</option>
                <option value="B+">B+</option>
                <option value="B-">B-</option>
                <option value="AB+">AB+</option>
                <option value="AB-">AB-</option>
                <option value="O+">O+</option>
                <option value="O-">O-</option>
            </select>
        </div>
      <div class="col-3">
        <BaseLabel label="Contact" />
        <BaseInput type="Number" v-model.trim="form.contact" placeholder="012-345-6789" group="+91" :start="true" :error=" contactField.error.value" :valid=" contactField.valid.value" :show="contactField.show.value"/>
      </div>
      
    </div>

    <div class="row mt-3">
        <div class="mt-3 col-2">
            <BaseLabel label="Gender" :required="true" />
            <div class="form-check">
                <input class="form-check-input" type="radio" name="gender" id="male" value="male" v-model.trim="form.gender">
                <BaseLabel label="Male" for="male"/>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="gender" id="female" value="female" v-model.trim="form.gender">
                <BaseLabel label="Female" for="female"/>
                
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="gender" id="other" value="other" v-model.trim="form.gender">
                <BaseLabel label="Other" for="other"/>
            </div>
      </div>
      <div class="col">
        <BaseLabel label="Address" :required="true" />
        <BaseTextarea v-model.trim="form.address"
          :error="addressField.error.value"
          :valid="addressField.valid.value"
          :show="addressField.show.value" />
      </div>
    </div>

    <div class="row mt-3">
      <div class="col-3">
        <BaseLabel label="Profile Photo" />
        <input type="file" class="form-control" @change="onImageChange" />
      </div>
      <div class="col-3">
        <BaseLabel label="Emergency Contact Details"/>
        <div>
            <BaseLabel label="Name" class="mt-3"/>
            <BaseInput v-model.capitalize.trim="form.emergency_contact_name":error="emgNameField.error.value":valid="emgNameField.valid.value":show="emgNameField.show.value" placeholder="Banti Kumar" />
        </div>
      </div>
      <div class="col-3 mt-4">
        <div>
            <BaseLabel label="Contact" class="mt-3"/>
            <BaseInput v-model.trim="form.emergency_contact_number":error="emgContactField.error.value":valid="emgContactField.valid.value":show="emgContactField.show.value" placeholder="012-345-6789" group="+91" :start="true" />
        </div>
      </div>
    </div>

    <Btn class="btn btn-primary mt-4"
      :disabled="!isValid"
      @click="submitForm"
      label="Update Profile" />
  </div>
    
</template>