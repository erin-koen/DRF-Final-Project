<template>
    <div class="home">
        <div class="container"></div>
				<div>
					<p class="mb-0">Posted by: <span>{{ question.author }}</span></p>
					<h2>{{question.content}}</h2>
				</div>
    </div>
</template>

<script>
import { apiService } from "../common/api.service.js";

export default {
    name: "home",
    data() {
        return {
            questions: []
        };
    },
    methods: {
        getQuestions() {
            let endpoint = "api/questions/";
            apiService(endpoint).then(data =>
                this.questions.push(...data.results)
            );
        }
		},
		// lifecycle method below
		created(){
			this.getQuestions()
		}
	
};
</script>
