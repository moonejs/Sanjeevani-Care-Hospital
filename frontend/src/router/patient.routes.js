export default [
  {
    path: '/patient',
    component: () => import('@/views/patient/PatientLayoutPage.vue'),
    meta: { role: 'patient' },
    children:[
      {
        path:'profile',
        name:'patient-profile',
        component:() => import('@/views/patient/ProfilePage.vue')
      },
      {
        path:'dashboard',
        name:'patient-dashboard',
        component:()=> import('@/views/patient/DashboardPage.vue')
      }
    ]
  }
]
