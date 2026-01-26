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

export const fetchPatientProfileApi=(id)=>{
    return api.get(`api/doctors/patients/${id}/profile`)
}

export const fetchDoctorPatientsListApi=(params)=>{
    return api.get('api/doctors/patients',{
        params
    })
}

export const fetchDoctorsByDepartmentApi =(departmentId) => {
    return api.get(`/api/departments/${departmentId}/doctors`)
}

export const updateDoctorProfileApi=(data)=>{
    return api.put("/api/doctors/profile",data,{
        headers: {
            "Content-Type": "multipart/form-data"
        }
    })
}

export const fetchCurrrentDoctorDetailsApi=()=>{
    return api.get('/api/doctors/profile')
}
