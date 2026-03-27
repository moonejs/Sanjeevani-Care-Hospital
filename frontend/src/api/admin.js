import api from "./axios"


export const fetchAdminDashboardDetailsApi=(range='today')=>{
    return api.get("api/admin/dashboard",{
        params:{range}
    })
}

export const fetchPatientsApi=()=>{
    return api.get("api/patients")
}

export const blockDoctorApi = (doctorId, reason = "") => {
    return api.post(`api/admin/doctors/${doctorId}/block`, {
        reason
    })
}

export const unblockDoctorApi = (doctorId) => {
    return api.post(`api/admin/doctors/${doctorId}/unblock`)
}

export const fetchAdminAppointmentsApi = (params) => {
  return api.get("/api/admin/appointments", { params })
}



export const cancelAppointmentApi = (appointmentId,reason) => {
    return api.put(`api/admin/appointments/${appointmentId}/cancel`, {
        reason
    })
}