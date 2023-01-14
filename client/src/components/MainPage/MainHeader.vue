<template>
  <header class="header" v-if="myPadeDate.header">
    <main-text
      class="header__logo-wrapper"
      :fontFamily="'montSer'"
      :fontSize="32"
      :fontWeight="600"
    >
      <img
        src="@/assets/header_logo.svg"
        alt="Logo"
        class="header__logo__img"
      />
      {{ myPadeDate.header.title }}
    </main-text>
    <nav class="header__nav">
      <button type="button" class="btn btn-dark">
        <main-text
          class="header__text"
          :fontFamily="'montSer'"
          :fontSize="18"
          >{{ myPadeDate.header.abs }}</main-text
        >
      </button>

      <!-- <button type="button" class="btn btn-dark">
        <main-text class="header__text" :fontFamily="'montSer'" :fontSize="18"
          ><a
            class="header__text_link"
            href="https://github.com/AndrewwKovv/client-exams"
            >{{ myPadeDate.header.git }}</a
          ></main-text
        >
      </button> -->
      <button type="button" class="btn btn-dark">
        <main-text
          class="header__text"
          :fontFamily="'montSer'"
          :fontSize="18"
          >{{ myPadeDate.header.contact }}</main-text
        >
      </button>
      <button type="button" @click="showDialog" class="btn btn-dark">
        <main-text
          class="header__text"
          :fontFamily="'montSer'"
          :fontSize="18"
          >{{ myPadeDate.header.login }}</main-text
        >
      </button>

      <auth-modal
        :myPadeDate="myPadeDate"
        v-model:show="dialogVisible"
      ></auth-modal>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'my-header',
  data() {
    return {
      dialogVisible: false,
    };
  },
  methods: {
    showDialog() {
      this.dialogVisible = true;
    },
  },
  props: {
    myPadeDate: Object,
  },
};
</script>

<style lang="scss" scoped>
.header {
  background-color: #404040;
  max-width: 1180px;
  width: 100%;
  height: 90px;
  border-radius: 5px;
  padding: 0 15px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  &__logo-wrapper {
    display: flex;
    align-items: center;
  }
  &__nav {
    display: flex;
    gap: 30px;
  }
  &__btn {
    padding: 1px 13px;
    border-radius: 5px;
  }
  &__text_link {
    color: white;
    text-decoration: none;
  }
}
@media screen and (max-width: 1030px) {
  .header {
    flex-wrap: wrap;
    height: 110px;
  }
}
@media screen and (max-width: 830px) {
  .header {
    height: 170px;
  }
}
@media screen and (max-width: 770px) {
  .header__nav {
    flex-wrap: wrap;
  }
}
@media screen and (max-width: 649px) {
  .header {
    height: 324px;
    padding: 0 60px;
  }
  .header__nav {
    gap: 10px;
    flex-wrap: nowrap;
    flex-direction: column;
  }
}
</style>
