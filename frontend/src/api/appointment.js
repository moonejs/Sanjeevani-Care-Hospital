import api from "./axios";


export const saveDoctorAvailabilityApi=(data)=>{
    return api.post("api/appointments",data)
}

export const fetchDoctorAvailabilityApi=(date)=>{
    return api.get("api/appointments",{
        params:{"date":date}
    })
}