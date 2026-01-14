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
    return api.get("api/appointments",{
        params:{"date":date}
    })
}