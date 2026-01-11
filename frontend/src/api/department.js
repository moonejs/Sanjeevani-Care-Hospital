import api from "./axios";

export const departmentDetailsApi = ()=>{
    return api.get("/api/departments")
}

export const addDepartmentApi=(data)=>{
    return api.post("api/departments",data)
}

export const departmentDetailsByIdApi=(id)=>{
    return api.get(`api/departments/${id}`)
}