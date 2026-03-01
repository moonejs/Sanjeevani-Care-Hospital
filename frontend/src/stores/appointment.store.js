import { defineStore } from 'pinia'
import { ref } from 'vue'
import { saveDoctorAvailabilityApi,fetchDoctorAvailabilityApi,fetchAllDoctorsAvailabilityApi,bookAppointmentApi,fetchAppointmentsByDoctorApi,updateAppointmentStatusApi,completeAppointmentApi,fetchDoctorAppointmentsHistoryApi,rescheduleAppointmentApi,cancelBookedAppointmentApi } from '@/api/appointment'

import { fetchPatientAppointmentsHistoryApi } from '@/api/appointment'

import { useDoctorStore } from './doctor.store'
import { delay } from '@/utils/comman'


export const useAppointmentStore=defineStore('appointment',()=>{
    const loading=ref(false)
    const error=ref(null)
    const days=ref([])
    const today=new Date()
    const doctorsAvailability = ref([])
    const selectedDate=ref("")
    const appointmentListByDoctor=ref([])
    const appointmentSummary = ref({ total: 0, pending: 0, confirmed: 0, completed: 0, cancelled: 0 })
    const appointmentHistory = ref([])
    const historyPagination = ref({ page: 1, per_page: 6, total: 0, pages: 1 })
    const activeAppointment = ref(null)
    

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
    async function fetchDoctorAppointmentHistory(page = 1) {
        loading.value = true
        error.value =null

        try {
            const res = await fetchDoctorAppointmentsHistoryApi({ page, per_page: historyPagination.value.per_page })

            appointmentHistory.value = res.data.appointments
            historyPagination.value = res.data.pagination
            console.log(res);
            
        }catch(err){
            error.value=err
            console.log(err);
            
        }finally {
            await delay(2000)
            loading.value = false
        } 
    }

    async function rescheduleAppointment({ appointment_id, date, start_time }) {
        loading.value = true
        error.value = null
        try {
            const res=await rescheduleAppointmentApi(appointment_id, {date,
                start_time})
            console.log(res);
            
        } catch (err) {
            error.value = err
            throw err
        } finally {
            loading.value = false
        }
    }
    async function fetchMyActiveAppointment() {
        const res = await fetchPatientAppointmentsHistoryApi({ page: 1, per_page: 5 })

        activeAppointment.value =res.data.appointments.find(a =>["pending", "confirmed"].includes(a.status)) || null
    }

    async function cancelBookedAppointment(appointment_id,data){
        loading.value=true
        error.value=null
        try {
            const res =await cancelBookedAppointmentApi(appointment_id,data)
            await fetchMyActiveAppointment()
            await fetchAllDoctorsAvailability(selectedDate.value)
            console.log(res);
            
        } catch (err) {
            error.value=err
            console.log(err);
            
        }finally{
            loading.value=false
        }
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
        appointmentSummary,
        appointmentHistory,
        historyPagination,
        fetchDoctorAppointmentHistory,
        activeAppointment,
        rescheduleAppointment,
        fetchMyActiveAppointment,
        cancelBookedAppointment
    }
})