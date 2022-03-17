import App from './App.svelte';

const app = new App({
	target: document.body,
	props: {
		question: 'Name a physician specialty that earns the most money in the medical field.',
		answers: [
			"Plastic Surgery",
			"Orthopedics",
			"Cardiology",
			"Uronology",
			"ENT/Otolaryngology",
			"Radiology",
			"Gastroenterology",
			"Oncology",
		]
	}
});

export default app;