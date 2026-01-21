<script setup>
    import BaseTable from '@/components/layout/BaseTable.vue';
    import BaseTableHead from '@/components/layout/BaseTableHead.vue';
    import { ref } from 'vue';
    import Btn from '@/components/common/Btn.vue';
    defineProps({
        appointments: Array
    })

    const tHead=ref(["Date","Time","Status","Type","Action"])
    const expandedId = ref(null)

    function toggle(id) {
        expandedId.value = expandedId.value === id ? null : id
    }
</script>

<template>
  <BaseTable>
    <template #caption>
      <h5 class="mb-2">Appointment History</h5>
    </template>

    <template #head>
      <BaseTableHead :t-head="tHead" />
    </template>

    <template #body >
      <template  v-for="(appt, i) in appointments" :key="appt.id">
        
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
