<template>
  <main class="main">
    <section class="intro" v-if="myPadeDate.intro">
      <main-text class="intro__title" :fontFamily="'montSer'"
        ><h1 class="intro__title">
          {{ myPadeDate.intro.title }}
        </h1>
      </main-text>
      <main-text
        class="intro__subtitle"
        :fontFamily="'montSer'"
        :fontSize="18"
        v-if="myPadeDate.intro.subtitle"
      >
        <p class="intro__subtitle">
          {{ myPadeDate.intro.subtitle.start }}
        </p>
      </main-text>
      <my-button class="intro__btn" @click="showDialog" v-if="myPadeDate.intro">
        <main-text
          class="intro__btn-text"
          :fontFamily="'montSer'"
          :fontSize="18"
          :fontWeight="600"
          :color="'#1E1E1E'"
          >{{ myPadeDate.intro.btn }}</main-text
        >
      </my-button>
      <main-modal
        :myPadeDate="myPadeDate"
        v-model:show="dialogVisible"
      ></main-modal>
    </section>
    <section class="about">
      <div class="about__title" v-if="myPadeDate.intro">
        <main-text
          class="about__title-text"
          :fontFamily="'montSer'"
          :fontSize="22"
        >
          <center>
            <b>{{ myPadeDate.intro.desc.title }}</b
            >{{ myPadeDate.intro.desc.text }}
          </center>
        </main-text>
      </div>
    </section>
    <section class="function">
      <nav class="function__nav" v-if="myPadeDate.func">
        <i
          :style="{
            transform: 'translateX' + '(' + currentSlideIndex + '%' + ')',
          }"
          class="function__activeTabFocusLine"
        ></i>
        <button class="function__items-tb" @click="oneSlide">
          <img
            src="@/assets/icn-test.svg"
            alt="test-task"
            class="function-icn"
          />
          <main-text :fontFamily="'montSer'" :fontSize="20"
            ><p class="items-title">
              {{ myPadeDate.func.icnTitle.a }}
            </p></main-text
          >
        </button>
        <button class="function__items-tb" @click="twoSlide">
          <img
            src="@/assets/icn-itv.svg"
            alt="test-task"
            class="function-icn"
          />
          <main-text :fontFamily="'montSer'" :fontSize="20"
            ><p class="items-title">
              {{ myPadeDate.func.icnTitle.b }}
            </p></main-text
          >
        </button>
        <button class="function__items-tb" @click="threeSlide">
          <img
            src="@/assets/icn-otchet.svg"
            alt="test-task"
            class="function-icn"
          />
          <main-text :fontFamily="'montSer'" :fontSize="20"
            ><p class="items-title">
              {{ myPadeDate.func.icnTitle.c }}
            </p></main-text
          >
        </button>
      </nav>
      <div class="function__desc">
        <div
          class="function__desc-carasel"
          :style="{
            transform: 'translateX(-' + currentSlideIndex + '%)',
          }"
        >
          <div class="function__desc-about" v-if="myPadeDate.func">
            <img
              src="@/assets/function-task.svg"
              alt="about-task"
              class="function__desc-img"
            />
            <main-text
              class="function__desc-title"
              :fontFamily="'montSer'"
              :fontSize="28"
              >{{ myPadeDate.func.descFunc.title.task }}
              <main-text
                class="function__desc-subtitle"
                :fontFamily="'montSer'"
                :fontSize="16"
              >
                {{ myPadeDate.func.descFunc.subtitle.task }}
              </main-text></main-text
            >
          </div>

          <div class="function__desc-about" v-if="myPadeDate.func">
            <img
              src="@/assets/func-vacancy-img.png"
              alt="about-task"
              class="function__desc-img"
            />
            <main-text
              class="function__desc-title"
              :fontFamily="'montSer'"
              :fontSize="28"
              >{{ myPadeDate.func.descFunc.title.vacy }}
              <main-text
                class="function__desc-subtitle"
                :fontFamily="'montSer'"
                :fontSize="16"
                >{{ myPadeDate.func.descFunc.subtitle.vacy }}</main-text
              ></main-text
            >
          </div>
          <div class="function__desc-about" v-if="myPadeDate.func">
            <img
              src="@/assets/function-task.svg"
              alt="about-task"
              class="function__desc-img"
            />
            <main-text
              class="function__desc-title"
              :fontFamily="'montSer'"
              :fontSize="28"
              >{{ myPadeDate.func.descFunc.title.ans }}
              <main-text
                class="function__desc-subtitle"
                :fontFamily="'montSer'"
                :fontSize="16"
                >{{ myPadeDate.func.descFunc.subtitle.ans }}</main-text
              ></main-text
            >
          </div>
        </div>
      </div>
      <div class="function__button" v-if="myPadeDate.func">
        <my-button class="function__btn" @click="showDialog">
          <main-text
            class="function__btn-text"
            :fontFamily="'montSer'"
            :fontSize="16"
            :fontWeight="500"
            :color="'#1E1E1E'"
            >{{ myPadeDate.func.button }}</main-text
          >
        </my-button>
        <main-modal v-model:show="dialogVisible"></main-modal>
      </div>
    </section>
    <section class="feedback">
      <div class="feedback__wrapper" v-if="myPadeDate.feedback">
        <main-text
          class="feedback__title"
          :fontFamily="'montSer'"
          :fontSize="32"
          :fontWeight="600"
          >{{ myPadeDate.feedback.title }}</main-text
        >
        <div class="feedback__users">
          <div class="feedback__user" v-if="myPadeDate.feedback.comments">
            <main-text
              :fontFamily="'montSer'"
              :fontSize="18"
              :color="'#1E1E1E'"
              :fontWeight="500"
              ><b class="feedback__quote">&lt;&lt;</b>
              {{ myPadeDate.feedback.comments.a }}
              <main-text
                :fontFamily="'montSer'"
                :fontSize="16"
                :color="'#1E1E1E'"
                class="feedback__author"
              >
                <b class="feedback__quote feedback__quote--close">&gt;&gt;</b>
                <i>{{ myPadeDate.feedback.comments.b }}</i>
              </main-text>
            </main-text>
          </div>
          <div class="feedback__user" v-if="myPadeDate.feedback.comments">
            <main-text
              :fontFamily="'montSer'"
              :fontSize="18"
              :color="'#1E1E1E'"
              :fontWeight="500"
              ><b class="feedback__quote">&lt;&lt;</b>
              {{ myPadeDate.feedback.comments.a }}
              <main-text
                :fontFamily="'montSer'"
                :fontSize="16"
                :color="'#1E1E1E'"
                class="feedback__author"
              >
                <b class="feedback__quote feedback__quote--close">&gt;&gt;</b>
                <i>{{ myPadeDate.feedback.comments.c }}</i>
              </main-text>
            </main-text>
          </div>
        </div>
        <div class="feedback__button" v-if="myPadeDate.feedback">
          <my-button class="feedback__btn" @click="showFeed">
            <main-text
              class="feedback__btn-text"
              :fontFamily="'montSer'"
              :fontSize="16"
              :fontWeight="500"
              :color="'#1E1E1E'"
              >{{ myPadeDate.feedback.btn }}</main-text
            >
          </my-button>
        </div>
        <FeedbackModal
          :myPadeDate="myPadeDate"
          v-model:show="modalVisible"
        ></FeedbackModal>
      </div>
    </section>
  </main>
