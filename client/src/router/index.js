import { createRouter, createWebHashHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/components/MainPage/MyPage.vue'),
  },
  {
    path: '/applications',
    name: 'applications',
    props: true,
    component: () => import('@/components/AppPage/Applications.vue'),
    children: [
      {
        path: '/candidates',
        name: 'candidates',
        props: true,
        component: () =>
          import('@/components/AppPage/Application/CandidatesPage.vue'),
      },
      {
        path: '/tasks',
        name: 'tasks',
        props: true,
        component: () =>
          import('@/components/AppPage/Application/TasksPage.vue'),
      },
      {
        path: '/templates',
        name: 'templates',
        props: true,
        component: () =>
          import('@/components/AppPage/Application/TemplatesPage.vue'),
      },
      {
        path: '/vacanci',
        name: 'vacanci',
        props: true,
        component: () =>
          import('@/components/AppPage/Application/VacanciPage.vue'),
      },
      {
        path: '/vacanci/:id:vacName:vacLink',
        name: 'vacancyPage',
        props: true,
        component: () =>
          import('@/components/AppPage/Application/Vacancies/Vacancy.vue'),
      },
      {
        path: '/settings',
        name: 'settings',
        props: true,
        component: () =>
          import('@/components/AppPage/Application/SettingsPage.vue'),
      },
    ],
  },
  // {
  //   path: '/printJson',
  //   name: 'enterJson',
  //   component: () => import('@/views/printJson.vue'),
  // },
  {
    path: '/404',
    name: '404',
    component: () => import('@/views/erroe.vue'),
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/404',
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
