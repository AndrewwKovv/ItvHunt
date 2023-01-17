<template>
  <div class="tasks">
    <AppHeader appTitle="Задачи"></AppHeader>
  </div>
</template>

<script>
import AppHeader from '../AppHeader.vue';

export default {
  name: 'tasks-page',
  components: { AppHeader },
};
</script>

<style lang="scss" scoped>
.tasks {
  margin-left: 130px;
  height: 100vh;
}
</style>
