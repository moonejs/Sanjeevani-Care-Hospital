<script setup>
import { useToastStore } from '@/stores/toast.store'

const toastStore = useToastStore()


</script>

<template>
  <div class="toast-container position-fixed start-0 bottom-0 rounded-1 p-3">

    <transition-group name="toast">
      <div v-for="toast in toastStore.toasts" :key="toast.id" class="hms-toast mb-2" :class="toast.type" >

        <div class="toast-header-custom d-flex justify-content-between align-items-center">

          <div class="toast-title">
            {{ toast.title || 'Notification' }}
          </div>

          <div class="d-flex align-items-center gap-2">
            <small class="text-muted">
              Now
            </small>

            <button
              class="btn-close"
              @click="toastStore.removeToast(toast.id)"
            ></button>
          </div>

        </div>

        
        <div class="toast-body-custom">
          {{ toast.message }}
        </div>

      </div>
    </transition-group>

  </div>
</template>

<style scoped>

.hms-toast {
  width: 300px;
  border: 1px solid #e0e0e0;
  border-left: 4px solid transparent;
  box-shadow: 0 2px 4px rgba(60,64,67,.15);
  overflow: hidden;
  font-size: 13px;
  background-color: #F0F2F4;
}


.toast-header-custom {
  padding: 8px 10px;
  border-bottom: 1px solid rgba(0,0,0,0.05);
}

.toast-title {
  font-weight: 600;
  color: #3c4043;
}


.toast-body-custom {
  padding: 10px;
  color: #5f6368;
}


.hms-toast.success {
  border-left-color: #34a853;
}


.hms-toast.error {
  
  border-left-color: #d93025;
}


.hms-toast.warning {
  border-left-color: #f9ab00;
}


.hms-toast.info {
  border-left-color: #1a73e8;
}




.toast-enter-from {
  opacity: 0;
  transform: translateY(30px);
}

.toast-enter-active {
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.toast-enter-to {
  opacity: 1;
  transform: translateY(0);
}


.toast-leave-from {
  opacity: 1;
  transform: translateY(0);
}

.toast-leave-active {
  transition: transform 0.25s ease, opacity 0.25s ease;
  position: absolute;
}

.toast-leave-to {
  opacity: 0;
  transform: translateY(30px); 
}

.toast-move {
  transition: transform 0.25s ease;
}
</style>