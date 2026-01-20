import api from "./axios";

export const addDoctorApi = (data)=>{
    return api.post("/api/doctors",data) 
}


export const doctorDetailsApi=()=>{
    return api.get("api/doctors")
}

export const doctorDetailsByIdApi=(id)=>{
    return api.get(`api/doctors/${id}`)
}

export const fetchAssignedTodayPatientsDetailsApi=(date)=>{
    return api.get("api/doctors/patients/today",{
        params:{
            date:date
        }
    })
}

export const fetchNextAppointmentApi = () => {
  return api.get('/api/doctors/appointments/next')
}
