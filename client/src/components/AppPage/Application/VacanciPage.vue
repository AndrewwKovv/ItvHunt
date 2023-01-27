<template>
  <div class="vacanci">
    <AppHeader appTitle="Вакансии"></AppHeader>
    <div class="vacanci__wrapper">
      <VacanciesTable :vacancy_data="validVacancies" />
    </div>
  </div>
</template>

<script>
import AppHeader from '../AppHeader.vue';
import VacanciesTable from './Vacancies/VacanciesTable.vue';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'vacanci-page',
  components: { AppHeader, VacanciesTable },
  data() {
    return {};
  },
  methods: {
    ...mapActions(['fetchVacancies']),
  },
  computed: {
    ...mapGetters(['validVacancies']),
  },
  async mounted() {
    // this.$store.dispatch('fetchVacancies');
    this.fetchVacancies();
  },
};
</script>

<style lang="scss" scoped>
.vacanci {
  margin-left: 130px;
  min-height: 100vh;
  &__wrapper {
    padding: 25px;
  }
}
</style>
