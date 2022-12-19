<template>
  <div class="cont">
    <main-page></main-page>
  </div>
</template>

<script>
import MainPage from './components/MainPage/MyPage.vue';
export default {
  components: { MainPage },
  name: 'App',
};
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
</style>
