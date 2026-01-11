import { defineStore } from "pinia";
import { doctorDetailsApi ,doctorDetailsByIdApi} from "@/api/doctor";
import { ref } from "vue";


export const useDoctorStore=defineStore('doctor',()=>{

    const doctorsList=ref([])
    const loading=ref(false)
    const error=ref(null)
    const selectedDoctor=ref(null)

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

    return{
        fetchDoctors,
        doctorsList,
        fetchDoctorById,
        selectedDoctor,
        loading,
        error  
    }
})