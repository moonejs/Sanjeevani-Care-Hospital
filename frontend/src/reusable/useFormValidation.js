import { computed } from "vue"

export function useFormValidation({fields = [],requiredValues = [],loading = null}) {
  const isValid = computed(() => {
    const fieldsValid = fields.every(
      field => !field.error.value
    )

    const valuesPresent = requiredValues.every(
      val => !!val.value
    )

    const notLoading = loading ? !loading.value : true

    return fieldsValid && valuesPresent && notLoading
  })

  return {
    isValid
  }
}
