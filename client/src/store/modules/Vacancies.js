// import axios from 'axios';

export default {
  state: {
    vacancies: [],
  },
  getters: {
    validVacancies(state) {
      return state.vacancies.filter((v) => {
        return v.title && v.link;
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
    async fetchVacancies() {
      // axios
      // .get('/main.json')
      // .then((response) => {
      //   ctx.commit('updateVacancies', response.data.vacancies);
      // });
    },
  },
};
