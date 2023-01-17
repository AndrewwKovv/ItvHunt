<template>
  <div class="vacanci">
    <AppHeader appTitle="Вакансии"></AppHeader>
    <div class="vacanci__wrapper">
      <div class="vacanci__container">
        <div class="vacanci__head">
          <form action="" class="vacanci__search">
            <input
              type="text"
              class="vacanci__search-inp"
              placeholder="Поиск"
            />
          </form>

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
        <vacanci-item></vacanci-item>
      </div>
    </div>
  </div>
</template>

<script>
import AppHeader from '../AppHeader.vue';
import VacanciItem from '@/components/AppPage/Application/VacanciItem.vue';

export default {
  name: 'vacanci-page',
  components: { AppHeader, VacanciItem },
  data() {
    return {
      dialogVisible: false,
    };
  },
  methods: {
    showDialog() {
      this.dialogVisible = true;
    },
  },
};
</script>

<style lang="scss" scoped>
.vacanci {
  margin-left: 130px;
  &__wrapper {
    padding: 25px;
  }
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
    justify-content: space-around;
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
