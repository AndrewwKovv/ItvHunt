<template>
  <div class="error">
    <p class="error__title">Похоже такой страницы нету....</p>
  </div>
</template>

<script>
export default {
  name: 'error-page',
};
</script>

<style lang="scss" scoped>
.error {
  &__title {
    margin: 250px 500px;
    color: white;
    font-size: 32px;
  }
}
</style>
