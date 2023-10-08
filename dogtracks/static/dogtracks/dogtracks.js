document.addEventListener('DOMContentLoaded', function() {

	document.getElementById('btn-cancel').addEventListener('click', redirect);

	document.getElementById('btn-alter-visit').addEventListener('click', visitStatus);
});

function visitStatus(event) {

	let visitId = this.dataset.instance;

	let visitStatus = this.dataset.status;


	fetch(`/dogtracks/visit-status/${visitId}`, {
		method: 'PUT',
		body: JSON.stringify({'status': visitStatus}),
		credentials: 'include',
	})
	.then(response => response.json())
	.then(redirect());
};

function redirect() {
	// Just redirect to dashboard
	document.location.href = '/dogtracks';
};
