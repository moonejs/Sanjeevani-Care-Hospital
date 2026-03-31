<script setup>
    import BaseTable from '../layout/BaseTable.vue';
    import BaseTableHead from '../layout/BaseTableHead.vue';
    import DoctorDashTableCaption from '../Doctor/DoctorDashTableCaption.vue';
    import AdminDoctorsRow from './AdminDoctorsRow.vue';
    import { useSearchFilter } from '@/utils/useSearchFilter';
    import { storeToRefs } from 'pinia';
    import { useDoctorStore } from '@/stores/doctor.store';
    import { useAdminStore } from '@/stores/admin.store';
    import { ref ,onMounted} from 'vue';
    import LoadingState from '../common/LoadingState.vue';
    import Btn from '../common/Btn.vue';
    import { useToastStore } from '@/stores/toast.store';
    import { useDepartmentStore } from '@/stores/department.store';

    const departmentStore=useDepartmentStore()
    const toast = useToastStore()
    const doctorStore=useDoctorStore()
    const adminStore=useAdminStore()
    const dptList=ref([])

    const props = defineProps({
        doctors: {
            type: Array,
            default: () => []
        }
    })
    onMounted(async ()=>{
        await departmentStore.fetchDepartments()
        departmentStore.departmentList.forEach(d => {
            dptList.value.push(d.name)
        });
    })
    const tHead=["Registration No.","Name","Department","Email","Specialization","Appointment Status","Actions"]
    


    const emit = defineEmits(['view','block','unblock'])


    const departmentFilter = ref('')
    const { doctorsList } = storeToRefs(doctorStore)
    const { searchQuery, filteredData } = useSearchFilter(
        doctorsList,
        ['name', 'email', 'department','registration_number'],
        {
            department: departmentFilter
        }
    )


    async function exportTreatment(){
      try {
        await adminStore.exportDoctors()
        toast.addToast({
          message: 'Downloaded Csv successfully',
          type: 'success'
        })
      } catch (error) {
        toast.addToast({
          title: 'Error',
          message: 'Failed to Download csv',
          type: 'error'
        })
      }

    }
</script>

<template>
    <BaseTable>
        <template #caption>
            
            <DoctorDashTableCaption title="Registered Doctors" v-model:searchQuery="searchQuery" :is-dropdown="true" 
            v-model:filter-drop="departmentFilter"
            filter-drop-label="Departments" :filter-drop="departmentFilter" :filter-drop-options="dptList" class3=" d-flex  gap-2 ms-7" class1=" ps-2" placeholder="Search Doctors..." class4="ms-5 w-100"/>

            <Btn  label="Clear" class="btn-primary btn-sm position-absolute right-9 top-5 mt-3 me-6 "   @click="searchQuery = ''; departmentFilter = '' "/>


            <Btn  :label="adminStore.exportLoading? 'Exporting...' : 'Export csv'" :loader="adminStore.exportLoading" @click="exportTreatment" class="btn-outline-secondary btn-sm position-absolute right-7 top-5 mt-3"/>

        </template>
        <template #head>
            <BaseTableHead :t-head="tHead"/>
        </template>
        <template #body class="">
            <LoadingState :loading="doctorStore.loading" class="position-absolute start-50 ms-5 top-1 " >
                <h4 v-if="filteredData.length == 0" class="text-muted d-flex position-absolute left-50 ms-12 top-2 justify-content-center mt-10">No Registered Doctors Found</h4>
                <AdminDoctorsRow  v-else v-for="(doctor,index) in filteredData" :key="index" :index=" 
            index" :doctor="doctor" @view="emit('view',doctor)" @block="emit('block',doctor)" @unblock="emit('unblock',doctor)"/>
            </LoadingState>
        </template>
    
    </BaseTable>
</template>

<style scoped>
.t{
    height: 4rem;
    overflow-y: auto;
}
</style>