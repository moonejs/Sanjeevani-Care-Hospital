<script setup>
    import { useAuthStore } from '@/stores/auth.store';
    import NavLink from './NavLink.vue';
    import { useRouter } from 'vue-router';
    import { computed } from 'vue';

    const props=defineProps({
        role:String
    })

    const auth=useAuthStore()
    const route=useRouter()
    
    const name = computed(()=>{
        const nm= auth.user.name ? auth.user.name.charAt(0).toUpperCase() + auth.user.name.slice(1).toLowerCase() 
        : "New user"  
        console.log(auth.role);
        console.log(auth.user);
        
        if(auth.role ==='doctor'){
            return "Dr. " + nm
        }
        else{
            return nm
        }
    })



    function logout(){
        auth.logout()
        route.replace('/')
    }
    
</script>

<template>
    <div class="dropstart">
        <a class="d-flex align-items-center gap-2 dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            <h3>{{ name }}</h3>
            <i class="fa-solid fa-circle-user fs-4 mb-1"></i>
        </a>
        <ul class="dropdown-menu">
            <li>
                <NavLink label="Profile" :route="`/${role}/profile`"/>
            </li>
            <li><hr class="dropdown-divider"></li>
            <li>
                <a class="dropdown-item" @click="logout">Logout</a>
            </li>
        </ul>
    </div>
</template>