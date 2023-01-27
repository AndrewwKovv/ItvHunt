<template>
  <div class="vacanci__container">
    <div class="vacanci__head">
      <input
        type="text"
        class="vacanci__search-inp"
        placeholder="Поиск"
        v-model="searchVacancies"
      />

      <my-button class="contact__button" @click="showDialog">
        <main-text
          class="contact__subtitle"
          :fontFamily="'montSer'"
          :fontSize="16"
          :fontWeight="500"
          >+ добавить вакансию
        </main-text></my-button
      >
      <vacancy-modal v-model:show="dialogVisible" />
    </div>
    <div class="vacanci__title">
      <main-text
        class="vacanci__subtitle"
        :fontFamily="'montSer'"
        :fontSize="14"
        :fontWeight="500"
      >
        название
      </main-text>
      <main-text
        class="vacanci__subtitle"
        :fontFamily="'montSer'"
        :fontSize="14"
        :fontWeight="500"
      >
        ссылка
      </main-text>
      <main-text
        class="vacanci__subtitle"
        :fontFamily="'montSer'"
        :fontSize="14"
        :fontWeight="500"
      >
        добавлена
      </main-text>
    </div>
    <VacanciItem
      v-for="vacancies in searchVacancy"
      :key="vacancies.id"
      :vacancies_data="vacancies"
    />
  </div>
</template>

<script>
import VacanciItem from './VacanciItem.vue';

export default {
  name: 'vacancies-table',
  data() {
    return {
      searchVacancies: '',
      dialogVisible: false,
    };
  },
  props: {
    vacancy_data: {
      type: Array,
      default: () => {
        return [];
      },
    },
  },
  methods: {
    showDialog() {
      this.dialogVisible = true;
    },
  },
  computed: {
    searchVacancy() {
      return this.vacancy_data.filter((vacancy) =>
        vacancy.title.toLowerCase().includes(this.searchVacancies.toLowerCase())  || vacancy.created_at.toLowerCase().includes(this.searchVacancies.toLowerCase())
      );
    },
  },
  components: { VacanciItem },
};
</script>

<style lang="scss" scoped>
.vacanci {
  &__container {
    border-radius: 24px;
    background-color: #505050;
    width: 100%;
    padding: 22px;
  }
  &__head {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
  }
  &__title {
    display: flex;
    margin-top: 75px;
    border: 1px solid #343434;
    border-radius: 5px;
    justify-content: space-between;
    padding: 0 10px;
  }
  &__subtitle {
    margin-left: 15px;
  }
  &__search-inp {
    border: 2px solid #343434;
    border-radius: 10px;
    background-color: #505050;
    max-width: 250px;
    height: 25px;
    padding: 5px;
    color: white;
  }
}
.contact {
  &__button {
    background-color: #4dd362;
    padding: 5px;
    &:hover {
      box-shadow: 0 0 0 2px #4dd362;
    }
  }
}
</style>
