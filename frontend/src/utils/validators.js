export const required = (msg = "This field is required")=>{
    return (value) =>(!value ? msg :"")
}

export const minLength = (len,msg) => {
    return (value) => value && value.length < len ? msg || `Minimum ${len} characters`:""
}
export const maxLength = (len,msg) =>{
    return (value) => value && value.length > len ? msg || `Maximum ${len} characters` :""
}