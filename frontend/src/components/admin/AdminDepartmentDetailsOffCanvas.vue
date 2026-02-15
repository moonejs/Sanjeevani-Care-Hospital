<script setup>
    import Btn from '../common/Btn.vue';
    import { watch,onMounted } from 'vue';
    const props=defineProps({
        show:Boolean,
        department:Object
    })
    const emit = defineEmits(['close'])

    let instance = null
    let el = null

    onMounted(() => {
      el = document.getElementById('appointmentOffcanvas')
      if (!el) return

      instance = bootstrap.Offcanvas.getOrCreateInstance(el)

      el.addEventListener('hidden.bs.offcanvas', () => {
        emit('close')
      })
    })

    watch(
      () => props.show,
      (val) => {
        if (!instance) return
        val ? instance.show() : instance.hide()
      }
    )

   
</script>
<template>
  <div class="offcanvas offcanvas-end" tabindex="-1" id="appointmentOffcanvas">
    <div class="offcanvas-header border-bottom">
      <div>
        <h5 class="offcanvas-title">{{ department?.name }}</h5>
        <small class="text-muted">Department Details</small>
      </div>
      <button type="button" class="btn-close" @click="emit('close')" />
    </div>

    <div class="offcanvas-body" v-if="department">
      
      
      <div class="mb-3">
        <h6 class="fw-semibold mb-2">Basic Information</h6>
        <div class="small text-muted mb-1">Description</div>
        <p class="mb-2">{{ department.description || "—" }}</p>

        <div class="d-flex flex-wrap gap-3">
          <div>
            <small class="text-muted">Icon</small>
            <div class="fw-semibold">{{ department.icon }}</div>
          </div>
          <div>
            <small class="text-muted">OPD Timing</small>
            <div class="fw-semibold">{{ department.opd_timing || "—" }}</div>
          </div>
        </div>
      </div>

      <hr />

      
      <div class="mb-3">
        <h6 class="fw-semibold mb-2">Services</h6>
        <ul class="list-group list-group-flush">
          <li
            v-for="(service, i) in department.services"
            :key="i"
            class="list-group-item px-0 py-1"
          >
            • {{ service }}
          </li>
          <li v-if="!department.services?.length" class="text-muted small">
            No services added
          </li>
        </ul>
      </div>

      <hr />

      
      <div class="mb-3">
        <h6 class="fw-semibold mb-2">Facilities</h6>
        <ul class="list-group list-group-flush">
          <li
            v-for="(facility, i) in department.facilities"
            :key="i"
            class="list-group-item px-0 py-1"
          >
            • {{ facility }}
          </li>
          <li v-if="!department.facilities?.length" class="text-muted small">
            No facilities added
          </li>
        </ul>
      </div>

      <hr />

      
      <div class="mb-3">
        <h6 class="fw-semibold mb-2">Contact & Location</h6>

        <div class="row g-2 small">
          <div class="col-6">
            <span class="text-muted">Phone</span>
            <div class="fw-semibold">{{ department.phone || "—" }}</div>
          </div>

          <div class="col-6">
            <span class="text-muted">Email</span>
            <div class="fw-semibold">{{ department.email || "—" }}</div>
          </div>

          <div class="col-6">
            <span class="text-muted">Building</span>
            <div class="fw-semibold">{{ department.building || "—" }}</div>
          </div>

          <div class="col-6">
            <span class="text-muted">Floor</span>
            <div class="fw-semibold">{{ department.floor ?? "—" }}</div>
          </div>
        </div>
      </div>

      <hr />

     
      <div class="mb-3">
        <h6 class="fw-semibold mb-2">Status</h6>

        <div class="d-flex gap-3">
          <span
            class="badge"
            :class="department.emergency_available ? 'bg-success' : 'bg-secondary'"
          >
            Emergency: {{ department.emergency_available ? "Available" : "Not Available" }}
          </span>

          <span
            class="badge"
            :class="department.is_active ? 'bg-success' : 'bg-danger'"
          >
            {{ department.is_active ? "Active" : "Inactive" }}
          </span>
        </div>
      </div>

      
      <div class="d-flex gap-2 mt-4">
        <Btn label="Print" class="btn-outline-secondary btn-sm" />
        <Btn label="Close" class="btn-outline-dark btn-sm" @click="emit('close')" />
      </div>
    </div>
  </div>
</template>
