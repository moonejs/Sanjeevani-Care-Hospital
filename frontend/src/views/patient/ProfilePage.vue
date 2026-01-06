<script setup>
import { ref, watch } from 'vue';
import { patientProfile } from '@/api/patient';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';

const name=ref("")
const age=ref("")
const gender=ref("")
const contact=ref("")
const address=ref("")
const loading=ref(false)
const disabled=ref(false)

const router=useRouter()
const auth=useAuthStore()

const gender1="Male"
const gender2="Female"


async function profileUpdate(){
    try{
        const res=await patientProfile({
            name:name.value,
            age:age.value,
            gender:gender.value,
            contact:contact.value,
            address:address.value

        
        })
        await auth.fetchMe()
        router.push('/patient/dashboard')
    }catch (err){
        console.log(err);        
    }
}

function canUpdate(){
    if(name.value && age.value && gender.value && contact.value ){
        profileUpdate()
    }else{
        console.log("errorr");
        
    }
}

</script>

<template>
    <div class="container">
        <h1>Edit your profile</h1>
        <form @submit.prevent="canUpdate">
                        <div class="form-group mb-4">
                            <label for="name">Full Name</label>
                            <div class="input-group">
                                <span class="input-group-text" id="basic-addon1"><span class="fas fa-envelope"></span></span>
                                <input type="text" class="form-control" placeholder="Ramesh" v-model.trim="name"
                                required id="name"  >
                            </div>
                        </div>
                        <div class="form-group mb-4">
                            <label for="age">Age</label>
                            <div class="input-group ">
                                <span class="input-group-text" id="basic-addon2"><span class="fas fa-unlock-alt"></span></span>
                                <input required type="number" 
                                v-model.trim="age"
                                placeholder="Age" class="form-control" id="age" />
                            </div>
                        </div>
                        <div class="form-group">
                            <div class="form-check ">
                                <input class="form-check-input" type="radio" v-model="gender" :value="gender1" id="gender1">
                                <label class="form-check-label" for="gender1">
                                    Male
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" v-model="gender" :value="gender2" id="gender2" >
                                <label class="form-check-label" for="gender2">
                                    Female
                                </label>
                            </div>
                        </div>
                        
                            
                        <div class="form-group mb-4">
                            <label for="contact">Contact</label>
                            <div class="input-group">
                                <span class="input-group-text" id="basic-addon2"><span class="fas fa-unlock-alt"></span></span>
                                <input required type="number" 
                                v-model.trim="contact"
                                placeholder="Contact" class="form-control" id="contact"/>
                                
                            </div>
                            
                        </div>
                        <div class="form-group mb-4">
                            <label for="address">Address</label>
                            <div class="input-group">
                                <span class="input-group-text" id="basic-addon2"><span class="fas fa-unlock-alt"></span></span>
                                <input required type="text" 
                                v-model.trim="address"
                                placeholder="Address" class="form-control" id="address" />
                            </div>
                            
                        </div>
                        <div class="d-grid">
                            <button type="submit"  :disabled="disabled" class="btn btn-primary">
                                <span v-if="loading">
                                    <span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
                                    <span class="ml-1">Updating...</span>
                                </span>
                                <span v-else>
                                    Update
                                </span>
                            </button>
                        </div>
                    </form>
        
    </div>
    
</template>