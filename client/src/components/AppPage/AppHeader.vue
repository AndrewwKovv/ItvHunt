<template>
  <div class="app-header">
    <main-text
      class="app-header__text"
      :fontFamily="'montSer'"
      :fontSize="24"
      :fontWeight="500"
      >{{ appTitle }}</main-text
    >

    <div class="app-header__profile">
      <!-- <button type="button" class="btn btn-dark">
        <main-text
          class="app-header__text"
          :fontFamily="'montSer'"
          :fontSize="18"
          ><a
            class="app-header__text_link"
            href="https://github.com/AndrewwKovv/client-exams"
            >GIT</a
          ></main-text
        >
      </button> -->
      <button type="button" class="btn btn-dark">
        <main-text
          :fontFamily="'montSer'"
          :fontSize="20"
          class="app-header__name-person"
          >{{ avatar.name }}</main-text
        >
      </button>
      <div class="app-header__photo" @click="this.$router.push('/settings')">
        <img src="@/assets/avatar-photo.svg" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app-header',
  props: {
    appTitle: String,
  },
  data() {
    return {
      avatar: {
        name: 'Андрей',
      },
    };
  },
};
</script>

<style lang="scss" scoped>
.app-header {
  display: flex;
  align-items: center;
  flex-wrap: wrap;

  justify-content: space-between;
  background-color: #505050;
  height: 67px;
  padding: 0 30px;
  &__profile {
    display: flex;
    align-items: center;
    gap: 35px;
    flex-wrap: wrap;
    cursor: pointer;
  }
  &__text_link {
    color: white;
    text-decoration: none;
    &:hover {
      opacity: 0.75;
    }
  }
  &__name-person {
    &:hover {
      opacity: 0.75;
    }
  }
  &__photo {
    &:hover {
      opacity: 0.75;
    }
  }
}
@media screen and (max-width: 500px) {
  .app-header {
    height: 87px;
  }
}
</style>
