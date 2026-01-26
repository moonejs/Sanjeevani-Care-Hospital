<script setup>
    import { ref, reactive, computed, onMounted, capitalize } from "vue"
    import { useRouter } from "vue-router"
    import { useDoctorStore } from "@/stores/doctor.store";
    import { useDepartmentStore } from "@/stores/department.store";
    import { useField } from "@/reusable/useField"
    import { required, minLength, maxLength,specialChar,hasCapital,hasDigit } from "@/utils/validators"
    import { useFormValidation } from "@/reusable/useFormValidation"

    import BaseInput from "@/components/Form/BaseInput.vue"
    import BaseLabel from "@/components/Form/BaseLabel.vue"
    import Btn from "@/components/common/Btn.vue"

    const router = useRouter()
    const department = useDepartmentStore()
    const doctor = useDoctorStore()
    const loading = ref(false)

    const form = reactive({
        email: "",
        password: "",
        name: "",
        specialization: "",
        department_id: "",
        roles: [] 
    })
    const emailField = useField(computed(() => form.email), [required(),minLength(3),maxLength(20)])
    const passwordField = useField(computed(() => form.password), [required(), minLength(6),specialChar(),hasCapital(),hasDigit(),maxLength(20)])
    const nameField = useField(computed(() => form.name), [required(), minLength(3)])
    const specializationField = useField(computed(() => form.specialization), [required()])

    const { isValid } = useFormValidation({
        fields: [emailField, passwordField, nameField, specializationField],
        requiredValues: [
            computed(() => form.department_id),
            computed(() => form.roles.length)
        ],
        loading: computed(() => loading.value)
    })

    onMounted(async () => {
        await department.fetchDepartments()
    })


    async function submitForm() {
        await doctor.addDoctor({...form})
    }


</script>

<template>
  <div class="container mt-4">
    <h4>Add Doctor</h4>

    <div class="row">
      <div class="col-4">
        <BaseLabel label="Email" :required="true" />
        <BaseInput v-model.trim="form.email" :error="emailField.error.value" :valid="emailField.valid.value" :show="emailField.show.value" placeholder="doctor" group="@hospital.com" :end="true" />
      </div>

      <div class="col-4">
        <BaseLabel label="Password" :required="true" />
        <BaseInput type="password" v-model="form.password" :error="passwordField.error.value" :valid="passwordField.valid.value" :show="passwordField.show.value" />
      </div>
    </div>

    <div class="row mt-3">
      <div class="col-4">
        <BaseLabel label="Full Name" :required="true" />
        <BaseInput v-model.capitalize.trim="form.name" :error="nameField.error.value" :valid="nameField.valid.value" :show="nameField.show.value" placeholder="Aman Verma" group="Dr." :start="true"/>
      </div>

      <div class="col-4">
        <BaseLabel label="Specialization" :required="true" />
        <BaseInput v-model.capitalize.trim="form.specialization" :error="specializationField.error.value" :valid="specializationField.valid.value" :show="specializationField.show.value" placeholder="Orthopedic" />
      </div>
    </div>

    <div class="row mt-3">
      
      <div class="col-4">
        <BaseLabel label="Department" :required="true" />
        <select class="form-select" v-model="form.department_id">
          <option value="">Select Department</option>
          <option v-for="d in department.departmentList" :key="d.id" :value="d.id">
            {{ d.name }}
          </option>
        </select>
      </div>
    </div>

    <div class="row mt-3">
      <div class="col-6">
        <BaseLabel label="Doctor Role" :required="true" />
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="consultant" id="consultant" v-model="form.roles" />
          <BaseLabel label="Consultant" for="consultant"/>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="surgeon" id="surgeon" v-model="form.roles" />
          <BaseLabel label="Surgeon" for="surgeon"/>
        </div>
      </div>
    </div>

    <Btn class="btn btn-primary mt-4"
      :disabled="!isValid"
      @click="submitForm"
      label="Add Doctor" />
  </div>
</template>
