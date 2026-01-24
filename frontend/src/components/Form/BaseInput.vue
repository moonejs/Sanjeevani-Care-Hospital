<script setup>
import { required } from '@/utils/validators';

  defineProps({
    id: String,
    type: { type: String, default: "text" },
    placeholder: String,
    disabled: Boolean,
    error: String,
    valid: Boolean,
    show:Boolean,
    required:String,
    group:String,
    start:Boolean,
    end:Boolean
  })

  const model = defineModel()
</script>

<template>
  <div class="input-group">
    <span class="input-group-text" v-if="group && start">{{ group }}</span>
    <input :id="id" :type="type" v-model="model" :placeholder="placeholder" required="required
    " :disabled="disabled" class="form-control" :class="{
        'is-invalid': show && error,
        'is-valid': show && valid
      }"/>
    <span class="input-group-text" v-if="group && end">{{ group }}</span>

    <div v-if="show && error " class="invalid-feedback">
      {{ error }}
    </div>

    <div v-if="show && valid" class="valid-feedback">
      Looks good
    </div>
  </div>
</template>
