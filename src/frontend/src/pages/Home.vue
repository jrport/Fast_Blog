<script>
import Post from './components/Post.vue';
import Footer from './components/Footer.vue';

export default {
	components: {
		Post,
		Footer
	},
	data () {
		return {
			posts: 0
		}
	},
	methods: {
		async getPosts(){
			const response = await fetch('http://localhost:80/')
			let posts = await response.json()
			return posts
		}
	},
	async mounted() {
		this.posts = await this.getPosts()
	}
}

</script>

<template>
	<Header />
  <div class="px-14 h-full flex pt-10 bg-gray-900 flex-col gap-4">
      <Post
        v-for='post in posts'
        :title='post.title'
        :content='post.content'
        :date='post.date'
		:id='post.id'
      />
  </div>
  	<Footer />
</template>
