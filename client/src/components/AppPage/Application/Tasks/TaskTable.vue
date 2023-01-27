<template>
  <div class="tasks__container">
    <div class="tasks__head">
      <input
        type="text"
        class="tasks__search tasks__search-inp"
        placeholder="Поиск"
        v-model="searchTask"
      />
      <my-button class="contact__button">
        <main-text
          class="contact__subtitle"
          :fontFamily="'montSer'"
          :fontSize="16"
          :fontWeight="500"
          >+ добавить задание
        </main-text></my-button
      >
    </div>
    <div class="tasks__title">
      <main-text
        class="tasks__subtitle"
        :fontFamily="'montSer'"
        :fontSize="14"
        :fontWeight="500"
      >
        задание
      </main-text>
      <main-text
        class="tasks__subtitle"
        :fontFamily="'montSer'"
        :fontSize="14"
        :fontWeight="500"
      >
        описание
      </main-text>
      <div @click="sortByName">
        <main-text
          class="tasks__subtitle"
          :fontFamily="'montSer'"
          :fontSize="14"
          :fontWeight="500"
        >
          добавлена
        </main-text>
      </div>
    </div>
    <task-items
      v-for="tasks in searchTasks"
      :key="tasks.id"
      :row_data="tasks"
    ></task-items>
  </div>
</template>

<script>
import TaskItems from '@/components/AppPage/Application/Tasks/TaskItems.vue';

export default {
  components: { TaskItems },
  name: 'task-table',
  data() {
    return {
      searchTask: '',
    };
  },
  props: {
    tasks_data: {
      type: Array,
      default: () => {
        return [];
      },
    },
  },
  methods: {
    sortByName() {
      this.searchTasks.sort((b, a) => a.created_at.localeCompare(b.created_at));
      console.log(this.searchTasks);
    },
  },
  computed: {
    searchTasks() {
      return this.tasks_data.filter(
        (tasks) =>
          tasks.title.toLowerCase().includes(this.searchTask.toLowerCase()) || tasks.desc.toLowerCase().includes(this.searchTask.toLowerCase())
      );
    },
  },
};
</script>

<style lang="scss" scoped>
.tasks {
  &__container {
    border-radius: 24px;
    background-color: #505050;
    width: 100%;
    padding: 22px;
  }
  &__head {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
  }
  &__title {
    display: flex;
    margin-top: 75px;
    border: 1px solid #343434;
    border-radius: 5px;
    justify-content: space-between;
    padding: 0 10px;
  }
  &__subtitle {
    margin-left: 15px;
  }
  &__search-inp {
    border: 2px solid #343434;
    border-radius: 10px;
    background-color: #505050;
    max-width: 250px;
    height: 25px;
    padding: 5px;
    color: white;
  }
}
.contact {
  &__button {
    background-color: #4dd362;
    padding: 5px;
    &:hover {
      box-shadow: 0 0 0 2px #4dd362;
    }
  }
}
</style>
