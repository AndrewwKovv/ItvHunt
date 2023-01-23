import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import components from './components/UI';
import axios from 'axios';
import VueAxios from 'vue-axios';

const app = createApp(App).use(store).use(router).use(VueAxios, axios);

components.forEach((component) => {
  app.component(component.name, component);
});

app.mount('#app');
