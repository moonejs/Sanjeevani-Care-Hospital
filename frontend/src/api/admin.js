import api from "./axios"

export const addDoctorApi = (data)=>{
    return api.post("/api/admin/doctors",data) 
}

export const departmentDetailsApi = ()=>{
    return api.get("/api/admin/departments")
}

export const addDepartmentApi=(data)=>{
    return api.post("api/admin/departments",data)
}

export const doctorDetailsApi=()=>{
    return api.get("api/admin/doctors")
}