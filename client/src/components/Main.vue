<template>
  <main class="main">
    <section class="intro">
      <main-text class="intro__title" :fontFamily="'montSer'"
        ><h1>
          Сервис для технических <br />
          собеседований
        </h1>
      </main-text>
      <main-text :fontFamily="'montSer'" :fontSize="18">
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
          :fontWeight="600"
          :color="'#1E1E1E'"
          >Начать</main-text
        >
      </my-button>
    </section>
    <section class="about">
      <div class="about__title">
        <main-text
          class="about__title-text"
          :fontFamily="'montSer'"
          :fontSize="22"
        >
          <center>
            <b>ItvHunt</b> — это сервис для технических собеседований онлайн,
            которая помогает кандидатам легко показать свои реальные навыки, а
            команде найма сократить время на подготовку и проведение интервью, и
            упростить принятие решений.
          </center>
        </main-text>
      </div>
    </section>
    <section class="function">
      <nav class="function__nav">
        <i
          :style="{ transform: 'translateX' + 100 + '%' }"
          class="function__activeTabFocusLine"
        ></i>
        <button class="function__items-tb" @click="oneSlide">
          <img
            src="@/assets/icn-test.svg"
            alt="test-task"
            class="function-icn"
          />
          <main-text :fontFamily="'montSer'" :fontSize="20"
            ><p class="items-title">Тестовое задание</p></main-text
          >
        </button>
        <button class="function__items-tb" @click="twoSlide">
          <img
            src="@/assets/icn-itv.svg"
            alt="test-task"
            class="function-icn"
          />
          <main-text :fontFamily="'montSer'" :fontSize="20"
            ><p class="items-title">Сценарии интервью</p></main-text
          >
        </button>
        <button class="function__items-tb" @click="threeSlide">
          <img
            src="@/assets/icn-otchet.svg"
            alt="test-task"
            class="function-icn"
          />
          <main-text :fontFamily="'montSer'" :fontSize="20"
            ><p class="items-title">Отчеты</p></main-text
          >
        </button>
      </nav>
      <div class="function__desc">
        <div class="function__desc-carasel" :style="currentSlideIndex">
          <div class="function__desc_about">
            <img
              src="@/assets/function-task.svg"
              alt="about-task"
              class="function__desc_img"
            />
            <main-text
              class="function__desc-title"
              :fontFamily="'montSer'"
              :fontSize="28"
              >Тестовые задания с набором кода (в разработке)
              <main-text
                class="function__desc-subtitle"
                :fontFamily="'montSer'"
                :fontSize="16"
                >Отправке кандидату короткую задачу с ограничением по времени,
                по ссылке будет редактор, после решения можно посмотреть
                код</main-text
              ></main-text
            >
          </div>

          <div class="function__desc_about">
            <img
              src="@/assets/function-task.svg"
              alt="about-task"
              class="function__desc_img"
            />
            <main-text :fontFamily="'montSer'" :fontSize="28"
              >Конструктор сценариев интервью</main-text
            >
            <main-text
              class="function__desc-subtitle"
              :fontFamily="'montSer'"
              :fontSize="16"
              >Подготовьте и используйте во время интервью шаблоны с<br />
              вопросами и задачами. Вам доступны разделы по темам,<br />
              блоки с вопросами, блок задач и блок навыков и знаний.<br />
              Забудьте excel, гугл формс и пр.</main-text
            >
          </div>
          <div class="function__desc_about">
            <img
              src="@/assets/function-task.svg"
              alt="about-task"
              class="function__desc_img"
            />
            <main-text :fontFamily="'montSer'" :fontSize="28">Отчёты</main-text>
            <main-text
              class="function__desc-subtitle"
              :fontFamily="'montSer'"
              :fontSize="16"
              >Все результаты хранятся в карточке кандидата. Оценка<br />
              интервьюера, ответы, задачи и код с интервью.</main-text
            >
          </div>
        </div>
      </div>
      <div class="function__button">
        <my-button class="function__btn">
          <main-text
            class="function__btn-text"
            :fontFamily="'montSer'"
            :fontSize="16"
            :fontWeight="500"
            :color="'#1E1E1E'"
            >Посмотреть все возможности</main-text
          >
        </my-button>
      </div>
    </section>
    <section class="feedback">
      <div class="feedback__wrapper">
        <main-text
          class="feedback__title"
          :fontFamily="'montSer'"
          :fontSize="32"
          :fontWeight="600"
          >ItvHunt экономит в среднем 25 минут на каждое интервью</main-text
        >
        <div class="feedback__users">
          <div class="feedback__user">
            <main-text
              :fontFamily="'montSer'"
              :fontSize="18"
              :color="'#1E1E1E'"
              :fontWeight="500"
              ><b class="feedback__quote">&lt;&lt;</b> Когда мы стали
              использовать Meet2Code вместо разных инструментов, время
              подготовки и проведения собеседования сократилось на 20-30 минут,
              а само интервью стало удобнее и менее утомительным.
              <main-text
                :fontFamily="'montSer'"
                :fontSize="16"
                :color="'#1E1E1E'"
                class="feedback__author"
              >
                <b class="feedback__quote feedback__quote--close">&gt;&gt;</b>
                <i>Михаил, тимлид фронтенд-разработки</i>
              </main-text>
            </main-text>
          </div>
          <div class="feedback__user">
            <main-text
              :fontFamily="'montSer'"
              :fontSize="18"
              :color="'#1E1E1E'"
              :fontWeight="500"
              ><b class="feedback__quote">&lt;&lt;</b> Когда мы стали
              использовать Meet2Code вместо разных инструментов, время
              подготовки и проведения собеседования сократилось на 20-30 минут,
              а само интервью стало удобнее и менее утомительным.
              <main-text
                :fontFamily="'montSer'"
                :fontSize="16"
                :color="'#1E1E1E'"
                class="feedback__author"
              >
                <b class="feedback__quote feedback__quote--close">&gt;&gt;</b>
                <i>Андрей, тимлид бэкенд-разработки</i>
              </main-text>
            </main-text>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
