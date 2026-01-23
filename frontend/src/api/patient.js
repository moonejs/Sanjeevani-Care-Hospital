import api from "./axios"

export const patientData=()=>{
    return api.get("/api/patients/profile")
}

export const patientProfile=(data)=>{
    return api.put("/api/patients/profile",data)
}
export const fetchPatientDashboardDataApi=()=>{
    return api.get("api/patients/dashboard")
}