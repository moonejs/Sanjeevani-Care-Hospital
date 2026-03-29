<script setup>
    import { ref } from 'vue';
    import Label from '@/components/Form/BaseLabel.vue';
    import Btn from '@/components/common/Btn.vue';
    const props=defineProps({
        showCompleteModal:Boolean,
        patient:Object,
        appointmentId: Number
    })
    const emit=defineEmits([
        'close',
        'submit'
    ])
    const form = ref({
        diagnosis: '',
        notes: '',
        follow_up_date: '',
        medicines: [
            { name: '', dose: '', frequency: '' }
        ]
    })

    function addMedicine(){
        form.value.medicines.push({
            name: '',
            dose: '',
            frequency: ''
        })
    }
    function removeMedicine(index){
        form.value.medicines.splice(index, 1)
    }

    function submitForm(){
        emit('submit', form.value)
    }
</script>

<template>
    <transition name="fade">
        <div v-if="showCompleteModal" class="small">
            <div class="modal fade show" style="display: block;">
                <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">Add Details</h5>
                            <button class="btn-close" @click="emit('close')"></button>
                        </div>
                        <div class="modal-body">
                            <p class="mb-3"><b>Patient:</b> {{ patient?.name }}</p>

                            <Label label="Diagnosis"/>
                            <input v-model="form.diagnosis" class="form-control mb-2" placeholder="Eg. Viral Fever" />

                            <Label label="Doctor Notes"/>
                            <textarea v-model="form.notes" class="form-control mb-2" placeholder="Clinical notes"></textarea>

                            <Label label="Prescribed Medicines"/>
                            <div v-for="(med, index) in form.medicines" :key="index" class="row g-2 mb-2" >
                                <div class="col-md-4">
                                    <input v-model="med.name" class="form-control" placeholder="Medicine name" />
                                </div>

                                <div class="col-md-3">
                                    <input v-model="med.dose" class="form-control" placeholder="Dose" />
                                </div>

                                <div class="col-md-4">
                                    <input v-model="med.frequency" class="form-control" placeholder="Frequency" />
                                </div>
                                <div class="col-md-1 d-flex align-items-center">
                                    <button class="btn btn-outline-danger btn-sm" v-if="form.medicines.length > 1" @click="removeMedicine(index)" > ✕ </button>
                                </div>
                            </div>
                            <Btn label="Add Medicine" class="btn-primary btn-sm d-block my-3" @click="addMedicine" />
                            

                            <Label class="d-inline" label="Follow-up Date"/>
                            <input v-model="form.follow_up_date" type="date" class="form-control mb-2" />
                        </div>
                        <div class="modal-footer">
                            <Btn @click="submitForm" class="btn btn-outline-secondary" label="Complete Appointment" />
                        </div>
                    </div>
                </div>
            </div>
            <div class="modal-backdrop fade show"></div>
        </div>
    </transition>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.25s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>