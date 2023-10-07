document.addEventListener('DOMContentLoaded', function() {

	document.getElementById('btn-cancel').addEventListener('click', () => {
		document.location.href = '/dogtracks';
	});

	document.getElementById('btn-cancel-visit').addEventListener('click', visitStatus);
});

function visitStatus(event) {

	let visitId = this.dataset.instance;

	fetch(`visit/${visitId}`, {
		method: 'PUT',
		body: JSON.stringify({cancel: true})
	})
	.then(response => response.json())
};
