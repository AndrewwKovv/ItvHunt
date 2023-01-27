<template>
  <div class="task__item">
    <router-link
      class="task__link"
      :to="{
        name: 'taskPage',
        params: {
          id: row_data.id,
          vacName: row_data.title,
        },
      }"
    >
      <div class="task__data">
        <main-text
          class="task__title"
          :fontFamily="'montSer'"
          :fontSize="16"
          :fontWeight="500"
        >
          {{ row_data.title }}
        </main-text>
      </div>
      <div class="task__data">
        <main-text
          class="task__title task__title_link"
          :fontFamily="'montSer'"
          :fontSize="16"
          :fontWeight="500"
        >
          {{ row_data.desc }}
        </main-text>
      </div>
      <div class="task__data">
        <main-text
          class="task__title_time"
          :fontFamily="'montSer'"
          :fontSize="16"
          :fontWeight="500"
        >
          {{ formateDate(row_data.created_at) }}
        </main-text>
      </div>
    </router-link>
  </div>
</template>

<script>
import { parseISO, format } from 'date-fns';
export default {
  name: 'task-items',
  props: {
    row_data: {
      type: Object,
      default: () => {
        return {};
      },
    },
  },
  methods: {
    formateDate(date) {
      let res = parseISO(date);
      date = res;
      return format(date, 'dd.MM.yyyy');
    },
  },
};
</script>

<style lang="scss" scoped>
.task__link {
  display: flex;
  justify-content: space-between;
  padding: 0 10px;
  text-decoration: none;
  align-items: center;
}
.task {
  &__item {
    margin-top: 35px;
    border: 1px solid #343434;
    border-radius: 5px;
    &:hover {
      box-shadow: 2px 2px 2px 2px grey;
    }
  }
  &__title {
    margin: 15px 0 15px;
    word-break: break-word;

    // &_time {
    //   max-width: 300px;
    // }
    // &_link {
    //   max-width: 300px;
    // }
  }
  &__data {
    width: 100%;
    &:last-child {
      text-align: right;
    }
  }
}
</style>
