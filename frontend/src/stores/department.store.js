import { defineStore } from "pinia";
import { ref,computed } from "vue";
import { departmentDetailsApi,departmentDetailsByIdApi,addDepartmentApi } from "@/api/department";
import { delay } from "@/utils/comman";

export const useDepartmentStore = defineStore('department',()=>{

    const departmentList=ref([])
    const loading=ref(false)
    const error=ref(null)
    const selectedDepartment=ref(null)



    async function fetchDepartments(){
        if(departmentList.value.length) return
        loading.value=true
        error.value=null

        
        try {
            const res=await departmentDetailsApi()
            departmentList.value=res.data
            console.log(res);
            
            
        } catch (err) {
            error.value=err
            console.log(err);
            
        }finally{
            await delay(2000)
            loading.value = false
            }
    }

    async function fetchDepartmentById(id){
        loading.value=true
        error.value=null

        try {
            const res= await departmentDetailsByIdApi(id)
            
            selectedDepartment.value=res.data
            console.log(selectedDepartment.value);
            console.log(res);
            
            
            
        } catch (error) {
            error.value=error
            console.log(error);
            
        }finally{
            loading.value=false
        }
    }

    async function addDepartment(data) {
        loading.value=true
        error.value=null

        try {
            const res =await addDepartmentApi(data)
            console.log(res);
            
        } catch (err) {
            error.value=err
            console.log(err);
        }finally{
            loading.value=false
        }
    }

    return {
        departmentList,
        fetchDepartments,
        loading,
        error,
        fetchDepartmentById,
        selectedDepartment,
        addDepartment,
    }
})