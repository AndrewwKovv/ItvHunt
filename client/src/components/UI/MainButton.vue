<template>
  <div class="btn">
    <slot />
  </div>
</template>

<script>
export default {
  name: 'my-button',
};
</script>

<style lang="scss">
.btn {
  background: none;
  border: 1px solid #4dd362;
  border-radius: 20px;
}
</style>
