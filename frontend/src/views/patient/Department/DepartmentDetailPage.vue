<script setup>
    import { useDepartmentStore } from '@/stores/department.store';
    import { useDoctorStore } from '@/stores/doctor.store';
    import ProfileCard from '@/components/layout/ProfileCard.vue';
    import { useRoute,useRouter } from 'vue-router';
    import { onMounted ,computed } from 'vue';
    import { departmentIcons } from '@/utils/departmentIcons';
    import { Phone,Mail,MapPinHouse,Calendar } from 'lucide-vue-next';
    import DoctorMiniCard from '@/components/Patient/DoctorMiniCard.vue';
    import Badge from '@/components/common/Badge.vue';
    import SearchInput from '@/components/common/SearchInput.vue';
    import { storeToRefs } from 'pinia';
    
    import { useSearchFilter } from '@/utils/useSearchFilter';

    const department=useDepartmentStore()
    const route=useRoute()
    const router=useRouter()
    const departmentId = route.params.id
    const doctor=useDoctorStore()

    onMounted(()=>{
        department.fetchDepartmentById(departmentId)
        doctor.fetchDoctorsByDepartment(departmentId)
    })

    const { doctorsByDepartment }=storeToRefs(doctor)
    const { searchQuery, filteredData } = useSearchFilter(
        doctorsByDepartment,
        ['name'],
        
    )

    function openDoctor(id) {
        router.push({
            name: "doctors-patient",
            query: { focus: id }
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
  <div class="container-fluid px-5 py-4">

    <div class="row g-5">
      <div class="col-lg-4">
        <div class="d-flex justify-content-between">
            <h4 class="section-title ">Doctors</h4>
            <SearchInput  class=""  v-model="searchQuery"  placeholder="Search doctors..."/>
        </div>
        <div class="mt-4">
          
          <div v-if="doctor.loading" class="text-muted small">
            Loading doctors...
          </div>
          <div v-else-if="!doctorsList.length" class="text-muted small">
            No doctors available
          </div>

          <DoctorMiniCard v-for="doc in filteredData" :key="doc.id" :doctor="doc" @select="openDoctor(doc.id)" />

        </div>

      </div>
      <div class="col-lg-8 " style="height: 37rem; overflow-y: auto;">

        <div v-if="department.loading">Loading...</div>

        <div v-else-if="!department.selectedDepartment">
          No department found
        </div>

        <div v-else>
          <div class="department-header mb-4">
            <div class="d-flex align-items-center gap-4">
              <div class="icon-wrapper-lg">
                <component  v-if="departmentIcon"  :is="departmentIcon"  class="text-dark"/>
              </div>

              <div>
                <h2 class="department-title mb-1">
                  {{ department.selectedDepartment.name }}
                </h2>

                <Badge :label="department.selectedDepartment.emergency_available ? 'Emergency available' : 'No emergency service'" :color="department.selectedDepartment.emergency_available ? 'success' :'danger'"/>
                
              </div>
            </div>
          </div>
          <p class="text-muted mb-5">
            {{ department.selectedDepartment.description }}
          </p>
          <div class="row">
            <div class="col-md-6">
              <div class="">
                <h5 class="text-muted">Services</h5>
                <ul class="clean-list">
                  <li v-for="(s, i) in department.selectedDepartment.services" :key="i">
                    {{ s }}
                  </li>
                </ul>
              </div>
            </div>

            <div class="col-md-6">
              <div class="mt-1">
                <h5 class="text-muted">Facilities</h5>
                <ul class="clean-list">
                  <li v-for="(f, i) in department.selectedDepartment.facilities" :key="i">
                    {{ f }}
                  </li>
                </ul>
              </div>
            </div>

          </div>
          <hr>
          <div class="mt-4">
            <h6 class="section-title">Contact</h6>

            <div class="row text-muted small">

              <div class="col-md-4" v-if="department.selectedDepartment.phone" style="font-size: 0.85rem;">
                
                <Phone :size="20"/>
                {{ department.selectedDepartment.phone }}
            
              </div>

              <div class="col-md-4" v-if="department.selectedDepartment.email">
                <Mail :size="20"/>
                {{ department.selectedDepartment.email }}
              </div>

              <div class="col-md-4" v-if="department.selectedDepartment.building">
                 <MapPinHouse :size="20"/>

                {{ department.selectedDepartment.building }}
                <span v-if="department.selectedDepartment.floor">
                    
                  , Floor {{ department.selectedDepartment.floor }}
                </span>
              </div>

            </div>
          </div>

        </div>

      </div>

    </div>

  </div>
</template>

<style scoped>
.clean-list {
  padding-left: 18px;
  margin: 0;
}

.clean-list li {
  font-size: 14px;
  color: #374151;
  margin-bottom: 6px;
}
.icon-wrapper-lg {
  width: 64px;
  height: 64px;
  background: #f3f4f6;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-wrapper-lg svg {
  width: 32px;
  height: 32px;
}

</style>