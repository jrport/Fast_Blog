<script>
import PostForms from './components/PostForms.vue';

export default {
	components: {
		PostForms
	}
}

</script>

<template>
	<Header />
	<div class="px-14 h-full flex pt-10 bg-gray-900 flex-col gap-4">
		<PostForms />
	</div>
	<Footer />
</template>
