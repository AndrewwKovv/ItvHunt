import { createStore } from 'vuex';
import Vacancies from './modules/Vacancies';
import Tasks from './modules/Tasks';

export default createStore({
  modules: { Vacancies, Tasks },
});
