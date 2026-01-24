<script setup>
    import { ref,computed,reactive } from "vue"
    import { useRouter } from "vue-router"
    import { useDepartmentStore } from "@/stores/department.store"

    import { useField } from "@/reusable/useField"
    import { required,minLength, maxLength } from "@/utils/validators"
    import BaseInput from "@/components/Form/BaseInput.vue"
    import BaseLabel from "@/components/Form/BaseLabel.vue"
    import BaseCheckbox from "@/components/Form/BaseCheckbox.vue"
    import BaseTextarea from "@/components/Form/BaseTextarea.vue"
    import Btn from "@/components/common/Btn.vue"
    import { departmentIcons } from "@/utils/departmentIcons"
    import { useFormValidation } from "@/reusable/useFormValidation"



    const router = useRouter()
    const departmentStore = useDepartmentStore()

    const form = reactive({
        name: "",
        description: "",
        phone: "",
        icon:"",
        email: "",
        building: "",
        floor: "",
        opd_timing: "",
        emergency_available: false,
        servicesText: "",
        facilitiesText: ""
    })

    const selectedIconComponent = computed(() => {
      return departmentIcons.find(i => i.key === form.icon)?.component
    })

    
    
    const nameField = useField( computed(() => form.name),[required(), minLength(3),maxLength(25)])
    const descriptionField = useField( computed(() => form.description), [required(),minLength(50)])
    const phoneField = useField(computed(()=> form.phone),[minLength(10),maxLength(10)])
    const emailField = useField(computed(()=> form.email),[minLength(5),maxLength(27)])
    



    async function submitForm() {

        const data = {
            name: form.name,
            description: form.description,
            icon:form.icon,
            phone: form.phone,
            email: `${form.email}@hospital.com`,
            building: form.building,
            floor: form.floor,
            opd_timing: form.opd_timing,
            emergency_available: form.emergency_available,
            services: form.servicesText.split("\n").map(s => s.trim()).filter(Boolean),
            facilities: form.facilitiesText.split("\n").map(f => f.trim()).filter(Boolean)
        }

        await departmentStore.addDepartment(data)
        router.push("/admin/departments")
    }

    const { isValid } = useFormValidation({fields: [nameField, descriptionField],
      requiredValues: [
        computed(() => form.icon)
      ],
      loading: computed(() => departmentStore.loading)
    })

</script>
<template>
  <div class="container-fluid mt-4">
    <h4>Add Department</h4>
    <div class="row">
      <div class="col-4">
        <BaseLabel label="Department Name" :required="true" />
        <BaseInput v-model="form.name" placeholder="Department name"  :error=" nameField.error.value" :valid=" nameField.valid.value" :show="nameField.show.value" required="required"/>
      </div>
      <div class="col-2">
        <BaseLabel label="Department Icon" :required="true"/>
        <select v-model="form.icon" class="form-select" required>
            <option disabled value="">
              Select a department icon
            </option>
            <option v-for="icon in departmentIcons" :key="icon.key" :value="icon.key">
              {{ icon.label }}
            </option>
        </select>
      </div>
      <div class="col-2">
        <component :is="selectedIconComponent" class="text-primary mt-4" style="width:32px;height:32px"/>

      </div>
      <div class="col-3">
        <BaseLabel label="OPD Timing" />
        <BaseInput v-model="form.opd_timing" placeholder="Mon - Sat | 9:00 AM - 5:00 PM"
        />
      </div>
    </div>

    <div class="row">
      <div class="col">
        <BaseLabel label="Description" :required="true" />
        <BaseTextarea v-model="form.description" placeholder="Department description" :error="descriptionField.error.value " :valid="descriptionField.valid.value" :show="descriptionField.show.value"/>
      </div>
       <div class="col">
        <BaseLabel label="Services (one per line)" />
        <BaseTextarea v-model="form.servicesText" />
      </div>
    </div>

    <div class="row">
      <div class="col-6">
        <BaseLabel label="Facilities (one per line)" />
        <BaseTextarea v-model="form.facilitiesText" />
      </div>
      <div class="col-3 ">
        <BaseLabel label="Phone" />
        <BaseInput type="Number" v-model="form.phone" placeholder="012-345-6789" group="+91" :start="true" :error=" phoneField.error.value" :valid=" phoneField.valid.value" :show="phoneField.show.value"/>
      </div>
      <div class="col-3">
        <BaseLabel label="Email" />
        <BaseInput  group="@hospital.com" :end="true" v-model="form.email" placeholder="Department"
        :error=" emailField.error.value" :valid="emailField.valid.value" :show="emailField.show.value" />
      </div>
    </div>


    <div class="row">
      <div class="col-3">
        <BaseLabel label="Building" />
        <BaseInput v-model="form.building"/>
      </div>
      <div class="col-2">
        <BaseLabel label="Floor" />
        <BaseInput type="Number" v-model="form.floor" group="Floor" :end="true" placeholder="2"/>
      </div>
      <div class="col-3">
        <BaseCheckbox v-model="form.emergency_available" id="emergency"/>
        <BaseLabel label="Emergency Available" for="emergency" />
      </div>
    </div>
    

    <Btn class="btn btn-primary mt-3" :disabled="!isValid" @click="submitForm" label="Save Department"
    />
      
  </div>
</template>
