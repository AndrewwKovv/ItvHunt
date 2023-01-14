<template>
  <div class="modal" v-if="show" @click="hideDialog">
    <div class="modal__content" @click.stop v-if="myPadeDate.feedback">
      <main-text
        class="modal__logo-wrapper"
        :fontFamily="'montSer'"
        :fontSize="24"
        :fontWeight="600"
      >
        <img
          src="@/assets/header_logo.svg"
          alt="Logo"
          class="modal__logo__img"
        />
        {{ myPadeDate.feedback.modalka.title }}
      </main-text>
      <form @submit.prevent class="modal__form">
        <input
          v-model="first_name"
          class="modal__form-content"
          name="name"
          type="text"
          placeholder="Имя"
        />
        <input
          v-model="vacan"
          class="modal__form-content"
          name="vacan"
          type="text"
          placeholder="Должность"
        />
        <textarea
          rows="45"
          cols="45"
          v-model="descriptions"
          class="modal__form-content modal__form-content_textarea"
          name="desc"
          type="text"
          placeholder="Отзыв"
        ></textarea>
      </form>
      <div class="modal__btn">
        <my-button class="btn__save" @click="hideDialog"
          ><main-text
            class="btn__save-text"
            :fontFamily="'montSer'"
            :fontSize="18"
            :fontWeight="500"
            :color="'#1E1E1E'"
            >{{ myPadeDate.feedback.modalka.btn }}</main-text
          ></my-button
        >
      </div>
      <main-text
        class="btn__save-text"
        :fontFamily="'montSer'"
        :fontSize="14"
        >{{ myPadeDate.feedback.modalka.disc }}</main-text
      >
    </div>
  </div>
</template>

<script>
export default {
  name: 'feedback-modal',
  props: {
    show: {
      type: Boolean,
      default: false,
    },
    myPadeDate: Object,
  },
  methods: {
    hideDialog() {
      this.$emit('update:show', false);
    },
  },
};
</script>

<style lang="scss" scoped>
.alert {
  margin: 5px;
  padding: 5px;
}
.modal {
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 9999;
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
    margin: 15px 0;
    &-content {
      background: none;
      color: white;
      outline: none;
      border: 1.5px solid #9c53d5;
      border-radius: 8px;
      height: 40px;
      min-width: 300px;
      padding-left: 10px;
      margin: 5px 0;
      &_textarea {
        height: 100px;
        padding: 5px;
      }
    }
  }
  &__btn {
    text-align: center;
  }
}
.btn__save {
  margin: 15px 0;
  background: #4dd362;
  text-align: center;
  height: 35px;
  &-text {
    text-align: center;
  }
}
</style>
