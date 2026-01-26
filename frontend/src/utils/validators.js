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

export const specialChar= (msg) => {
    return (value) => value && /[^a-zA-Z0-9\s]/.test(value) ? "" : msg || "add at least one Special character"
}

export const hasCapital = (msg) => {
    return (value) => value && /[A-Z]/.test(value) ? "" : msg || "Must contain at least one capital letter"
}

export const hasDigit = (msg) => {
    return (value) => value && /\d/.test(value) ? "" : msg || "Must contain at least one digit"
}