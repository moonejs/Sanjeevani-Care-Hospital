import api from "./axios";

export const loginApi = (data)=>{
    return api.post('/login?include_auth_token',data)
}
export const currentUserApi=(token)=>{
    return api.get("/api/me",{
        headers:{
            "Authentication-Token" :token
        }
    })
}