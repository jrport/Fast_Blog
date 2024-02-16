<script>
import Home from './pages/Home.vue'
import WritePost from './pages/WritePost.vue'

const routes = {
  '/': Home,
  '/write': WritePost
}

  export default {
    data() {
      return {
        currentPath: window.location.pathname
      }
    },
    computed: {
      currentView() {
        return routes[this.currentPath.slice(1) || '/'] || NotFound
      }
    },
    mounted() {
      window.addEventListener('hashchange', () => {
        this.currentPath = window.location.hash
      })
    }
  }
</script>

<template>
  <component :is='currentView' />
</template>
