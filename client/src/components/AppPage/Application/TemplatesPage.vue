<template>
  <div class="templates">
    <AppHeader appTitle="Шаблоны"></AppHeader>
  </div>
</template>

<script>
import AppHeader from '../AppHeader.vue';

export default {
  name: 'templates-page',
  components: { AppHeader },
};
</script>

<style lang="scss" scoped>
.templates {
  margin-left: 130px;
  height: 100vh;
}
</style>
