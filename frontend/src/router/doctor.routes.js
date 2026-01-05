export default [
  {
    path: '/doctor',
    name: 'doctor',
    component: () => import('@/views/doctor/DoctorDashboardPage.vue'),
    meta: { role: 'doctor' }
  }
]
