import api from "./axios"

export const patientData=()=>{
    return api.get("/api/patients/profile")
}

export const patientProfile=(data)=>{
    return api.put("/api/patient/profile",data)
}