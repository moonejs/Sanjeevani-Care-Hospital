<script setup>
    import { ref, onMounted, onUnmounted, computed } from 'vue'

    const now = ref(new Date())
    let timer = null
    onMounted(()=>{
        timer=setInterval(()=>{
            now.value=new Date()
        },1000)
    })
    
    onUnmounted(()=>{
        clearInterval(timer)
    })

    const formattedDate=computed(()=>{
        return now.value.toLocaleDateString('en-In',{
            weekday: 'long',
            day: 'numeric',
            month: 'short',
            year: 'numeric'
        })
    })
    const formattedTime = computed(()=>{
        return now.value.toLocaleTimeString('en-In',{
            hour: 'numeric',
            minute: '2-digit',
            second: '2-digit',
            hour12: true
        })
    })
    


</script>

<!-- <template>
  <div class="bg-info time">
      <h4>{{ formattedTime }}</h4>
    <h4>{{ formattedDate }}</h4>
    
  </div>
</template> -->

<template>
  <div class="time-container text-end">
    <div class="d-flex align-items-center justify-content-end gap-2">
        <span class="pulse-dot"></span>
        <h4 class="time-display m-0">{{ formattedTime }}</h4>
    </div>
    <div class="date-display text-muted small fw-medium">
        {{ formattedDate }}
    </div>
  </div>
</template>

<style scoped>
.time-container {
    padding: 0.5rem;
}

.time-display {
    font-weight: 700;
    color: var(--hms-text-main);
    letter-spacing: -0.5px;
    font-size: 1.25rem;
}

.date-display {
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-size: 0.75rem;
}

/* Subtle animation to show the dashboard is live */
.pulse-dot {
  height: 8px;
  width: 8px;
  background-color: #34a853; /* Google Green */
  border-radius: 50%;
  display: inline-block;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { opacity: 1; }
  50% { opacity: 0.4; }
  100% { opacity: 1; }
}
</style>