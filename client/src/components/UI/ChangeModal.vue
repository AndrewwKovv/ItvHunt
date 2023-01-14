<template>
  <div class="vacancy-modal" v-if="show" @click="hideDialog">
    <div class="vacancy-modal__content" @click.stop>
      <main-text
        class="vacanci__title"
        :fontFamily="'montSer'"
        :fontSize="22"
        :fontWeight="500"
      >
        {{ nameVacy }}
      </main-text>
      <form @submit.prevent class="vacancy-modal__form">
        <label class="vacancy__label" for="login"
          ><main-text
            class="vacanci__title"
            :fontFamily="'montSer'"
            :fontSize="12"
            :fontWeight="400"
          >
            изменить название
          </main-text></label
        >
        <main-form class="vacancy__form_input" v-model="title" type="text" />
        <label class="vacancy__label" for="login"
          ><main-text
            class="vacanci__title"
            :fontFamily="'montSer'"
            :fontSize="12"
            :fontWeight="400"
          >
            изменить ссылку
          </main-text></label
        >
        <main-form class="vacancy__form_input" v-model="link" type="text" />
      </form>
      <div class="vacancy-modal__btn">
        <my-button class="btn__save" @click="onClick"
          ><main-text
            class="vacancy-modal__title"
            :fontFamily="'montSer'"
            :fontSize="20"
            :fontWeight="500"
          >
            Изменить
          </main-text></my-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import { mapMutations } from 'vuex';
export default {
  name: 'change-modal',
  data() {
    return {
      title: '',
      link: '',
    };
  },
  props: {
    show: {
      type: Boolean,
      default: false,
    },
    nameVacy: String,
  },
  methods: {
    hideDialog() {
      this.$emit('update:show', false);
    },
    ...mapMutations(['createVacancies']),
    onClick() {
      this.createVacancies({
        title: this.title,
        link: this.link,
        id: Date.now,
        created_at: new Date(),
      });
      this.$emit('update:show', false);
      this.title = '';
      this.link = '';
    },
  },
};
</script>

<style lang="scss" scoped>
.vacancy-modal {
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 10000;
  position: fixed;
  display: flex;
  &__content {
    background-color: #1e1e1e;
    margin: auto;
    border-radius: 10px;
    min-height: 200px;
    min-width: 200px;
    padding: 35px;
  }
  &__form {
    display: flex;
    flex-direction: column;
    margin: 20px auto;
  }
  &__title {
    margin: 2px auto;
  }
}
.btn__save {
  margin: 15px 0;
  background: #4dd362;
  text-align: center;
  height: 35px;
}
.vacancy__form {
  &_input {
    color: white;
    margin: 5px auto 20px;
    background: none;
    border: 2px solid #9c53d5;
    border-radius: 5px;
    height: 35px;
    width: 350px;
    padding: 5px;
  }
}
</style>
