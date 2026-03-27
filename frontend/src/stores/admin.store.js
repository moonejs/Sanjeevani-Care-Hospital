import { defineStore } from 'pinia'
import { ref, computed ,watch} from 'vue'
import { fetchAdminDashboardDetailsApi,fetchPatientsApi,blockDoctorApi,unblockDoctorApi,fetchAdminAppointmentsApi,cancelAppointmentApi } from '@/api/admin'
import { delay } from '@/utils/comman'

export const useAdminStore=defineStore('admin',()=>{
    const loading = ref(false)
    const error = ref(null)
    const appointmentSummary = ref({pending: 0, confirmed: 0, completed: 0, cancelled: 0})
    const patientList=ref([])
    const adminAppointments = ref([])
    const adminAppointmentsPagination = ref({ page: 1, per_page: 10, total: 0, pages: 1 })


    const dashboard = ref({
        stats: {},
        upcoming_appointments: [],
        status_summary: {},
        recent_activity: []
    })

    const selectedRange = ref("today")
    async function fetchAdminDashboardDetails(range = "today") {
        loading.value = true
        error.value = null
        try {
            selectedRange.value = range
            const res = await fetchAdminDashboardDetailsApi(range)
            dashboard.value = res.data
            appointmentSummary.value=res.data.status_summary
            console.log(res);
            
        } catch (err) {
            error.value = err
            console.error("Dashboard fetch failed:", err)
        } finally {
            await delay(2000)
            loading.value = false
        }
    }

    async function fetchPatients(){
        loading.value=true
        error.value=null
        try{
            const res = await fetchPatientsApi()
            console.log(res);
            patientList.value=res.data
            console.log(patientList);
            
        }
        catch (err){
            error.value=err
            console.log(err);
            
        }finally{
            loading.value=false
        }
    }


    async function blockDoctor(doctorId, reason="") {
        loading.value = true
        error.value = null
        try {
            const res = await blockDoctorApi(doctorId, reason)
            console.log(res)
            return res.data
        } catch (err) {
            error.value = err
            console.error("Doctor block failed:", err)
            throw err
        } finally {
            loading.value = false
        }
    }
    async function unblockDoctor(doctorId){
        loading.value = true
        error.value = null

        try{
            const res = await unblockDoctorApi(doctorId)
            return res.data
        }
        catch(err){
            error.value = err
            throw err
        }
        finally{
            loading.value = false
        }
    }

    async function fetchAdminAppointments(page = 1) {
        loading.value = true
        error.value = null

        try {

            const res = await fetchAdminAppointmentsApi({
                page,
                per_page: adminAppointmentsPagination.value.per_page
            })

            adminAppointments.value = res.data.appointments
            adminAppointmentsPagination.value = res.data.pagination

            console.log(res)

        } catch (err) {

            error.value = err
            console.log(err)

        } finally {

            loading.value = false
        }
    }

    async function cancelAppointment(appointmentId, reason="Cancelled by admin") {
        loading.value = true
        error.value = null

        try {
            const res = await cancelAppointmentApi(appointmentId, reason )
            console.log(res);
            return res.data

        } catch (err) {
            error.value = err
            throw err
        } finally {
            loading.value = false
        }
    }
    return {
        loading,
        error,
        dashboard,
        selectedRange,
        fetchAdminDashboardDetails,
        appointmentSummary,
        fetchPatients,
        patientList,
        blockDoctor,
        unblockDoctor,
        adminAppointments,
        adminAppointmentsPagination,
        fetchAdminAppointments,
        cancelAppointment
    }

})