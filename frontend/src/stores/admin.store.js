import { defineStore } from 'pinia'
import { ref, computed ,watch} from 'vue'
import { fetchAdminDashboardDetailsApi,fetchPatientsApi,blockDoctorApi,unblockDoctorApi,fetchAdminAppointmentsApi,cancelAppointmentApi,exportDoctorsApi, exportDoctorProfileApi, checkExportStatusApi ,exportAppointmentsApi } from '@/api/admin'
import { delay } from '@/utils/comman'

export const useAdminStore=defineStore('admin',()=>{
    const loading = ref(false)
    const error = ref(null)
    const appointmentSummary = ref({pending: 0, confirmed: 0, completed: 0, cancelled: 0})
    const patientList=ref([])
    const adminAppointments = ref([])
    const exportLoading = ref(false)
    const pdfLoading = ref(false)
    const exportAppointmentsLoading = ref(false)

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
            await delay(2000)
            loading.value = false
        }
    }

    async function fetchPatients(){
        loading.value=true
        error.value=null
        try{
            const res = await fetchPatientsApi()
            console.log(res);
            patientList.value=res.data
            console.log(patientList);
            
        }
        catch (err){
            error.value=err
            console.log(err);
            
        }finally{
            loading.value=false
        }
    }


    async function blockDoctor(doctorId, reason="") {
        loading.value = true
        error.value = null
        try {
            const res = await blockDoctorApi(doctorId, reason)
            console.log(res)
            return res.data
        } catch (err) {
            error.value = err
            console.error("Doctor block failed:", err)
            throw err
        } finally {
            loading.value = false
        }
    }
    async function unblockDoctor(doctorId){
        loading.value = true
        error.value = null

        try{
            const res = await unblockDoctorApi(doctorId)
            return res.data
        }
        catch(err){
            error.value = err
            throw err
        }
        finally{
            loading.value = false
        }
    }

    async function fetchAdminAppointments(page = 1) {
        loading.value = true
        error.value = null

        try {

            const res = await fetchAdminAppointmentsApi()

            adminAppointments.value = res.data.appointments

            console.log(res)

        } catch (err) {

            error.value = err
            console.log(err)

        } finally {

            loading.value = false
        }
    }

    async function cancelAppointment(appointmentId, reason="Cancelled by admin") {
        loading.value = true
        error.value = null

        try {
            const res = await cancelAppointmentApi(appointmentId, reason )
            console.log(res);
            return res.data

        } catch (err) {
            error.value = err
            throw err
        } finally {
            loading.value = false
        }
    }

    async function exportDoctors() {
    exportLoading.value = true
    error.value = null

    try {
        const res = await exportDoctorsApi()
        const taskId = res.data.task_id

        const interval = setInterval(async () => {
            try {
                const statusRes = await checkExportStatusApi(taskId)

                if (statusRes.data.status === "completed") {
                    clearInterval(interval)

                    window.location.href = `http://127.0.0.1:5000/exports/${statusRes.data.filename}`

                    exportLoading.value = false
                }

                if (statusRes.data.status === "failed") {
                    clearInterval(interval)
                    exportLoading.value = false
                    error.value = "Export failed"
                }

            } catch (err) {
                clearInterval(interval)
                exportLoading.value = false
                error.value = err
            }
        }, 2000)

    } catch (err) {
        exportLoading.value = false
        error.value = err
    }
}

async function downloadDoctorPdf(doctorId) {
    pdfLoading.value = true
    error.value = null

    try {
        const res = await exportDoctorProfileApi(doctorId)
        const taskId = res.data.task_id

        const interval = setInterval(async () => {
            try {
                const statusRes = await checkExportStatusApi(taskId)

                if (statusRes.data.status === "completed") {
                    clearInterval(interval)

                    window.location.href = `http://127.0.0.1:5000/exports/${statusRes.data.filename}`

                    pdfLoading.value = false
                }

                if (statusRes.data.status === "failed") {
                    clearInterval(interval)
                    pdfLoading.value = false
                    error.value = "PDF generation failed"
                }

            } catch (err) {
                clearInterval(interval)
                pdfLoading.value = false
                error.value = err
            }
        }, 2000)

    } catch (err) {
        pdfLoading.value = false
        error.value = err
    }
}
async function exportAppointments() {
    exportAppointmentsLoading.value = true
    error.value = null

    try {
        const res = await exportAppointmentsApi()
        const taskId = res.data.task_id

        const interval = setInterval(async () => {
            try {
                const statusRes = await checkExportStatusApi(taskId)

                if (statusRes.data.status === "completed") {
                    clearInterval(interval)

                    window.location.href = `http://127.0.0.1:5000/exports/${statusRes.data.filename}`

                    exportAppointmentsLoading.value = false
                }

                if (statusRes.data.status === "failed") {
                    clearInterval(interval)
                    exportAppointmentsLoading.value = false
                    error.value = "Export failed"
                }

            } catch (err) {
                clearInterval(interval)
                exportAppointmentsLoading.value = false
                error.value = err
            }
        }, 2000)

    } catch (err) {
        exportAppointmentsLoading.value = false
        error.value = err
    }
}


    return {
        loading,
        error,
        dashboard,
        selectedRange,
        fetchAdminDashboardDetails,
        appointmentSummary,
        fetchPatients,
        patientList,
        blockDoctor,
        unblockDoctor,
        adminAppointments,
        fetchAdminAppointments,
        cancelAppointment,
        exportDoctors,
        downloadDoctorPdf,
        exportLoading,
        pdfLoading,
        exportAppointments,
        exportAppointmentsLoading
        
    }

})