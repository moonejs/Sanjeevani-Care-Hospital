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

export const fetchAppointmentsByDoctorApi=(date)=>{
    return api.get("api/doctors/appointments",{
        params:{"date":date}
    })
}