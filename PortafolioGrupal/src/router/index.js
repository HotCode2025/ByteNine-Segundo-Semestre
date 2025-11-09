import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/member/:id',
    name: 'member',
    component: () => import('@/components/MemberProfile.vue'),
    props: true  // Esto pasa el parámetro :id como prop
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router