import { defineStore } from 'pinia'
import { ref, computed ,watch} from 'vue'
import { fetchAdminDashboardDetailsApi } from '@/api/admin'


export const useAdminStore=defineStore('admin',()=>{
    const loading = ref(false)
    const error = ref(null)
    const appointmentSummary = ref({pending: 0, confirmed: 0, completed: 0, cancelled: 0})

    const dashboard = ref({
        stats: {},
        upcoming_appointments: [],
        status_summary: {},
        recent_activity: []
    })

    const selectedRange = ref("today")
    async function fetchAdminDashboardDetails(range = "today") {
        loading.value = true
        error.value = null

        try {
            selectedRange.value = range
            const res = await fetchAdminDashboardDetailsApi(range)
            dashboard.value = res.data
            appointmentSummary.value=res.data.status_summary
            console.log(res);
            
        } catch (err) {
            error.value = err
            console.error("Dashboard fetch failed:", err)
        } finally {
            loading.value = false
        }
    }
    return {
        loading,
        error,
        dashboard,
        selectedRange,
        fetchAdminDashboardDetails,
        appointmentSummary
    }

})