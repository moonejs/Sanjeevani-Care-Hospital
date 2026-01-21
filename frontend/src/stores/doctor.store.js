import { defineStore } from "pinia";
import { doctorDetailsApi ,doctorDetailsByIdApi,fetchAssignedTodayPatientsDetailsApi,fetchNextAppointmentApi,fetchPatientProfileApi} from "@/api/doctor";
import { ref } from "vue";




export const useDoctorStore=defineStore('doctor',()=>{

    const doctorsList=ref([])
    const loading=ref(false)
    const error=ref(null)
    const selectedDoctor=ref(null)
    const assignedPatientsList=ref([])
    const totalAssignedPatients=ref(0)
    const nextAppointment = ref(null)
    const selectedPatient=ref(null)

    async function fetchDoctors(){
        if(doctorsList.value.length) return
        loading.value=true
        error.value=null
        try {
            const res = await doctorDetailsApi()
            console.log(res);
            doctorsList.value=res.data
            
        } catch (error) {
            error.value=error
            console.log(error);            
        }finally{
            loading.value=false
        }
        
    }

    async function fetchDoctorById(id){
        loading.value=true
        error.value=null
        try {
            const res=await doctorDetailsByIdApi(id)
            console.log(res);
            selectedDoctor.value=res.data
            
        } catch (error) {
            error.value=error
            console.log(error);
            
        }finally{
            loading.value=false
        }
    }

    async function fetchAssignedTodayPatientsDetails(date){
        loading.value=true,
        error.value=null

        try {
            const res=await fetchAssignedTodayPatientsDetailsApi(date)
            assignedPatientsList.value=res.data.patients
            totalAssignedPatients.value=res.data.total_patients

            console.log(res);
            
        } catch (err) {
            error.value=err
            console.log(err);
            
        }finally{
            loading.value=false
        }
    }
    async function fetchNextAppointment(){
        loading.value=true,
        error.value=null
        try {
            const res = await fetchNextAppointmentApi()
            console.log(res);
            
            nextAppointment.value = res.data
        } catch (err) {
            error.value=err
            console.log(err)
        }finally{
            loading.value=false
        }
    }

    async function refreshDoctor(){
        const today = new Date().toISOString().split('T')[0]

        await Promise.all([
            fetchAssignedTodayPatientsDetails(today),
            fetchNextAppointment()
        ])
    }
    async function fetchPatientProfile(id){
        loading.value=true
        error.value=null

        try {
            const res=await fetchPatientProfileApi(id)
            selectedPatient.value=res.data
            console.log(res);
                        
        } catch (err) {
            error.value=err
            console.log(err);
            
        }finally{
            loading.value=false
        }
    }


    return{
        fetchDoctors,
        doctorsList,
        fetchDoctorById,
        selectedDoctor,
        loading,
        error,
        fetchAssignedTodayPatientsDetails,
        assignedPatientsList,
        totalAssignedPatients,
        fetchNextAppointment,
        nextAppointment,
        refreshDoctor,
        fetchPatientProfile,
        selectedPatient 
    }
})