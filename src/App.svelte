<script>
	import * as data from './qa.json';
	console.log(data);
	export let question;
	export let answers;
</script>

<main>
	<h1>{ question }</h1>
	{#each answers as answer}
		<p>{ answer }</p>
	{/each}
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>