import { defineStore } from "pinia";
import { fetchPatientDashboardDataApi,updatepatientProfileApi,exportPatientTreatmentApi,checkExportStatusApi } from "@/api/patient";
import { fetchPatientAppointmentsHistoryApi } from "@/api/appointment";
import { delay } from "@/utils/comman";

import { ref } from "vue";

export const usePatientStore=defineStore('patient',()=>{
    const loading=ref(false)
    const error =ref(null)
    const nextAppointment = ref(null)
    const upcomingCount = ref(0)
    const lastVisit = ref(null)
    const historyPagination = ref({ page: 1, per_page: 8, total: 0, pages: 1 })
    const patientAppointmentHistory=ref([])
    const exportLoading = ref(false)
    const loadingPdf = ref(false)

    async function fetchPatientDashboardData(){
        loading.value=true
        error.value=null

       
        try {
            const res = await fetchPatientDashboardDataApi()

            nextAppointment.value = res.data.next_appointment
            upcomingCount.value = res.data.upcoming_count
            lastVisit.value = res.data.last_visit

            console.log(res);
            
        } catch (err) {
            error.value=err
            console.log(err);
            
        }finally{
            await delay(1000)
            loading.value=false
        }
    }

    async function fetchPatientAppointmentsHistory(page=1){
        loading.value=true
        error.value=null

        
        try {

            const res = await fetchPatientAppointmentsHistoryApi({ page, per_page: historyPagination.value.per_page })
            patientAppointmentHistory.value = res.data.appointments
            historyPagination.value = res.data.pagination
            console.log(res);
            
        } catch (err) {
            error.value=err
            console.log(err);
            
        }finally{
            await delay(2000)
            loading.value=false
        }
    }

    async function updatepatientProfile(data){
        loading.value=true
        error.value=null
        try {
            const res =await updatepatientProfileApi(data)
            console.log(res);
            
        } catch (err) {
            console.log(err);
            error.value=err
            
        }finally{
            loading.value=false
        }
    }

    async function exportPatientTreatment() {
        exportLoading.value = true
        error.value = null

        try {
            await delay(3000)
            const res = await exportPatientTreatmentApi()
            const taskId = res.data.task_id

            const interval = setInterval(async () => {
                try {
                    const statusRes = await checkExportStatusApi(taskId)

                    console.log("Status:", statusRes.data.status)

                    if (statusRes.data.status === "completed") {
                        clearInterval(interval)

                        const filename = statusRes.data.filename

                    
                        window.location.href = `http://127.0.0.1:5000/exports/${filename}`

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
            exportLoading.value = true
            error.value = err
            console.log(err)
        }
    }

    async function downloadPdf(appointmentId) {
        loadingPdf.value = true

        try {
            const res = await fetch(`http://127.0.0.1:5000/export-appointment/${appointmentId}`)
            const data = await res.json()

            const taskId = data.task_id

            const interval = setInterval(async () => {
                const statusRes = await fetch(`http://127.0.0.1:5000/export-status/${taskId}`)

                if (!statusRes.ok) {
                    throw new Error("Server error while checking PDF status")
                }

                const status = await statusRes.json()

                if (status.status === "completed") {
                    clearInterval(interval)

                    window.location.href = `http://127.0.0.1:5000/exports/${status.filename}`

                    loadingPdf.value = false
                }

                if (status.status === "failed") {
                    clearInterval(interval)
                    loadingPdf.value = false
                }
            }, 2000)

        } catch (err) {
            loadingPdf.value = false
        }
    }
    return {
        loading,
        error,
        nextAppointment,
        upcomingCount,
        lastVisit,
        fetchPatientDashboardData,
        fetchPatientAppointmentsHistory,
        historyPagination,
        patientAppointmentHistory,
        updatepatientProfile,
        exportPatientTreatment,
        exportLoading,
        downloadPdf,
        loadingPdf
    }
})