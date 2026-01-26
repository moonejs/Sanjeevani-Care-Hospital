<script setup>
    import { useDepartmentStore } from '@/stores/department.store';
    import { useDoctorStore } from '@/stores/doctor.store';
    import ProfileCard from '@/components/layout/ProfileCard.vue';
    import { useRoute,useRouter } from 'vue-router';
    import { onMounted ,computed } from 'vue';
    import { departmentIcons } from '@/utils/departmentIcons';
    import { Phone,Mail,MapPinHouse,Calendar } from 'lucide-vue-next';
    import Badge from '@/components/common/Badge.vue';
    const department=useDepartmentStore()
    const route=useRoute()
    const router=useRouter()
    const departmentId = route.params.id
    const doctor=useDoctorStore()

    onMounted(()=>{
        department.fetchDepartmentById(departmentId)
        doctor.fetchDoctorsByDepartment(departmentId)
    })

    function openDoctorPage(id){
        router.push({
            name:'doctorProfile-patient',
            params:{
                id:id
            }
        })
    }

    const doctorsList=computed(()=>{
        return doctor.doctorsByDepartment
    })

    const departmentIcon = computed(() => {
        return departmentIcons.find(i => i.key ===department.selectedDepartment?.icon)?.component
    })

</script>

<template>
    <div class="d-flex container-fluid">

        <div class="departmentDetail-page-left container-fluid bg-success">
            <div class="upper bg-warning">
                <h1>Speciallists</h1>

                <div class="bg-primary">
                    <div class="row">
                        <div class="col-4" v-for="doctor in doctorsList" :key="doctor.id" >
                            <ProfileCard :label="doctor.name"   @select="openDoctorPage(doctor.id)" class="doctor-profile-card" />
                        </div>
                    </div>
                    
                </div>
            </div>

            
        </div>
        <div class="departmentDetail-page-right container-fluid bg-danger">
            <div v-if="department.loading">
                Loading department...
            </div>

            <div v-else-if="!department.selectedDepartment">
                <p>No department found</p>
            </div>
            <div v-else>
          <div class="d-flex align-items-center mb-4 mt-2">
            <component v-if="departmentIcon" :is="departmentIcon" class="me-3 text-primary department-detail-icon"/>
            <h1 class="mb-0 display-2">{{ department.selectedDepartment.name }}</h1>

            <div v-if="department.selectedDepartment.emergency_available" class="ms-4">
                <Badge label="Emergency Available" color="success"/>
            </div>
            <div v-else="department.selectedDepartment.emergency_available" class="ms-4">
                <Badge label="Emergency Not Available" color="danger"/>
            </div>
          </div>

          
          <p class="fs-6">
            {{ department.selectedDepartment.description }}
          </p>

          <div class="bg-light d-flex gap-8 ">
                <div v-if="department.selectedDepartment.services?.length" class="mt-4">
                    <h5>Services Provided</h5>
                    <ul>
                    <li
                        v-for="(service, i) in department.selectedDepartment.services"
                        :key="i"
                    >
                        {{ service }}
                    </li>
                    </ul>
                </div>
                <div v-if="department.selectedDepartment.facilities?.length" class="mt-4">
                    <h5>Facilities</h5>
                    <ul>
                    <li
                        v-for="(facility, i) in department.selectedDepartment.facilities"
                        :key="i"
                    >
                        {{ facility }}
                    </li>
                    </ul>
                </div>
          </div>
          
          <div class="bg-info d-flex gap-6">

              <div class="mt-4">
                    <h5>Contact</h5>
                    <p v-if="department.selectedDepartment.phone">
                      <span>
                          <Phone :size="20"/>
                        </span>
                        {{ department.selectedDepartment.phone }}
                    </p>
                    <p v-if="department.selectedDepartment.email">
                        <Mail :size="20"/>
                        {{ department.selectedDepartment.email }}
                    </p>
                    <p v-if="department.selectedDepartment.building">
                        <MapPinHouse :size="20"/>
                        {{ department.selectedDepartment.building }}
                        <span v-if="department.selectedDepartment.floor">
                            
                            , Floor {{ department.selectedDepartment.floor }}
                        </span>
                    </p>
                </div>

                <div v-if="department.selectedDepartment.opd_timing" class="mt-4">
                    <Calendar :size="20" />
                    {{ department.selectedDepartment.opd_timing}}
                </div>
              
            </div>
        </div>

        </div>
    </div>
</template>