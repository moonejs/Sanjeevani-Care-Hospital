<script setup>
import { required } from '@/utils/validators';

  defineProps({
    id: String,
    placeholder: String,
    disabled: Boolean,
    error: String,
    valid: Boolean,
    rows: {
      type: Number,
      default: 4
    },
    show:Boolean,
    required:String
  })

  const model = defineModel()
</script>

<template>
  <div>
    <textarea :id="id" v-model="model" :placeholder="placeholder" :disabled="disabled" required="required" :rows="rows" class="form-control" :class="{
        'is-invalid': show && error,
        'is-valid': show && valid
      }"
    ></textarea>

    <div v-if="show && error" class="invalid-feedback">
      {{ error }}
    </div>

    <div v-if="show && valid" class="valid-feedback">
      Looks good
    </div>
  </div>
</template>
