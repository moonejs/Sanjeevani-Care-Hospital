import { defineStore } from "pinia";
import { fetchPatientDashboardDataApi } from "@/api/patient";
import { ref } from "vue";
export const usePatientStore=defineStore('patient',()=>{
    const loading=ref(false)
    const error =ref(null)
    const nextAppointment = ref(null)
    const upcomingCount = ref(0)
    const lastVisit = ref(null)

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



    return {
        loading,
        error,
        nextAppointment,
        upcomingCount,
        lastVisit,
        fetchPatientDashboardData
    }
})