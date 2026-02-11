import api from "./axios"


export const fetchAdminDashboardDetailsApi=(range='today')=>{
    return api.get("api/admin/dashboard",{
        params:{range}
    })
}

