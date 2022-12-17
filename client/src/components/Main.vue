<template>
  <main class="main">
    <section class="intro">
      <main-text class="intro__title" :fontFamily="'montSer'" :color="'#ffffff'"
        ><h1>
          Сервис для технических <br />
          собеседований
        </h1>
      </main-text>
      <main-text :fontFamily="'montSer'" :color="'#ffffff'" :fontSize="18">
        <p>
          Мы предлагаем удобную систему для проведения и<br />
          хранения технических собеседований в одном окне<br />
          браузера
        </p>
      </main-text>
      <my-button class="intro__btn">
        <main-text
          class="intro__btn_text"
          :fontFamily="'montSer'"
          :fontSize="18"
          :color="'#ffffff'"
          >Начать</main-text
        >
      </my-button>
    </section>
    <section class="function">
      <nav class="function__nav">
        <ul class="function__row">
          <li class="function__item">
            <div class="function__items-tb">
              <img
                src="@/assets/icn-test.svg"
                alt="test-task"
                class="function-icn"
              />
              <main-text
                :fontFamily="'montSer'"
                :color="'#ffffff'"
                :fontSize="20"
                ><p class="items-title">Тестовое задание</p></main-text
              >
            </div>
          </li>
          <li class="function__item">
            <div class="function__items-tb">
              <img
                src="@/assets/icn-itv.svg"
                alt="test-task"
                class="function-icn"
              />
              <main-text
                :fontFamily="'montSer'"
                :color="'#ffffff'"
                :fontSize="20"
                ><p class="items-title">Сценарии интервью</p></main-text
              >
            </div>
          </li>
          <li class="function__item">
            <div class="function__items-tb">
              <img
                src="@/assets/icn-otchet.svg"
                alt="test-task"
                class="function-icn"
              />
              <main-text
                :fontFamily="'montSer'"
                :color="'#ffffff'"
                :fontSize="20"
                ><p class="items-title">Отчеты</p></main-text
              >
            </div>
          </li>
        </ul>
      </nav>
    </section>
  </main>
</template>

<script>
export default {
  name: 'my-main',
};
</script>

<style lang="scss" scoped>
.main {
  padding: 50px 0;
}
.intro {
  padding-top: 105px;
  background: url(@/assets/intro-bg.svg) no-repeat center;
  //background-size: cover;
  &__title {
    margin-bottom: 30px;
  }
  &__btn {
    max-width: 240px;
    height: 50px;
    background-color: #4dd362;
    border-radius: 30px;
    margin-top: 40px;
    &_text {
      margin: 12px 85px;
    }
  }
}
.function {
  display: flex;
  &__row {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
}
</style>
