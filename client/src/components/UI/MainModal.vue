<template>
  <div class="modal" v-if="show" @click="hideDialog">
    <div class="modal__content" @click.stop>
      <main-text :fontFamily="'montSer'" :fontSize="26" :fontWeight="500"
        >{{ myPadeDate.regis.title }}
      </main-text>
      <form @submit.prevent class="modal__form" method="post">
        <select class="content__form">
          <option selected disabled>Выберите деятельность</option>
          <option value="Компания HR">Компания HR</option>
          <option value="Кандидат">Кандидат</option>
        </select>
        <input
          class="content__form"
          name="Name"
          type="text"
          placeholder="Ваше имя"
        />
        <input
          class="content__form"
          name="email"
          type="text"
          placeholder="Почта"
        />
        <input
          class="content__form"
          name="password"
          type="text"
          placeholder="Пароль"
        />
      </form>
      <div class="modal__content-accept">
        <div for="btn-acceptt" class="modal__content-p">
          <main-text :fontFamily="'montSer'" :fontSize="14"
            >{{ myPadeDate.regis.text.start }}
            <a href="#" class="modal__link">{{ myPadeDate.regis.text.pols }}</a>
            {{ myPadeDate.regis.text.and }}
            <a href="#" class="modal__link">{{
              myPadeDate.regis.text.policy
            }}</a></main-text
          >
        </div>
      </div>
      <div class="modal__btn">
        <my-button class="btn__save" type="submit" @click="onClick"
          ><main-text
            :fontFamily="'montSer'"
            :fontSize="22"
            :fontWeight="500"
            :color="'#1E1E1E'"
            >Зарегистрироваться</main-text
          ></my-button
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'main-modal',
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
    onClick() {
      if (this.post.body === this.falseBody) {
        console.log('!');
      } else {
        this.$emit('update:show', false);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
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
    min-height: 170px;
    min-width: 270px;
    padding: 35px;
    &-p {
      max-width: 400px;
    }
  }
  &__form {
    display: flex;
    flex-direction: column;
    margin: 15px 0;
  }
  &__link {
    color: #ffffff;
  }
  &__btn {
    text-align: center;
  }
}
.content {
  &__form {
    background: none;
    color: white;
    outline: none;
    border: 1.5px solid #9c53d5;
    border-radius: 8px;
    height: 40px;
    padding-left: 10px;
    margin: 5px 0;
    &_text {
      color: #1e1e1e;
    }
  }
}
.btn__save {
  margin: 15px 0;
  background: #4dd362;
  text-align: center;
}
</style>
