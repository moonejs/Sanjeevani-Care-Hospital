<script setup>
import Btn from '../common/Btn.vue';
    const props=defineProps({
        showModal: Boolean,
        doctor:Object
    })
    const emit =defineEmits(['block','close','unblock'])
</script>
<template>
    <transition name="fade">

        <div v-if="showModal">
            
            <div class="modal fade show" style="display: block;">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                        <h1 class="modal-title fs-5" v-if="doctor.is_blocked" id="exampleModalLabel">
                            You are about to Unblock <b>Dr. {{ doctor.name }}</b> 
                        </h1>
                        <h1 class="modal-title fs-5" v-else id="exampleModalLabel">
                            You are about to block <b>Dr. {{ doctor.name }}</b> 
                        </h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" @click="emit('close')"></button>
                    </div>
                    <div class="modal-body">
                        <div v-if="!doctor.is_blocked">
                            <ul>
                                <li>The doctor will not be able to receive new appointments.</li>
                                <li>All upcoming appointments will be cancelled.</li>
                                <li>Patients will no longer see this doctor for booking.</li>
                            </ul>
                        </div>
                        Are you sure you want to continue?

                    </div>
                    <div class="modal-footer">
                        <Btn label="Close" class="btn-sm btn-primary" @click="emit('close')"/>
                        <Btn v-if="doctor.is_blocked" label="Unblock" class="btn-sm btn-outline-danger" @click="emit('unblock')"/>
                        <Btn v-else label="Block" class="btn-sm animate-up-1 btn-danger" @click="emit('block')"/>
                        
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