<template>
  <div class="candidates">
    <AppHeader appTitle="Кандидаты"></AppHeader>
    <div class="candidates__wrapper">
      <div class="candidates__container"></div>
    </div>
  </div>
</template>

<script>
import AppHeader from '../AppHeader.vue';

export default {
  name: 'candidates-page',
  components: { AppHeader },
};
</script>

<style lang="scss" scoped>
.candidates {
  margin-left: 130px;
  height: 100vh;
  &__wrapper {
    padding: 25px;
  }
  &__container {
    border-radius: 24px;
    background-color: #505050;
    width: 100%;
    height: 500px;
    padding: 22px;
  }
}
</style>
