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

export const hasAlpha = (letter, msg) => {
    return (value) => value && value.includes(letter) ? "" : msg || `Must contain the letter '${letter}'`
}


function toMinutes(time) {
  if (!time) return null
  const [h, m] = time.split(":").map(Number)
  return h * 60 + m
}

export const timeMin = (min, msg) => value => {
  if (!value) return null
  return toMinutes(value) < toMinutes(min) ? msg : null
}

export const timeMax = (max, msg) => value => {
  if (!value) return null
  return toMinutes(value) > toMinutes(max) ? msg : null
}

export const afterTime = (startRef, msg) => value => {
    if (!value) return null
    if (!startRef.value) return "Please enter start time first"
    return toMinutes(value) <= toMinutes(startRef.value)
        ? msg || "End time must be after start time"
        : null
}
