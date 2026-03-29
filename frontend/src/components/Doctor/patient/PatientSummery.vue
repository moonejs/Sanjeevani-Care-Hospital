<script setup>
    defineProps({
        patient:Object
    })
</script>

<template>
  <div class="mb-3 text-muted">
    <div class="row">
      <div class="col v">
          <img v-if="patient.profile_image" :src="patient.profile_image" class=" border border-4"/>
      </div> 
      <div class="col mt-3">
        <div class="mb-1">
         <span><span>Name : </span><span class="fw-bold h5"> {{ patient.name }}</span></span>
        </div>
        <div class="mb-1 text-capitalize">
          <span>Age : </span><b>{{ patient.age }}</b>
        </div>
      <div class="mb-1 text-capitalize">
        <span>Gender : </span><b>{{ patient.gender }}</b>
      </div>
      <div class="mb-1 text-capitalize">
        <span>Blood : </span><b class="text-danger">{{ patient.blood_group }}</b>
      </div>
      </div>
    </div>
   
    <hr>

    <div class="row">
      <div class="col">
        <div class="info-row"><span>Height : </span><b>{{ patient.height_cm }} cm</b></div>
        <div class="info-row"><span>Weight : </span><b>{{ patient.weight_kg }} kg</b></div>
      </div>
      <div class="col">
        <div class="info-row"><span>Phone : </span><b>{{ patient.contact }}</b></div>
        <div class="info-row"><span>Email : </span><b>{{ patient.email }}</b></div>
      </div>
    </div>
  </div>
  <hr>
</template>

<style scoped>
.v img{
    width: 10rem;
    height: 10rem;
    object-fit: cover;
}
</style>