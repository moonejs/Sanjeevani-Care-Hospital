import LandingPage from '@/views/LandingPage.vue'

export default [
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/views/NotFoundPage.vue')
  }
]