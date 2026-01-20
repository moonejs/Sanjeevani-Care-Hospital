import { defineStore } from 'pinia'
import { ref } from 'vue'
import { saveDoctorAvailabilityApi,fetchDoctorAvailabilityApi,fetchAllDoctorsAvailabilityApi,bookAppointmentApi,fetchAppointmentsByDoctorApi,updateAppointmentStatusApi,completeAppointmentApi } from '@/api/appointment'

import { useDoctorStore } from './doctor.store'


export const useAppointmentStore=defineStore('appointment',()=>{
    const loading=ref(false)
    const error=ref(null)
    const days=ref([])
    const today=new Date()
    const doctorsAvailability = ref([])
    const selectedDate=ref("")
    const appointmentListByDoctor=ref([])
    const appointmentSummary = ref({ total: 0, pending: 0, confirmed: 0, completed: 0, cancelled: 0 })
    

    function formatDate(date) {
        return date.toISOString().split('T')[0]
    }

    for(let i=1;i<=7;i++){
        const d=new Date(today)
        d.setDate(today.getDate()+i)

        days.value.push({
            day:d.toLocaleDateString('en-gb',{weekday: 'short',}),
            date:d.getDate(),
            fullDate: formatDate(d) 
        })
    }

    async function saveDoctorAvailability(data){
        loading.value=true
        error.value=null

        try {

            const payload={
                date:data.date,
                online_booking:data.onlineBooking,
                
                morning_enabled:data.morning.enabled,
                morning: {
                    from: data.morning.startTime,
                    to: data.morning.endTime,
                    slot_duration:data.morning.slotDuration,
                    max_patients:data.morning.maxPatients
                },
                afternoon_enabled: data.afternoon.enabled,
                afternoon: {
                    from: data.afternoon.startTime,
                    to: data.afternoon.endTime,
                    slot_duration:data.afternoon.slotDuration,
                    max_patients:data.afternoon.maxPatients
                },

                evening_enabled: data.evening.enabled,
                evening: {
                    from: data.evening.startTime,
                    to: data.evening.endTime,
                    slot_duration:data.evening.slotDuration,
                    max_patients:data.evening.maxPatients
                },
        
            }


            const res=await saveDoctorAvailabilityApi(payload)
            console.log(res);
            
            
        } catch (error) {
            error.value=error
            console.log(error);
            
        }finally{
            loading.value=false
        }
    }

    async function fetchDoctorAvailability(date) {
        loading.value=true
        error.value=null
        try {
            console.log(date);
            
            const res = await fetchDoctorAvailabilityApi(date)
            console.log(res);
            return res.data
            
        } catch (err) {
            error.value=err
            console.log(err);
            
        }finally{
            loading.value=false
        }
    }

    async function fetchAllDoctorsAvailability(date){
        loading.value=true
        error.value=null
        try {
            const res=await fetchAllDoctorsAvailabilityApi(date)
            doctorsAvailability.value=res.data.doctors
            console.log(res.data.doctors);
            return doctorsAvailability.value
            
        } catch (err) {
            error.value=err
            console.log(err);
            return
        }finally{
            loading.value=false
        }
    }

    async function bookAppointment(data){
        loading.value=true
        error.value=null
        try {
            const res=await bookAppointmentApi(data)
            console.log(res);
            
        } catch (error) {
            error.value=error
            console.log(error);
            
        }finally{
            loading.value=false
        }
    }

    async function fetchAppointmentsByDoctor(date){
        loading.value=true
        error.value=null
        try {
            const res=await fetchAppointmentsByDoctorApi(date)
            appointmentListByDoctor.value=res.data.appointments
            appointmentSummary.value=res.data.summary
            console.log(res);
            
        } catch (err) {
            error.value=err
            console.log(err);
            
        }finally{
            loading.value=false
        }
    }

    async function updateAppointmentStatus(appointment_id,status){
        loading.value=true
        error.value=null
        try {
            const res=await updateAppointmentStatusApi(appointment_id,status)
            await refreshAfterAppointmentChange()
            console.log(res);
        } catch (err) {
            error.value=err
            console.log(error);
            
        }
    }

    async function completeAppointment(appointment_id,data){
        loading.value=true
        error.value=null
        try {
            const res=await completeAppointmentApi(appointment_id,data)
            await refreshAfterAppointmentChange()
            console.log(res);
        } catch (err) {
            error.value=err
            console.log(err);
        }finally{
            loading.value=false
        }
    }
    async function refreshAfterAppointmentChange(){
        const doctorStore=useDoctorStore()
        await Promise.all([
            fetchAppointmentsByDoctor(selectedDate.value),
            doctorStore.refreshDoctor()
        ])
    }


    return{
        saveDoctorAvailability,
        loading,
        error,
        fetchDoctorAvailability,
        days,
        today,
        formatDate,
        fetchAllDoctorsAvailability,
        doctorsAvailability,
        selectedDate,
        bookAppointment,
        fetchAppointmentsByDoctor,
        appointmentListByDoctor,
        updateAppointmentStatus,
        completeAppointment,
        appointmentSummary
    }
})