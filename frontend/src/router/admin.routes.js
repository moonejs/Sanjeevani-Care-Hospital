export default [
  {
    path: '/admin',
    name: 'admin',
    component: () => import('@/views/admin/AdminDashboardPage.vue'),
    meta: { role: 'admin' }
  }
]
