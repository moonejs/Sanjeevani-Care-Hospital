export default [
  {
    path: '/patient',
    name: 'patient',
    component: () => import('@/views/patient/patientLayoutPage.vue'),
    meta: { role: 'patient' }
  }
]
