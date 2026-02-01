import api from "./axios";


export const saveDoctorAvailabilityApi=(data)=>{
    return api.post("api/availability",data)
}

export const fetchDoctorAvailabilityApi=(date)=>{
    return api.get("api/availability",{
        params:{"date":date}
    })
}

export const fetchAllDoctorsAvailabilityApi=(date)=>{
    return api.get("api/patients/appointments",{
        params:{"date":date}
    })
}

export const bookAppointmentApi=(data)=>{
    return api.post("api/appointments/book",data)
}

export const rescheduleAppointmentApi=(appointment_id,data)=>{
    return api.put(`api/appointments/reschedule/${appointment_id}`,data)
}

export const fetchAppointmentsByDoctorApi=(date)=>{
    return api.get("api/doctors/appointments",{
        params:{"date":date}
    })
}


export const updateAppointmentStatusApi=(appointment_id,status)=>{
    return api.patch(`api/doctors/appointments/${appointment_id}/status`,{
        "status":status
    })
}

export const completeAppointmentApi=(appointment_id,data)=>{
    return api.post(`api/doctors/appointments/${appointment_id}/complete`,data)
}

export const fetchDoctorAppointmentsHistoryApi=(params)=>{
    return api.get('api/doctors/appointments/history',{
        params
    })
}

export const fetchPatientAppointmentsHistoryApi=(params)=>{
    return api.get('api/patients/appointments/history',{
        params
    })
}