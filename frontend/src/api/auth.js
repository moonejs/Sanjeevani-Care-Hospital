import api from "./axios";

export const loginApi = (data)=>{
    return api.post('/login?include_auth_token',data)
}
export const currentUserApi=()=>{
    return api.get("/api/me")
}

export const logoutApi=()=>{
    return api.post("/logout")
}

export const registerApi=(data)=>{
    return api.post("/api/patient/register",data)
}