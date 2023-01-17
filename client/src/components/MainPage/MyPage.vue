<template>
  <div class="container">
    <my-header :myPadeDate="myPadeDate"></my-header>
    <my-body :myPadeDate="myPadeDate"></my-body>
    <MyFooter :myPadeDate="myPadeDate"></MyFooter>
  </div>
</template>

<script>
import MyHeader from './MainHeader.vue';
import MyBody from './MainBody.vue';
import MyFooter from '@/components/MainPage/MainFooter.vue';

export default {
  components: { MyHeader, MyBody, MyFooter },
  name: 'main-page',
  data() {
    return { myPadeDate: [] };
  },
  methods: {
    getDate() {
      fetch('mainPage.json')
        .then((response) => response.json())
        .then((date) => (this.myPadeDate = date));
    },
  },
  beforeMount() {
    this.getDate();
  },
};
</script>

<style lang="scss" scoped>
.container {
  padding: 36px 20px 0 80px;
  background-color: #1e1e1e;
}
@media screen and (max-width: 550px) {
  .container {
    padding: 15px 20px 0;
  }
}
</style>