export default {
  name: 'my-main',
  data() {
    return {
      show: true,
      currentSlideIndex: 0,
    };
  },
  methods: {
    oneSlide() {
      this.currentSlideIndex == 0;
    },
    twoSlide() {
      this.currentSlideIndex == 100;
    },
    threeSlide() {
      this.currentSlideIndex == 200;
    },
  },
};
</script>

<style lang="scss" scoped>
.main {
  padding: 50px 0;
}
.intro {
  padding-top: 105px;
  background: url(@/assets/intro-bg.svg) no-repeat center;
  &__title {
    margin-bottom: 30px;
  }
  &__btn {
    max-width: 240px;
    height: 50px;
    background-color: #4dd362;
    border-radius: 30px;
    margin: 40px 0;
    &_text {
      margin: 12px 85px;
    }
  }
}
.about {
  background: url(@/assets/about-bg.svg) no-repeat center;
  background-size: cover;
  padding: 65px 0 60px;
}
.function {
  margin-top: 80px;
  &__nav {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: auto;
    gap: 50px;
  }
  &__items-tb {
    border: none;
    background: none;
    cursor: pointer;
    width: calc(100% / 3);
    opacity: 0.7;
    &--active {
      opacity: 1;
    }
  }
  &__btn {
    max-width: 300px;
    height: 35px;
    background-color: #4dd362;
    border-radius: 30px;
    margin: 60px auto;
    &-text {
      margin: 6px 21px;
    }
  }
  &__activeTabFocusLine {
    margin-top: 20px;
    position: absolute;
    left: 0;
    right: 0;
    bottom: -3px;
    width: -moz-calc(100%/3);
    width: calc(100% / 3);
    height: 6px;
    background: #4dd362;
    -webkit-transition: 0.5s;
    -moz-transition: 0.5s;
    transition: 0.5s;
  }
  &__desc {
    overflow: hidden;
    max-width: 1180px;
    margin-top: 35px;
    &-carasel {
      display: flex;
    }
    &-title {
      margin: 30px;
    }
    &-subtitle {
      margin-top: 15px;
    }
    &_about {
      display: flex;
      align-items: center;
      min-width: 100%;
      background: url(@/assets/func-about-bg.svg) no-repeat center;
      background-size: cover;
    }
    &_img {
      border-radius: 10px;
    }
  }
}
.items-title {
  margin: 20px 0 40px;
}
.feedback {
  margin: 40px 0;
  &__title {
    text-align: center;
  }
  &__users {
    margin-top: 60px;
    display: flex;
    justify-content: space-between;
  }
  &__user {
    display: flex;
    align-items: center;
    position: relative;
    margin: 25px;
    padding: 30px;
    background-color: #4dd362;
  }
  &__author {
    margin-top: 15px;
    text-align: right;
  }
  &__quote {
    position: absolute;
    top: 0;
    left: -20px;
    color: white;
    font-size: 30px;
    &--close {
      top: auto;
      bottom: 0;
      right: -20px;
      left: auto;
    }
  }
}
</style>
