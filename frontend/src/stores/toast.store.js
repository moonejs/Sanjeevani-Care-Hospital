import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useToastStore = defineStore('toast', () => {
    const toasts = ref([])

    function addToast({ message, type = 'info', title = 'Notification' }) {
        const id = Date.now()

        toasts.value.push({
            id,
            message,
            type,
            title,
            createdAt: Date.now()
        })

        
        setTimeout(() => {
            removeToast(id)
        }, 6000)
    }

    function removeToast(id) {
        toasts.value = toasts.value.filter(t => t.id !== id)
    }
    

    return { toasts, addToast, removeToast }
})
