<script setup>
  import { reactive, watch ,ref,computed} from "vue"
  import { useDoctorStore } from "@/stores/doctor.store"
  
  import BaseInput from "@/components/Form/BaseInput.vue"
  import BaseLabel from "@/components/Form/BaseLabel.vue"
  import BaseTextarea from "@/components/Form/BaseTextarea.vue"
  import Btn from "@/components/common/Btn.vue"

  import { useField } from '@/reusable/useField';
  import { required,minLength, maxLength,postive,maxValue } from "@/utils/validators"
  import { useFormValidation } from '@/reusable/useFormValidation';

  const doctorStore = useDoctorStore()
  const loading=ref(false)

  const form = reactive({
    name: "",
    age: "",
    gender: "",
    contact: "",
    bio: "",
    languages_spoken: [],
    profile_image: null,
    profile_image_url: null
  })

  
  const ageField = useField(computed(() => form.age),[required(),postive("Age must be postive"),maxValue(120,"Please enter a valid age.")])
  const contactField = useField(computed(()=> form.contact),[postive("Please enter a valid Phone Number"),minLength(10,"Please enter a valid Phone Number"),maxLength(10,"Please enter a valid Phone Number")])
  const bioField = useField(computed(()=> form.bio),[required(),minLength(10)])


  const { isValid } = useFormValidation({
    fields: [ageField,contactField,bioField],
    requiredValues: [
      computed(() => form.gender)
    ],
    loading: computed(() => loading.value)
  })

  watch(() => doctorStore.doctorProfile,(d) => {
      if (!d) return
      form.name = d.name
      form.contact = d.contact
      form.bio = d.bio
      form.profile_image_url = d.profile_image
      form.age=d.age
      form.gender=d.gender
      form.languages_spoken = d.languages_spoken? d.languages_spoken.split(","): []
    },{ immediate: true })

  function onImageChange(e) {
    const file = e.target.files[0]
    if (!file) return
    form.profile_image = file
    form.profile_image_url = URL.createObjectURL(file)
  }

  async function submitForm() {
    const formData= new FormData()

    Object.entries(form).forEach(([k, v]) => {
      if (k === "languages_spoken") {
        formData.append(k, v.join(","))   
      } else if (v !== null && v !== undefined && k !== "profile_image_url") {
        formData.append(k, v)
      }
    })

  try {
    loading.value = true
    await doctorStore.updateDoctorProfile(formData)
    
  } finally {
    loading.value = false
  }
}
</script>
<template>

<div class="">

  <div class="d">

    <h4 class="mb-4">
      Personal Details
    </h4>

      <div class="row">
        <div class="col-4">
          <BaseLabel label="Full Name" :required="true" />
          <BaseInput  v-model="form.name" group="Dr " :start="true" disabled
          />
        </div>

        <div class="col-2">
          <BaseLabel label="Age" :required="true" />
          <BaseInput type="number" v-model.trim="form.age" :error="ageField.error.value" :valid="ageField.valid.value" :show="ageField.show.value" placeholder="25"
          />
        </div>

        <div class="col-3">
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
        <div class=" doctor-profile-img ">
              <img v-if="form.profile_image_url" :src="form.profile_image_url" class="img-thumbnail rounded-0 border-0 mb-2"  alt="...">
        </div>
        
      </div>
      <div class="row mt-3">
        <div class="col-8">
          <BaseLabel label="About me" :required="true" />
          <BaseTextarea  v-model="form.bio" :rows="6" :error="bioField.error.value" :valid="bioField.valid.value" :show="bioField.show.value" placeholder="Write a short professional introduction about yourself"
          />
        </div>
        <div class="col-3 ">
          <BaseLabel label="Profile Photo" />
          <input type="file" class="form-control" @change="onImageChange" />
        </div>
      </div>

      <div class="row">
        <div class="col-6">
          <BaseLabel label="Languages Spoken" />
          <span class="font-small"> (use <mark class="font-monospace">ctl</mark> to select multiple Languages )</span>
          <select class="form-select" v-model="form.languages_spoken" multiple>
            <option value="english">English</option>
            <option value="hindi">Hindi</option>
            <option value="spanish">Spanish</option>
            <option value="french">French</option>
            <option value="german">German</option>
            <option value="chinese">Chinese</option>
            <option value="arabic">Arabic</option>
          </select>
        </div>
      </div>
      
      <hr>
      <div class="mt-4">
        <h3>Contact Details</h3>

        <div class="row">
          <div class="col-4">
            <BaseLabel label="Contact" :required="true"/>
            <BaseInput type="Number" v-model.trim="form.contact" placeholder="012-345-6789" group="+91" :start="true" :error=" contactField.error.value" :valid=" contactField.valid.value" :show="contactField.show.value"/>
          </div>
        </div>
      </div>

      
      <div class="mt-4">
        <Btn class="btn btn-secondary mt-4" :disabled="!isValid" @click="submitForm" label="Update Profile" />
      </div>

    </div>
  </div>
</template>

<style scoped>
.doctor-profile-img {
  position: absolute;
  top: 6rem;
  right: 3rem;
  width: fit-content;
}
.d{
  height: 39rem;
  overflow-y: auto;
  overflow-x: hidden;
}
</style>