export default [
  {
    path: '/doctor',
    component: () => import('@/views/doctor/DoctorLayoutPage.vue'),
    meta: { role: 'doctor' },
    children:[
      {
        path: '',
        redirect: { name: 'dashboard-doctor' }
      },
      {
        path:'dashboard',
        name:'dashboard-doctor',
        component:()=> import('@/views/doctor/DashboardPage.vue')
      },
      {
        path:'appointments',
        name:'appointments-doctor',
        component:()=> import('@/views/doctor/AppointmentsPage.vue')
      },
      {
        path:'schedule',
        name:'schedule-doctor',
        component:()=> import('@/views/doctor/SchedulePage.vue')
      },
      {
        path:'patients',
        children:[
          {
            path:"",
            name:'patients-doctor',
            component:()=> import('@/views/doctor/patient/PatientsPage.vue')
          },
          {
            path:":id",
            name:'patientProfile-doctor',
            component:()=>import('@/views/doctor/patient/PatientProfilePage.vue'),
            props:true
          }
        ]
      },
      {
        path:'profile',
        component:()=>import('@/views/doctor/profile/ProfilePageLayout.vue'),
        

      }

    ]
  }
]
