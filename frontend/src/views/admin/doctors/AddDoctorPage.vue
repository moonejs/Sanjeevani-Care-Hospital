<script setup>
    import { ref, watch } from 'vue';
    import { addDoctorApi ,departmentDetailsApi } from '@/api/admin';
    

    const email = ref("")
    const password = ref("")
    const name = ref("")
    const specialization = ref("")
    const department_id = ref("")
    const contact=ref("")
    const departments=ref([])

    async function departmentDetails(){
        try {
            const res = await departmentDetailsApi()
            
            departments.value=res.data
            
            
        } catch (error) {
            console.log(error);
            
        }
    }
    
    
    departmentDetails()
    

    async function addDoctor(){
        
        try{
            await addDoctorApi({
                email:email.value,
                password:password.value,
                name:name.value,
                contact:contact.value,
                specialization:specialization.value,
                department_id:department_id.value,
            })
            
            console.log("doctor added successfully");
            
        }
        catch(err){
            console.log(err);
            
        }
    }

    function canAddDoctor(){
        addDoctor()
    }


</script>

<template>
    <div class="container border p-5 mt-6">

        <form @submit.prevent="canAddDoctor" class="row g-3">
            <div class="col-md-6">
                <label for="inputEmail4" class="form-label">Email</label>
                <input type="email" placeholder="doctor@hospital.com" class="form-control" v-model="email" id="inputEmail4">
            </div>
            <div class="col-md-6">
                <label for="inputPassword4" class="form-label">Password</label>
                <input type="password" class="form-control" placeholder="password" v-model="password" id="inputPassword4">
            </div>
            <div class="col-12">
                <label for="inputAddress" class="form-label">Full Name</label>
                <input type="text" class="form-control" id="inputAddress" v-model="name" placeholder="Dr.Chaman">
            </div>
            <div class="col-12">
                <label for="inputAddress1" class="form-label">Contact</label>
                <input type="number" class="form-control" id="inputAddress1" v-model="contact" placeholder="+91 8888888">
            </div>
            <div class="col-12">
                <label for="specialization" class="form-label">Specialization</label>
                <input type="text" class="form-control" id="specialization" v-model="specialization" placeholder="Brain Doctor">
            </div>
            <div class="col-md-4">
            <label for="inputState" class="form-label">Department</label>
            <select v-model="department_id" id="inputState" class="form-select">
                <option selected value="">Choose...</option>
                <option v-for="dept in departments" :key="dept.id" :value="dept.id">{{ dept.name }}</option>
        </select>
        </div>
        
        <div class="col-12">
            <button type="submit" class="btn btn-primary">Add Doctor</button>
        </div>
    </form>
</div>
</template>