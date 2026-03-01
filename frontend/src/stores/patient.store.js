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
    const historyPagination = ref({ page: 1, per_page: 6, total: 0, pages: 1 })
    const patientAppointmentHistory=ref([])
    

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
    loading.value = true
    error.value = null

    try {
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

                    loading.value = false
                }

                if (statusRes.data.status === "failed") {
                    clearInterval(interval)
                    loading.value = false
                    error.value = "Export failed"
                }

            } catch (err) {
                clearInterval(interval)
                loading.value = false
                error.value = err
            }
        }, 2000)

    } catch (err) {
        loading.value = false
        error.value = err
        console.log(err)
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
        exportPatientTreatment
    }
})