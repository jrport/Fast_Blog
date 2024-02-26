<script>
    export default{
        data() {
            title: null;
            content: null
        },
        methods: {
            async post_form() {
                const payload = `{'title': '${this.title}', 'content': '${this.content}'}`
                const response = await fetch("http://localhost:80/create_post", {
                                                                            method: "POST", // or 'PUT'
                                                                            headers: {
                                                                                "Content-Type": "application/json",
                                                                            },
                                                                            mode: 'no-cors',
                                                                            body: payload,
                                                                            });
            }
        }
    }
</script>

<template>
    <div class="h-full gap-5 item flex flex-col">
            <div class="flex flex-col gap-2">
                <label for="title" class="text-xl">Title</label>
                <input type="text" v-model="title" title="title" value="title" class="focus:outline-slate-500 bg-slate-600">
            </div>
            <div class="flex flex-col gap-2">
                <label for="content" class="text-xl">Text:</label>
                <textarea name="content" v-model="content" title="body" cols="30" rows="10" class=" focus:outline-slate-500 bg-slate-600"></textarea>
            </div>  
            <button type="button" @click="post_form" class="self-center w-fit border-solid border-4 rounded-lg bg-blue-900 p-1 hover:bg-blue-950 border-blue-900">Submit</button>
    </div>
</template>