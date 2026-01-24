import {  computed } from "vue"

export function useField(value, rules = []) {
  const error = computed(() => {
    for (const rule of rules) {
      const msg = rule(value.value)
      if (msg) return msg
    }
    return ""
  })

    const valid = computed(() => !error.value)
    const show = computed(() => !!value.value)

    return {
        error,
        valid,
        show
    }
}
