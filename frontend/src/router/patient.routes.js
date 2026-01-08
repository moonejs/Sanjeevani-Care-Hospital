export default [
  {
    path: '/patient',
    component: () => import('@/views/patient/PatientLayoutPage.vue'),
    meta: { role: 'patient' },
    children:[
      {
        path: '',
        redirect: { name: 'patient-dashboard' }
      },
      {
        path:'profile',
        name:'patient-profile',
        component:() => import('@/views/patient/ProfilePage.vue')
      },
      {
        path:'dashboard',
        name:'patient-dashboard',
        component:()=> import('@/views/patient/DashboardPage.vue')
      },
      {
        path:'departments',
        name:'patient-departments',
        component:()=> import('@/views/patient/DepartmentsPage.vue')
      },
      {
        path:'doctors',
        name:'patient-doctors',
        component:()=> import('@/views/patient/DoctorsPage.vue')
      },
      {
        path:'appointments',
        name:'my-appointments',
        component:()=> import('@/views/patient/Appointment/MyAppointmentsPage.vue')
      },
      {
        path:'appointments/new',
        name:'book-appointments',
        component:()=> import('@/views/patient/Appointment/BookAppointmentsPage.vue')
      },
      {
        path:'medical-records/history',
        name:'medical-history',
        component:()=> import('@/views/patient/MedicalHistoryPage.vue')
      },
      {
        path:'medical-records/billing',
        name:'medical-bills',
        component:()=> import('@/views/patient/BillingPage.vue')
      },
      
    ]
  }
]
