<template>
  <div
    class="vacanci__item"
    v-for="vacancies in validVacancies"
    :key="vacancies.id"
  >
    <router-link
      class="vacancy__link"
      :to="{
        name: 'vacancyPage',
        params: {
          id: vacancies.id,
          vacName: vacancies.title,
          // vacLink: vacancies.link_vacancy,
        },
      }"
    >
      <main-text
        class="vacanci__title"
        :fontFamily="'montSer'"
        :fontSize="16"
        :fontWeight="500"
      >
        {{ vacancies.title }}
      </main-text>
      <main-text
        class="vacanci__title vacanci__title_link"
        :fontFamily="'montSer'"
        :fontSize="16"
        :fontWeight="500"
      >
        {{ vacancies.link_vacancy }}
      </main-text>
      <main-text
        class="vacanci__title_time"
        :fontFamily="'montSer'"
        :fontSize="16"
        :fontWeight="500"
      >
        {{ formateDate(vacancies.created_at) }}
      </main-text></router-link
    >
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import { parseISO, format } from 'date-fns';
export default {
  name: 'vacanci-item',
  computed: {
    ...mapGetters(['validVacancies']),
  },
  methods: {
    ...mapActions(['fetchVacancies']),
    formateDate(date) {
      let res = parseISO(date);
      date = res;
      return format(date, 'dd.MM.yyyy');
    },
  },
  async mounted() {
    // this.$store.dispatch('fetchVacancies');
    this.fetchVacancies();
  },
};
</script>

<style lang="scss" scoped>
.vacancy__link {
  display: flex;
  justify-content: space-between;
  padding: 0 10px;
  text-decoration: none;
}
.vacanci {
  &__item {
    margin-top: 35px;
    border: 1px solid #343434;
    border-radius: 5px;
    &:hover {
      box-shadow: 2px 2px 2px 2px grey;
    }
  }
  &__title {
    margin: 15px 0 15px 15px;
    word-break: break-word;
    &_time {
      max-width: 208px;
    }
    &_link {
      max-width: 300px;
    }
  }
}
</style>
