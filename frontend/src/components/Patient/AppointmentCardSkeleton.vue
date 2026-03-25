<template>
  <div class=" mb-3 p-3">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <div class="d-flex align-items-center gap-3">
        
        <div class="placeholder-glow">
          <span class="placeholder rounded-circle" style="width:50px; height:50px;"></span>
        </div>

        
        <div class="placeholder-glow">
          <div class="mb-1">
            <span class="placeholder col-6" style="height:18px; width:90px;"></span>
          </div>
          <div class="mb-1">
            <span class="placeholder col-4" style="height:8px; width:60px;"></span>
          </div>
          <div>
            <span class="placeholder col-3" style="height:8px; width:40px;"></span>
          </div>
        </div>
      </div>

      <div class="placeholder-glow">
        <span class="placeholder " style="height:24px; width:90px;"></span>
      </div>
    </div>

   
    <div class="mb-2"> 
      <div class="d-flex flex-wrap gap-1 mt-3 placeholder-glow">
        <span v-for="i in 12" :key="'m'+i"
          class="placeholder rounded-1"
          style="width:50px; height:22px;">
        </span>
      </div>
    </div>
    <div class="mb-2"> 
      <div class="d-flex flex-wrap gap-1 mt-2 placeholder-glow">
        <span v-for="i in 14" :key="'m'+i"
          class="placeholder rounded-1"
          style="width:50px; height:22px;">
        </span>
      </div>
    </div>
    <div class="mb-3"> 
      <div class="d-flex flex-wrap gap-1 mt-2 placeholder-glow">
        <span v-for="i in 10" :key="'m'+i"
          class="placeholder rounded-1"
          style="width:50px; height:22px;">
        </span>
      </div>
    </div>

    
    
  </div>
</template>