</template>

<script>
import FeedbackModal from '../UI/FeedbackModal.vue';

export default {
  name: 'my-body',
  props: {
    myPadeDate: Object,
  },
  data() {
    return {
      currentSlideIndex: 0,
      dialogVisible: false,
      modalVisible: false,
    };
  },
  methods: {
    oneSlide() {
      this.currentSlideIndex = 0;
    },
    twoSlide() {
      this.currentSlideIndex = 100;
    },
    threeSlide() {
      this.currentSlideIndex = 200;
    },
    showDialog() {
      this.dialogVisible = true;
    },
    showFeed() {
      this.modalVisible = true;
    },
  },
  components: { FeedbackModal },
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
    max-width: 600px;
  }
  &__subtitle {
    max-width: 580px;
  }
  &__btn {
    max-width: 240px;
    height: 50px;
    background-color: #4dd362;
    border-radius: 10px;
    margin: 40px 0;
    &-text {
      margin: 0 20px;
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
  }
  &__btn {
    max-width: 300px;
    height: 35px;
    background-color: #4dd362;
    border-radius: 10px;
    margin: 60px auto;
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
    transition: 0.5s;
  }
  &__desc {
    overflow: hidden;
    max-width: 1180px;
    margin-top: 35px;
    &-carasel {
      display: flex;
      transition: 0.5s;
    }
    &-title {
      margin: 30px;
    }
    &-subtitle {
      margin-top: 15px;
    }
    &-about {
      display: flex;
      align-items: center;
      min-width: 100%;
      background: url(@/assets/func-about-bg.svg) no-repeat center;
      background-size: cover;
    }
    &-img {
      border-radius: 10px;
    }
  }
  &__button {
    text-align: center;
  }
}
.items-title {
  margin: 20px 0 40px;
}
.function__desc-img {
  width: 600px;
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
  &__btn {
    max-width: 200px;
    height: 35px;
    background-color: #4dd362;
    border-radius: 10px;
    margin: 60px auto;
    &-text {
      margin: 0 5px;
      text-align: center;
    }
  }
  &__button {
    text-align: center;
  }
}
@media screen and (max-width: 1025px) {
  .function__desc_img {
    width: 480px;
  }
  .function__desc_about {
    flex-wrap: wrap;
  }
}

@media screen and (max-width: 844px) {
  .feedback__users {
    flex-wrap: wrap;
  }
}

@media screen and (max-width: 700px) {
  .intro__subtitle {
    font-size: 16px;
  }
  .intro__title {
    font-size: 22px;
  }
}
@media screen and (max-width: 500px) {
  .function__desc_img {
    width: 358px;
  }
  .function-icn {
    width: 32px;
  }
  .items-title {
    font-size: 16px;
  }
}
@media screen and (max-width: 340px) {
  .items-title {
    font-size: 12px;
  }
  .function__desc_img {
    width: 288px;
  }
  .function__btn-text {
    margin: 6px 12px;
  }
  .function-icn {
    width: 22px;
  }
}
</style>
