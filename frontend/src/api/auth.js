import api from "./axios";

export const loginApi = (data)=>{
    return api.post('/login?include_auth_token',data)
}