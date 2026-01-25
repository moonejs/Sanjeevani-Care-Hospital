import api from "./axios"

export const patientData=()=>{
    return api.get("/api/patients/profile")
}

export const updatepatientProfileApi=(data)=>{
    return api.put("/api/patients/profile",data,{
        headers: {
            "Content-Type": "multipart/form-data"
        }
    })
}
export const fetchPatientDashboardDataApi=()=>{
    return api.get("api/patients/dashboard")
}