import { defineStore } from "pinia";
import { fetchPatientDashboardDataApi } from "@/api/patient";
import { fetchPatientAppointmentsHistoryApi } from "@/api/appointment";

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
            loading.value=false
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
        patientAppointmentHistory
    }
})