<template>
  <div class="tasks">
    <AppHeader appTitle="Задачи"></AppHeader>
    <div class="tasks__wrapper">
      <task-table :tasks_data="validTasks"></task-table>
    </div>
  </div>
</template>

<script>
import AppHeader from '../AppHeader.vue';
import TaskTable from './Tasks/TaskTable.vue';
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'tasks-page',
  components: { AppHeader, TaskTable },
  computed: {
    ...mapGetters(['validTasks']),
  },
  methods: {
    ...mapActions(['fetchTasks']),
  },
  async mounted() {
    this.fetchTasks();
  },
};
</script>

<style lang="scss" scoped>
.tasks {
  min-height: 100vh;
  margin-left: 130px;
  &__wrapper {
    padding: 25px;
  }
}
</style>
