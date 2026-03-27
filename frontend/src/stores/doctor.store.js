import { defineStore } from "pinia";
import { doctorDetailsApi ,doctorDetailsByIdApi,fetchAssignedTodayPatientsDetailsApi,fetchNextAppointmentApi,fetchPatientProfileApi,fetchDoctorPatientsListApi,fetchDoctorsByDepartmentApi,addDoctorApi,fetchCurrrentDoctorDetailsApi,updateDoctorProfileApi} from "@/api/doctor";
import { delay } from "@/utils/comman";
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
    const patients = ref([])
    const totalPatients = ref(0)
    const historyPagination = ref({ page: 1, per_page: 6, total: 0, pages: 1 })
    const doctorsByDepartment = ref([])
    const doctorProfile = ref(null)


    async function fetchDoctors(){
        loading.value=true
        error.value=null
        
        try {
            const res = await doctorDetailsApi()
            console.log(res);        
            doctorsList.value=res.data
        
            
        } catch (err) {
            error.value=err
            console.log(error);            
        }finally{
            await delay(5000)
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

    async function fetchDoctorPatientsList(page=1){
        loading.value=true,
        error.value=null
        try {
            const res = await fetchDoctorPatientsListApi({ page, per_page: historyPagination.value.per_page })
            patients.value = res.data.patients
            historyPagination.value = res.data.pagination
            totalPatients.value=historyPagination.value.total
            console.log(res);
            

        } catch (err) {
            error.value=err
            console.log(err);
            
        }finally{
            await delay(2000)
            loading.value=false
        }
    }
    async function fetchDoctorsByDepartment(departmentId){
        loading.value = true
        error.value = null
        try {
            const res = await fetchDoctorsByDepartmentApi(departmentId)
            doctorsByDepartment.value = res.data
        } catch(err){
            error.value = err
            console.log(err)
        } finally {
            loading.value = false
        }
    }
    async function addDoctor(data){
        loading.value=true
        error.value=null
        try {
            const res = await addDoctorApi(data)
            console.log(res);
            return res.data
            
        } catch (err) {
            error.value=err
            throw err
            console.log(err);
            
        }finally{
            loading.value=false
        }
    }

    async function fetchCurrrentDoctorDetails() {
        loading.value = true
        error.value=null
        try {
            const res = await fetchCurrrentDoctorDetailsApi()
            doctorProfile.value = res.data
            console.log(res);
            
        } catch (err) {
            error.value = err
            console.log(err);
            
        } finally {
            loading.value = false
        }
    }
    async function updateDoctorProfile(formData) {
        loading.value = true
        error.value=null
        try {
            const res = await updateDoctorProfileApi(formData)
            await fetchCurrrentDoctorDetails() 
            console.log(res);
            
        } catch (err) {
            error.value = err
            console.log(err);
            
        } finally {
            loading.value = false
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
        selectedPatient,
        fetchDoctorPatientsList,
        patients,
        totalPatients,
        historyPagination,
        fetchDoctorsByDepartment,
        doctorsByDepartment,
        addDoctor,
        fetchCurrrentDoctorDetails,
        updateDoctorProfile,
        doctorProfile,
    }
})