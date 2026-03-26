<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'

const props = defineProps({
    type: {
        type: String,
        default: 'digital' 
    }
})
const shortDate = computed(() => {
    return now.value.toLocaleDateString('en-IN', {
        weekday: 'short',
        day: 'numeric'
    })
})
const now = ref(new Date())
let timer = null

onMounted(() => {
    timer = setInterval(() => {
        now.value = new Date()
    }, 1000)
})

onUnmounted(() => {
    clearInterval(timer)
})


const formattedDate = computed(() => {
    return now.value.toLocaleDateString('en-IN', {
        weekday: 'long',
        day: 'numeric',
        month: 'short',
        year: 'numeric'
    })
})

const formattedTime = computed(() => {
    return now.value.toLocaleTimeString('en-IN', {
        hour: 'numeric',
        minute: '2-digit',
        second: '2-digit',
        hour12: true
    })
})


const seconds = computed(() => now.value.getSeconds())
const minutes = computed(() => now.value.getMinutes())
const hours = computed(() => now.value.getHours())

const secondDeg = computed(() => seconds.value * 6)
const minuteDeg = computed(() => minutes.value * 6 + seconds.value * 0.1)
const hourDeg = computed(() => (hours.value % 12) * 30 + minutes.value * 0.5)

</script>

<template>


    <div v-if="type === 'digital'" class="time-container text-end">
        <div class="d-flex align-items-center justify-content-end gap-2">
            <span class="pulse-dot"></span>
            <h4 class="time-display m-0">{{ formattedTime }}</h4>
        </div>
        <div class="date-display text-muted small fw-medium">
            {{ formattedDate }}
        </div>
    </div>

    
   <div v-else class="d-flex flex-column align-items-center">

    <div class="analog-clock">
        <div class="hand hour" :style="{ transform: `rotate(${hourDeg}deg)` }"></div>
        <div class="hand minute" :style="{ transform: `rotate(${minuteDeg}deg)` }"></div>
        <div class="hand second" :style="{ transform: `rotate(${secondDeg}deg)` }"></div>
        <div class="center-dot"></div>
    </div>

    
    <div class="analog-date mt-2 text-muted">
        {{ shortDate }}
    </div>

</div>

</template>

<style scoped>

.time-display {
    font-weight: 700;
    letter-spacing: -0.5px;
    font-size: 1.25rem;
}

.date-display {
    text-transform: uppercase;
    font-size: 0.75rem;
}

.pulse-dot {
    height: 8px;
    width: 8px;
    background-color: #34a853;
    border-radius: 50%;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { opacity: 1; }
    50% { opacity: 0.4; }
    100% { opacity: 1; }
}


.analog-clock {
    width: 120px;
    height: 120px;
    border: 6px solid #242E4C;
    border-radius: 50%;
    position: relative;
    background: #fff;
}

.hand {
    position: absolute;
    bottom: 50%;
    left: 50%;
    transform-origin: bottom;
    transform: translateX(-50%);
}

.hour {
    width: 4px;
    height: 30px;
    background: #242E4C;
}

.minute {
    width: 3px;
    height: 40px;
    background: #242E4C;
}

.second {
    width: 2px;
    height: 45px;
    background: red;
}

.center-dot {
    width: 8px;
    height: 8px;
    background: #242E4C;
    border-radius: 50%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

</style>