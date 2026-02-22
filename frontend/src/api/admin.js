import api from "./axios"


export const fetchAdminDashboardDetailsApi=(range='today')=>{
    return api.get("api/admin/dashboard",{
        params:{range}
    })
}

export const fetchPatientsApi=()=>{
    return api.get("api/patients")
}

