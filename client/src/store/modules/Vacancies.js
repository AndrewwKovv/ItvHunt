/* eslint-disable no-unused-vars */
import axios from 'axios';
import { GET, POST } from '@/api/axios-api';
export default {
  state: {
    vacancies: [],
  },
  getters: {
    validVacancies(state) {
      return state.vacancies.filter((v) => {
        return v.title;
      });
    },
    allVacancies(state) {
      return state.vacancies;
    },
  },
  mutations: {
    updateVacancies(state, vacancies) {
      state.vacancies = vacancies;
    },
    createVacancies(state, newVacancies) {
      state.vacancies.unshift(newVacancies);
    },
  },
  actions: {
    async fetchVacancies(ctx) {
      const response = await GET(`/api/vacancy/`);
      // this.vacancies = response.data.results;
      ctx.commit('updateVacancies', response.data.vacancies);
      // console.log(response.data);
    },
    async addVacancies(ctx, payload) {
      const response = await POST(`/api/vacancy/`, payload);
      ctx.commit('createVacancies', response.data);
      ctx.dispatch('fetchVacancies');
      // console.log(response.data);
    },
  },
};
