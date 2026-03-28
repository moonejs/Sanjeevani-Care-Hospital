<script setup>
    import Btn from '../common/Btn.vue';
    import { watch,onMounted,computed } from 'vue';
    import { departmentIcons } from "@/utils/departmentIcons"
    import Badge from '../common/Badge.vue';
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

    const iconComponent = computed(() => {
        const icon = departmentIcons.find(i => i.key === props.department?.icon)
        return icon ? icon.component : null
    })

   
</script>
<template>
  <div class="offcanvas offcanvas-end" tabindex="-1" id="appointmentOffcanvas">
    <div class="offcanvas-header border-bottom">
      <div class="d-flex gap-2 align-items-center">
        <component :is="iconComponent" class="text-primary " style="width:40px;height:40px"/>
        <h5 class="offcanvas-title">{{ department?.name }}</h5>

        <div class="d-flex gap-1">
          <Badge :label="department?.emergency_available ? 'Emergency' : 'No Emergency'" :color="department?.emergency_available ? 'success' : 'danger'"/>

          <Badge :label="department?.is_active ? 'Active' : 'Not Active'" :color="department?.is_active ? 'success' : 'danger'"/>

        </div>
      </div>
      <button type="button" class="btn-close" @click="emit('close')" />
    </div>

    <div class="offcanvas-body" v-if="department">
      
      
      <div class="mb-3">
        <p class="mb-2 small text-italic ">{{ department.description || "----" }}</p>

      </div>

      <hr />

      
      <div class="mb-3 ">
        <h6 class="fw-semibold mb-2 text-muted">Services</h6>
        <ul class="list-group">
          <li v-for="(service, i) in department.services" :key="i" class="ms-3  py-1 small ">
             {{ service }}
          </li>
          <li v-if="!department.services?.length" class="text-muted small">
            No services added
          </li>
        </ul>
      </div>

      <hr />

      
      <div class="mb-3">
        <h6 class="fw-semibold mb-2 text-muted">Facilities</h6>
        <ul class="list-group ">
          <li v-for="(facility, i) in department.facilities" :key="i" class="ms-3  py-1 small">
             {{ facility }}
          </li>
          <li v-if="!department.facilities?.length" class="text-muted small">
            No facilities added
          </li>
        </ul>
      </div>

      <hr />

      
      <div class="mb-3">
        <h6 class="fw-semibold mb-2 text-muted">Contact & Location</h6>

        <div class="row g-2 small">
          <div class="col-6">
            <span class="text-muted">Phone</span>
            <div class="fw-semibold small">+91 {{ department.phone || "—" }}</div>
          </div>

          <div class="col-6">
            <span class="text-muted">Email</span>
            <div class="fw-semibold "> <mark>{{ department.email || "—" }}</mark></div>
          </div>

          <div class="col-6">
            <span class="text-muted">Building</span>
            <div class="fw-semibold small">{{ department.building || "—" }}</div>
          </div>

          <div class="col-6">
            <span class="text-muted">Floor</span>
            <div class="fw-semibold small">{{ department.floor ?? "—" }}</div>
          </div>
          <div class="d-flex flex-wrap gap-3">
          <div>
            <small class="text-muted">OPD Timing</small>
            <div class="fw-semibold small">{{ department.opd_timing || "—" }}</div>
          </div>
        </div>
        </div>
      </div>

      <hr />
      <div class="d-flex gap-2 mt-4">
        <Btn label="Close" class="btn-outline-dark btn-sm" @click="emit('close')" />
      </div>
    </div>
  </div>
</template>
