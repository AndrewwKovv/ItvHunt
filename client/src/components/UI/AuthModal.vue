<template>
  <div class="modal" v-if="show" @click="hideDialog">
    <div class="modal__content" @click.stop>
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
        {{ myPadeDate.intro.desc.title }}
      </main-text>
      <form @submit.prevent class="modal__form">
        <input
          v-model="login"
          class="modal__form-content"
          name="email"
          type="text"
          placeholder="Почта"
        />
        <input
          v-model="password"
          class="modal__form-content"
          name="password"
          type="password"
          placeholder="Пароль"
        />
        <div class="model__msg-error alert" role="alert" v-if="errored">
          <main-text
            class="modal__logo-wrapper"
            :fontFamily="'montSer'"
            :fontSize="16"
            :fontWeight="500"
            >{{ myPadeDate.auth.error }}
          </main-text>
        </div>
      </form>
      <div class="modal__btn">
        <button type="button" @click="isValidAuth" class="btn btn-dark">
          <main-text
            class="btn__save"
            :fontFamily="'montSer'"
            :fontSize="22"
            :fontWeight="500"
            >Войти</main-text
          >
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'auth-modal',
  data() {
    return {
      login: '',
      password: '',
      errored: false,
    };
  },
  props: {
    myPadeDate: Object,
    show: {
      type: Boolean,
      default: false,
    },
    modelValue: [String, Number],
  },
  methods: {
    hideDialog() {
      this.$emit('update:show', false);
    },
    isValidAuth() {
      if ((this.login === 'login@mail.ru', this.password === '0000')) {
        this.$router.push('/vacanci');
      } else {
        this.errored = true;
      }
    },
    updateInput(event) {
      this.$emit('update:modelValue', event.target.value);
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
  z-index: 999;
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
    }
  }
  &__btn {
    text-align: center;
  }
}
</style>
