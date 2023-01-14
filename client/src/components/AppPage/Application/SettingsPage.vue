<template>
  <div class="settings">
    <AppHeader appTitle="Настройка профиля"></AppHeader>
    <div class="settings__wrapper">
      <div class="settings__container">
        <main-text
          class="settings__title"
          :fontFamily="'montSer'"
          :fontSize="22"
          :fontWeight="500"
        >
          Андрей
        </main-text>
        <main-text
          class="settings__title"
          :fontFamily="'montSer'"
          :fontSize="20"
          :fontWeight="500"
        >
          login@mail.ru
        </main-text>
        <div class="settings__corrector">
          <label class="settings__label" for="login"
            ><main-text
              class="settings__title"
              :fontFamily="'montSer'"
              :fontSize="14"
              :fontWeight="400"
            >
              Изменить имя
            </main-text></label
          >
          <main-form class="settings__form_input" v-model="link" type="text" />
        </div>
        <main-text
          class="settings__titles"
          :fontFamily="'montSer'"
          :fontSize="18"
          :fontWeight="500"
        >
          Изменить пароль
        </main-text>
        <div class="settings__correctors">
          <div class="settings__correctors_item">
            <label class="settings__label" for="login"
              ><main-text
                class="settings__title"
                :fontFamily="'montSer'"
                :fontSize="14"
                :fontWeight="400"
              >
                Тукущий пароль
              </main-text></label
            >
            <main-form
              class="settings__form_input"
              v-model="link"
              type="text"
            />
          </div>
          <div class="settings__correctors_item">
            <label class="settings__label" for="login"
              ><main-text
                class="settings__title"
                :fontFamily="'montSer'"
                :fontSize="14"
                :fontWeight="400"
              >
                Новый пароль
              </main-text></label
            >
            <main-form
              class="settings__form_input"
              v-model="link"
              type="text"
            />
          </div>

          <div class="settings__correctors_item">
            <label class="settings__label" for="login"
              ><main-text
                class="settings__title"
                :fontFamily="'montSer'"
                :fontSize="14"
                :fontWeight="400"
              >
                Повторите пароль
              </main-text></label
            >
            <main-form
              class="settings__form_input"
              v-model="link"
              type="text"
            />
          </div>
        </div>
        <div class="settings__exit">
          <main-text
            class="settings__exiting"
            :fontFamily="'montSer'"
            :fontSize="14"
            :fontWeight="400"
            @click="this.$router.push('/')"
          >
            выйти
          </main-text>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AppHeader from '../AppHeader.vue';

export default {
  name: 'settings-page',
  components: { AppHeader },
};
</script>

<style lang="scss" scoped>
.settings {
  margin-left: 130px;
  &__exit {
    display: flex;
    flex-direction: row-reverse;
  }
  &__exiting {
    cursor: pointer;
    width: 60px;
    &:hover {
      opacity: 0.8;
    }
  }
  &__wrapper {
    padding: 25px;
  }
  &__container {
    border-radius: 24px;
    background-color: #505050;
    width: 100%;
    padding: 22px;
  }
  &__corrector {
    margin-top: 0;
  }
  &__form_input {
    color: white;
    margin: 5px auto 20px;
    background: none;
    border: 2px solid #9c53d5;
    border-radius: 5px;
    height: 25px;
    width: 200px;
    padding: 5px;
  }
  &__titles {
    margin-bottom: 20px;
  }
  &__title {
    margin-right: 15px;
  }
}
</style>
