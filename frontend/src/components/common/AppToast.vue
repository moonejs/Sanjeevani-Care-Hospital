<script setup>
import { useToastStore } from '@/stores/toast.store'

const toastStore = useToastStore()

function getTimeAgo(timestamp) {
  const now = Date.now()
  const diff = Math.floor((now - timestamp) / 1000)

  if (diff < 5) return 'just now'
  if (diff < 60) return `${diff}s ago`
  if (diff < 3600) return `${Math.floor(diff / 60)}m ago`

  return `${Math.floor(diff / 3600)}h ago`
}
</script>

<template>
  <div class="toast-container position-fixed top-0 end-0 p-3">

    <transition-group name="toast">
      <div
        v-for="toast in toastStore.toasts"
        :key="toast.id"
        class="hms-toast mb-2"
        :class="toast.type"
      >

        
        <div class="toast-header-custom d-flex justify-content-between align-items-center">

          <div class="toast-title">
            {{ toast.title || 'Notification' }}
          </div>

          <div class="d-flex align-items-center gap-2">
            <small class="text-muted">
              {{ getTimeAgo(toast.createdAt) }}
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
  border-radius: 6px;
  border: 1px solid #e0e0e0;
  border-left: 4px solid transparent;
  box-shadow: 0 2px 4px rgba(60,64,67,.15);
  overflow: hidden;
  font-size: 13px;
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
  background: #e6f4ea;
  border-left-color: #34a853;
}


.hms-toast.error {
  background: #fce8e6;
  border-left-color: #d93025;
}


.hms-toast.warning {
  background: #fef7e0;
  border-left-color: #f9ab00;
}


.hms-toast.info {
  background: #e8f0fe;
  border-left-color: #1a73e8;
}



.toast-enter-from {
  opacity: 0;
  transform: translateY(-10px);
}

.toast-enter-active {
  transition: all 0.25s ease;
}

.toast-enter-to {
  opacity: 1;
  transform: translateY(0);
}

.toast-leave-from {
  opacity: 1;
}

.toast-leave-active {
  transition: all 0.2s ease;
  position: absolute;
}

.toast-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

.toast-move {
  transition: transform 0.2s ease;
}
</style>