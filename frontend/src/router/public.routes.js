
export default [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/LandingPage.vue')
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'notFound',
    component: () => import('@/views/NotFoundPage.vue')
  }
]