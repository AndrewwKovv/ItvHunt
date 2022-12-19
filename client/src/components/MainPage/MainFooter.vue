<template>
  <div>
    <section class="contact">
      <div class="contact__wrapper">
        <div class="contact__info">
          <main-text
            class="contact__title"
            :fontFamily="'montSer'"
            :fontSize="28"
            :fontWeight="600"
          >
            Подпишитесь на рассылку
            <main-text
              class="contact__subtitle"
              :fontFamily="'montSer'"
              :fontSize="22"
              :fontWeight="500"
              :color="'#BCBCBC'"
            >
              Наши письма читают уже более 10000 HR-специалистов
            </main-text>
          </main-text>
        </div>
        <div class="contact__form">
          <form class="contact-form">
            <fieldset class="contact-form__info">
              <input
                type="text"
                name="Your email"
                class="contact-form__field"
                placeholder="Ваше имя"
              />
              <input
                type="text"
                name="Your email"
                class="contact-form__field"
                placeholder="Ваша почта"
              />
              <my-button type="submit" class="contact__btn"
                ><main-text
                  class="contact__btn_text"
                  :fontFamily="'montSer'"
                  :fontSize="16"
                  >Подписаться</main-text
                >
              </my-button>
            </fieldset>
          </form>
        </div>
      </div>
    </section>
    <section class="footer">
      <div class="footer__wrapper">
        <a href=""
          ><main-text
            class="footer__link"
            :fontFamily="'montSer'"
            :fontSize="18"
            :color="'#BCBCBC'"
            >Политика конфиденциальности</main-text
          ></a
        >
        <a href=""
          ><main-text
            class="footer__link"
            :fontFamily="'montSer'"
            :fontSize="18"
            :color="'#BCBCBC'"
            >Пользовательское соглашение</main-text
          ></a
        >
        <main-text :fontFamily="'montSer'" :fontSize="18" :color="'#BCBCBC'"
          >kovshov.K@yandex.ru</main-text
        >
        <a href="#"
          ><img
            src="@/assets/telegram-icn.svg"
            alt="telega"
            class="footer__img"
        /></a>
        <a href="https://vk.com/kovsh.andrew"
          ><img src="@/assets/vk-icn.svg" alt="vk" class="footer__img"
        /></a>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'MyFooter',
};
</script>

<style lang="scss" scoped>
.contact {
  &__info {
    margin: auto;
    text-align: center;
  }
  &__subtitle {
    margin: 5px 0 50px;
  }
  &-form {
    &__info {
      border: none;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 15px;
    }

    &__field {
      background: none;
      border: 1.5px solid #9c53d5;
      border-radius: 20px;
      min-width: 240px;
      height: 40px;
      padding-left: 5px;
      color: white;
      outline: none;
    }
  }
  &__btn {
    background: #9c53d5;
    border-color: #9c53d5;
    min-width: 240px;
    height: 40px;
    &_text {
      margin-top: 10px;
      text-align: center;
    }
  }
}
.footer {
  margin-top: 160px;
  padding-bottom: 10px;
  &__wrapper {
    display: flex;
    justify-content: center;
    gap: 20px;
  }
}
a {
  color: #bcbcbc;
}
</style>
