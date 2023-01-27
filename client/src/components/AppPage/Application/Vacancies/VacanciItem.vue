<template>
  <div class="vacanci__item">
    <router-link
      class="vacancy__link"
      :to="{
        name: 'vacancyPage',
        params: {
          id: vacancies_data.id,
          vacName: vacancies_data.title,
          // vacLink: vacancies.link_vacancy,
        },
      }"
    >
      <div class="vacanci__data">
        <main-text
          class="vacanci__title"
          :fontFamily="'montSer'"
          :fontSize="16"
          :fontWeight="500"
        >
          {{ vacancies_data.title }}
        </main-text>
      </div>
      <div class="vacanci__data">
        <main-text
          class="vacanci__title vacanci__title_link"
          :fontFamily="'montSer'"
          :fontSize="16"
          :fontWeight="500"
        >
          {{ vacancies_data.link_vacancy }}
        </main-text>
      </div>
      <div class="vacanci__data">
        <main-text
          class="vacanci__title_time"
          :fontFamily="'montSer'"
          :fontSize="16"
          :fontWeight="500"
        >
          {{ formateDate(vacancies_data.created_at) }}
        </main-text>
      </div></router-link
    >
  </div>
</template>

<script>
import { parseISO, format } from 'date-fns';
export default {
  name: 'vacanci-item',
  props: {
    vacancies_data: {
      type: Object,
      default: () => {
        return {};
      },
    },
  },
  methods: {
    formateDate(date) {
      let res = parseISO(date);
      date = res;
      return format(date, 'dd.MM.yyyy');
    },
  },
};
</script>

<style lang="scss" scoped>
.vacancy__link {
  display: flex;
  justify-content: space-between;
  padding: 0 10px;
  text-decoration: none;
  align-items: center;
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
    // &_time {
    //   max-width: 208px;
    // }
    // &_link {
    //   max-width: 300px;
    // }
  }
  &__data {
    width: 100%;
    &:last-child {
      text-align: right;
    }
  }
}
</style>
