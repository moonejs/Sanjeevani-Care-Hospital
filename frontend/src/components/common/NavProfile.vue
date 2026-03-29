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

<!-- <template>
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
</template> -->

<template>
  <div class="dropdown">
    <div class="profile-trigger d-flex align-items-center gap-2"data-bs-toggle="dropdown">
      <span class="profile-name">{{ name }}</span>
      <i class="fa-solid fa-circle-user profile-icon"></i>
    </div>

    <ul class="dropdown-menu profile-dropdown dropdown-menu-end">

      <li>
        <NavLink label="Profile" :route="`/${auth.role}/profile`"/>
      </li>

      <li><hr class="dropdown-divider"></li>

      <li>
        <button class="dropdown-item logout-btn" @click="logout">
          Logout
        </button>
      </li>

    </ul>
  </div>
</template>

<style scoped>

.profile-trigger {
  cursor: pointer;
  padding: 6px 10px;
  border-radius: 8px;
  transition: all 0.2s ease;
}

.profile-trigger:hover {
  background-color: #f1f3f5;
}


.profile-name {
  font-weight: 600;
  font-size: 1rem;
}


.profile-icon {
  font-size: 1.6rem;
}


.profile-dropdown {
  border: 1px solid #e9ecef;
  border-radius: 2px;
  padding: 6px;
  min-width: 180px;
}

.logout-btn {
  border-radius: 6px;
}

.logout-btn:hover {
  background-color: #ffe3e3;
  color: #c92a2a;
}
</style>