<template>
  <div class="applications-cont">
    <Sidebar :appPageDate="appPageDate"></Sidebar>
    <router-view />
  </div>
</template>

<script>
import Sidebar from './Sidebar.vue';

export default {
  components: { Sidebar },
  name: 'app-page',
  data() {
    return { appPageDate: [] };
  },
  methods: {
    getAppDate() {
      fetch('appPage.json')
        .then((response) => response.json())
        .then((date) => (this.appPageDate = date));
    },
  },
  beforeMount() {
    this.getAppDate();
  },
};
</script>

<style lang="scss" scoped>
.applications-cont {
  background-color: #343434;
  height: 100%;
  width: 100vw;
}
</style>
