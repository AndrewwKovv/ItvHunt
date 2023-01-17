<template>
  <div>
    <section class="contact">
      <div class="contact__wrapper">
        <div class="contact__info" v-if="myPadeDate.footer">
          <main-text
            class="contact__title"
            :fontFamily="'montSer'"
            :fontSize="28"
            :fontWeight="600"
          >
            {{ myPadeDate.footer.msg.title }}

            <main-text
              class="contact__subtitle"
              :fontFamily="'montSer'"
              :fontSize="22"
              :fontWeight="500"
              :color="'#BCBCBC'"
            >
              {{ myPadeDate.footer.msg.subtitle }}
            </main-text>
          </main-text>
        </div>
        <div class="contact__form" v-if="myPadeDate.footer">
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
                >
                  {{ myPadeDate.footer.msg.btn }}
                </main-text>
              </my-button>
            </fieldset>
          </form>
        </div>
      </div>
    </section>
    <footer class="footer">
      <div class="footer__wrapper" v-if="myPadeDate.footer">
        <a href=""
          ><main-text
            class="footer__link"
            :fontFamily="'montSer'"
            :fontSize="18"
            :color="'#BCBCBC'"
            >{{ myPadeDate.footer.list.policy }}</main-text
          ></a
        >
        <a href=""
          ><main-text
            class="footer__link"
            :fontFamily="'montSer'"
            :fontSize="18"
            :color="'#BCBCBC'"
            >{{ myPadeDate.footer.list.pols }}</main-text
          ></a
        >
        <main-text :fontFamily="'montSer'" :fontSize="18" :color="'#BCBCBC'">{{
          myPadeDate.footer.list.email
        }}</main-text>
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
    </footer>
  </div>
</template>

<script>
export default {
  name: 'MyFooter',
  props: {
    myPadeDate: Object,
  },
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
      flex-wrap: wrap;
    }

    &__field {
      background: none;
      border: 1.5px solid #9c53d5;
      border-radius: 10px;
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
@media screen and (max-width: 970px) {
  .contact-form__field {
    min-width: 100px;
  }
  .contact__btn {
    min-width: 130px;
  }
}

@media screen and (max-width: 760px) {
  .footer__wrapper {
    flex-wrap: wrap;
  }
}
</style>
