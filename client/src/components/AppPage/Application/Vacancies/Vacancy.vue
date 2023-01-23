<template>
  <div class="vacancy">
    <AppHeader appTitle="Вакансия"></AppHeader>
    <div class="vacancy__wrapper">
      <button type="button" class="btn btn-secondary">
        <main-text
          class="vacancy__back"
          :fontFamily="'montSer'"
          :fontSize="16"
          :fontWeight="500"
          @click="this.$router.push('/vacanci')"
        >
          Назад
        </main-text>
      </button>

      <div class="vacancy__container">
        <main-text
          class="vacancy__title"
          :fontFamily="'montSer'"
          :fontSize="18"
          :fontWeight="500"
        >
          {{ title }}
        </main-text>
        <main-text
          class="vacancy__title"
          :fontFamily="'montSer'"
          :fontSize="18"
          :fontWeight="500"
        >
          <a href="/${link}">{{ link }}</a>
        </main-text>
        <my-button class="vacancy__btn" @click="showDialog">
          <main-text
            class="vacancy__subtitle"
            :fontFamily="'montSer'"
            :fontSize="14"
            :fontWeight="500"
          >
            редактировать
          </main-text>
        </my-button>
        <change-modal
          v-model:show="dialogVisible"
          :nameVacy="title"
        ></change-modal>
      </div>
    </div>
  </div>
</template>

<script>
import AppHeader from '@/components/AppPage/AppHeader.vue';

export default {
  name: 'vacancy-place',
  components: { AppHeader },
  data() {
    return {
      title: '',
      link: '',
      dialogVisible: false,
    };
  },
  props: {
    vacName: String,
    // vacLink: String,
  },
  methods: {
    getTitleName() {
      this.title = this.$route.params.vacName;
    },
    getLinkAdress() {
      // this.link = this.$route.params.vacLink;
    },
    showDialog() {
      this.dialogVisible = true;
    },
  },
  beforeMount() {
    this.getTitleName();
    this.getLinkAdress();
  },
};
</script>

<style lang="scss" scoped>
.vacancy {
  margin-left: 130px;
  height: 100vh;
  &__wrapper {
    padding: 25px;
  }
  &__container {
    margin-top: 5px;
    border-radius: 24px;
    background-color: #505050;
    width: 100%;
    padding: 22px;
    display: flex;
  }
  &__back {
    cursor: pointer;
    &:hover {
      opacity: 0.8;
    }
  }
  &__btn {
    width: 140px;
    background-color: #4dd362;
  }
  &__title {
    margin-right: 15px;
    color: white;
  }
  &__subtitle {
    margin: auto;
    text-align: center;
  }
}
</style>
