<script>
	export default {
    props: ['id', 'title', 'content', 'date'],
    data() {
      return {
        post_id: this.id,
        story_link: `./posts/read/${this.id}`
      }
    }
  }
</script>

<template>
  <div class="flex flex-col h-fit max-w-full flex-wrap">
    <a class="text-2xl text-violet-900" :href="story_link">{{ title }}</a>
    <p class="">{{ date.replaceAll('-', ' ') }}</p>
    <p class=" max-w-full break-words">{{ content }}</p>
  </div>
</template>
