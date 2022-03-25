<script>
	import data from './qa.json';
	let answers = [];
	let index = 0;
	for (let i = 0; i < data[index].answers.length; i++) {
		answers.push(data[index].answers[i]);
		answers[i].clicked = false;
	}

	function handleClick(answerNumber) {
		answers[answerNumber - 1].clicked = !answers[answerNumber - 1].clicked;
	}
</script>

<main>
	<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Logo_of_Family_Feud.png/250px-Logo_of_Family_Feud.png">

	<h1>{ data[index].question }</h1>
	<div class="answer-board">
		{#each answers as answer}
			<div class="answer" on:click|once={handleClick(answer.number)}>
				{#if answer.clicked}
					{ answer.solution }
				{:else}
					{ answer.number }
				{/if}
			</div>
		{/each}
	</div>
</main>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Oswald&display=swap');
	main {
		font-family: 'Oswald';
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		text-transform: uppercase;
		font-size: 2em;
	}

	.answer-board {
		display: flex;
		flex-flow: row wrap;
	}

	.answer {
		flex: 40%;
		font-size: 1.5em;
		background-color: cornflowerblue;
		color: white;
		margin: 1%;
		padding: 1%;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>