<template>
  <aside class="app-sidebar">
    <div class="logo">
      <img src="@/assets/header_logo.svg" alt="Logo" />
    </div>

    <div class="menu">
      <router-link to="/candidates" class="button">
        <span class="material-icons">
          <img
            src="@/assets/candidates-icn.svg"
            alt="candidates"
            class="material-icons__size"
          />
        </span>
        <span class="text" v-if="appPageDate.sidebar"
          ><main-text
            class="sidebar__text"
            :fontFamily="'montSer'"
            :fontSize="16"
            >{{ appPageDate.sidebar.candidates }}</main-text
          ></span
        >
      </router-link>
      <router-link to="/tasks" class="button">
        <span class="material-icons">
          <img
            src="@/assets/tasks-icn.svg"
            alt="candidates"
            class="material-icons__size"
          />
        </span>
        <span class="text" v-if="appPageDate.sidebar"
          ><main-text
            class="sidebar__text"
            :fontFamily="'montSer'"
            :fontSize="16"
            >{{ appPageDate.sidebar.task }}</main-text
          ></span
        >
      </router-link>
      <router-link to="/templates" class="button">
        <span class="material-icons">
          <img
            src="@/assets/templates-icn.svg"
            alt="candidates"
            class="material-icons__size"
          />
        </span>
        <span class="text" v-if="appPageDate.sidebar"
          ><main-text
            class="sidebar__text"
            :fontFamily="'montSer'"
            :fontSize="16"
            >{{ appPageDate.sidebar.templates }}</main-text
          ></span
        >
      </router-link>
      <router-link to="/vacanci" class="button">
        <span class="material-icons">
          <img
            src="@/assets/vacanci-icn.svg"
            alt="candidates"
            class="material-icons__size"
          />
        </span>
        <span class="text" v-if="appPageDate.sidebar"
          ><main-text
            class="sidebar__text"
            :fontFamily="'montSer'"
            :fontSize="16"
            >{{ appPageDate.sidebar.vacancy }}</main-text
          ></span
        >
      </router-link>
    </div>

    <div class="flex"></div>

    <div class="menu">
      <router-link to="/settings" class="bttn">
        <span class="sidebar__settigns">
          <img
            src="@/assets/settings-icn.svg"
            alt="candidates"
            class="sidebar__settigns_size"
          />
        </span>
      </router-link>
    </div>
  </aside>
</template>

<script>
export default {
  name: 'my-sidebar',
  props: {
    appPageDate: Object,
  },
};
</script>

<style lang="scss" scoped>
aside {
  display: flex;
  flex-direction: column;
  position: fixed;

  background-color: #1e1e1e;
  align-items: center;
  width: 130px;
  overflow: hidden;
  min-height: 100vh;
  padding: 15px 0;
  .flex {
    flex: 1 1 0%;
  }
  .menu {
    margin: 0 -1rem;
    .button {
      align-items: center;
      text-decoration: none;
      transition: 0.2s ease-in-out;
      padding: 1rem 1rem;
      display: flex;
      flex-direction: column;
      opacity: 0.7;
      .material-icons {
        transition: 0.2s ease-in-out;
        &__size {
          width: 22px;
        }
      }
      .text {
        transition: 0.2s ease-in-out;
      }
      &.router-link-exact-active {
        opacity: 1;
        margin-right: -3px;
        background-color: #343434;
        border-left: 4px solid #4dd362;
      }
      &:active,
      &:hover {
        opacity: 1;
      }
      &:first-child {
        margin-top: 55px;
      }
    }
  }
  .sidebar__settigns {
    padding: 10px 10px 10px 10px;
    border: 2px solid;
    border-radius: 10px;
    border-color: #4dd362;
    &_size {
      width: 22px;
    }
    &:active,
    &:hover {
      background-color: #343434;
    }
  }

  @media (max-width: 1024px) {
    position: absolute;
    z-index: 99;
  }
}
</style>
