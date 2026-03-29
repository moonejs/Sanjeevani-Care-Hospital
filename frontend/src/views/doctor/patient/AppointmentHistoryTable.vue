<script setup>
    import BaseTable from '@/components/layout/BaseTable.vue';
    import BaseTableHead from '@/components/layout/BaseTableHead.vue';
    import { ref,computed } from 'vue';
    import Btn from '@/components/common/Btn.vue';
    import DoctorDashTableCaption from '@/components/Doctor/DoctorDashTableCaption.vue';
    import Badge from '@/components/common/Badge.vue';
    
  
    import { useSearchFilter } from '@/utils/useSearchFilter';
    import { useDoctorStore } from '@/stores/doctor.store'

    const props=defineProps({
        appointments: Array
    })

    const doctoStore=useDoctorStore()
    const dateFilter=ref('')

    const appointmentList = computed(() => 
        doctoStore.selectedPatient.appointments || []
    )

    const { searchQuery, filteredData } = useSearchFilter(
        appointmentList,
        ['type','status '],
        {
          date:dateFilter
        }
        
    )


    const tHead=ref(["Date","Time","Status","Type","Action"])
    const expandedId = ref(null)

    function toggle(id) {
        expandedId.value = expandedId.value === id ? null : id
    }
</script>

<template>
  <BaseTable>
    <template #caption>
      <DoctorDashTableCaption title="Appointment History" v-model:searchQuery="searchQuery" v-model:date-filter="dateFilter" :is-date="true" class3="d-flex gap-4" class2="gap-9"/>
      <Btn  label="Clear" class="btn-secondary btn-sm position-absolute right-5 me-4 top-8 "  @click="searchQuery = '';dateFilter=''"/>
    </template>

    <template #head>
      <BaseTableHead :t-head="tHead" />
    </template>

    <template #body >
      <template  v-for="(appt, i) in filteredData" :key="appt.id">
        
        <tr class="small">
          <td>{{ i + 1 }}</td>
          <td>{{ appt.date }}</td>
          <td class="mark"> <mark>{{ appt.time }}</mark></td>
          <td :class="appt.type === 'emergency' ? 'text-danger':'text-primary'" class="text-uppercase">
            {{ appt.type }}
          </td>
          <td>
            <Badge :label="appt.status" :color="appt.status === 'completed' ? 'primary' :
            appt.status === 'pending' ? 'warning' : appt.status === 'confirmed' ? 'success' : appt.status === 'cancelled' ? 'danger' : 'secondary' "/>
          </td>
          <td>
            <Btn class="btn-sm btn-outline-secondary" @click="toggle(appt.id)" :label="expandedId === appt.id ? 'Hide' : 'View'">
              
            </Btn>
          </td>
        </tr>
        <tr v-if="expandedId === appt.id">
          <td colspan="6">
            <div class="p-3 v">

              <div v-if="appt.treatment">
                <p>Diagnosis : <span class="small fw-bold">{{ appt.treatment.diagnosis }}</span> </p>
                <p>Notes :  <span class="fw-bold small">{{ appt.treatment.notes || '—' }}</span></p>

                <div v-if="appt.treatment.medicines?.length">
                  Medicines : 
                  <ul>
                    <li
                      v-for="(m, idx) in appt.treatment.medicines"
                      :key="idx"
                    >
                      {{ m.name }} - {{ m.dose }} - {{ m.frequency }}
                    </li>
                  </ul>
                </div>

                <p v-if="appt.treatment.follow_up_date">
                  <b>Follow-up:</b> {{ appt.treatment.follow_up_date }}
                </p>
              </div>

              <p v-else class="text-muted">
                No treatment recorded for this visit
              </p>

            </div>
          </td>
        </tr>

      </template>
    </template>
  </BaseTable>
</template>

<style scoped>
.v{
  background-color: #E5E7EB;
}
</style>