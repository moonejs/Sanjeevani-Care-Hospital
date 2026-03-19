<script setup>
    import BaseTable from '@/components/layout/BaseTable.vue';
    import BaseTableHead from '@/components/layout/BaseTableHead.vue';
    import { ref,computed } from 'vue';
    import Btn from '@/components/common/Btn.vue';
    import DoctorDashTableCaption from '@/components/Doctor/DoctorDashTableCaption.vue';
    
  
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
      <DoctorDashTableCaption title="Appointment History" v-model:searchQuery="searchQuery" v-model:date-filter="dateFilter" :is-date="true"/>
      <Btn  label="Clear" class="btn-primary "  @click="searchQuery = '';dateFilter=''"/>
    </template>

    <template #head>
      <BaseTableHead :t-head="tHead" />
    </template>

    <template #body >
      <template  v-for="(appt, i) in filteredData" :key="appt.id">
        
        <tr>
          <td>{{ i + 1 }}</td>
          <td>{{ appt.date }}</td>
          <td>{{ appt.time }}</td>
          <td>{{ appt.type }}</td>
          <td>
            <span
              :class="{
                'text-success': appt.status === 'completed',
                'text-warning': appt.status === 'pending',
                'text-primary': appt.status === 'confirmed',
                'text-danger': appt.status === 'cancelled'
              }"
            >
              {{ appt.status }}
            </span>
          </td>
          <td>
            <Btn class="btn-sm btn-primary" @click="toggle(appt.id)" :label="expandedId === appt.id ? 'Hide' : 'View'">
              
            </Btn>
          </td>
        </tr>
        <tr v-if="expandedId === appt.id">
          <td colspan="6">
            <div class="p-3 bg-warning">

              <div v-if="appt.treatment">
                <p><b>Diagnosis:</b> {{ appt.treatment.diagnosis }}</p>
                <p><b>Notes:</b> {{ appt.treatment.notes || '—' }}</p>

                <div v-if="appt.treatment.medicines?.length">
                  <b>Medicines:</b>
                  <ul>
                    <li
                      v-for="(m, idx) in appt.treatment.medicines"
                      :key="idx"
                    >
                      {{ m.name }} – {{ m.dose }} – {{ m.frequency }}
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
