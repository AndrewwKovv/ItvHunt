/* eslint-disable no-unused-vars */
import { GET, POST, DELETE } from '@/api/axios-api';
export default {
  state: {
    tasks: [],
  },
  getters: {
    validTasks(state) {
      return state.tasks.filter((t) => {
        return t.title;
      });
    },
    allTasks(state) {
      return state.tasks;
    },
  },
  mutations: {
    updateTasks(state, tasks) {
      state.tasks = tasks;
    },
    createTasks(state, newTasks) {
      state.tasks.unshift(newTasks);
    },
  },
  actions: {
    async fetchTasks(ctx) {
      const response = await GET(`/api/task/tasks/`);
      ctx.commit('updateTasks', response.data);
    //   console.log(response);
    },
    async addTasks(ctx, payload) {
      const response = await POST(`/api/task/`, payload);
      ctx.commit('createTasks', response.data);
      ctx.dispatch('fetchTasks');
    //   console.log(response.data);
    },
    async deleteTask(ctx, payload) {
      const response = await DELETE()
    },
  },
};
