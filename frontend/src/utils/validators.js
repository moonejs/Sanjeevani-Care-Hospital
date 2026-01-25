export const required = (msg = "This field is required")=>{
    return (value) =>(!value ? msg :"")
}

export const minLength = (len,msg) => {
    return (value) => value && value.length < len ? msg || `Minimum ${len} characters`:""
}
export const maxLength = (len,msg) =>{
    return (value) => value && value.length > len ? msg || `Maximum ${len} characters` :""
}
export const postive = (msg) =>{
    return (value) => value && value < 0 ? msg || `Must be a postive value` :""
}

export const maxValue = (max, msg) => {
    return (value) => value && value <= max ? "": msg || `Must be less than or equal to ${max}`
}