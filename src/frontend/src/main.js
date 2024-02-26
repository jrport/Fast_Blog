import { createApp } from "vue";
import App from './App.vue'
import Header from './pages/components/Header.vue'
import Footer from './pages/components/Footer.vue'
import './main.css'

const app = createApp(App)

app.component('Header', Header)
app.component('Footer', Footer)

app.mount("#app")
