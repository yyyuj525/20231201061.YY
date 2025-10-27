import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import EntryList from '../views/EntryList.vue'
import EntryDetail from '../views/EntryDetail.vue'
import CategoryList from '../views/CategoryList.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/entries',
    name: 'EntryList',
    component: EntryList
  },
  {
    path: '/entries/:id',
    name: 'EntryDetail',
    component: EntryDetail,
    props: true
  },
  {
    path: '/categories',
    name: 'CategoryList',
    component: CategoryList
  },
  {
    path: '/categories/:id/entries',
    name: 'CategoryEntries',
    component: EntryList,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router