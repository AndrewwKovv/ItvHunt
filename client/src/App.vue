<template>
  <div class="container">
    <my-header></my-header>
    <my-main></my-main>
  </div>
</template>

<script>
import MyHeader from './components/Header.vue';
import MyMain from './components/Main.vue';
export default {
  components: { MyHeader, MyMain },
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
.container {
  height: 900px;
  background-color: #1e1e1e;
  padding: 36px 130px 0;
}
</style>
