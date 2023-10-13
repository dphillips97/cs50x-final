document.addEventListener('DOMContentLoaded', function() {

	// Cancel and return to dashboard
	document.getElementById('btn-cancel-changes').addEventListener('click', redirect);

	// Cancel the visit request
	document.getElementById('btn-cancel-visit').addEventListener('click', cancelVisit);
	
});

function cancelVisit(event) {

	let visitId = this.dataset.instance;

	fetch(`/dogtracks/cancel-visit/${visitId}`, {
		method: 'PUT',
		body: JSON.stringify({'status': 'cancel'}),
		credentials: 'include',
	})
	.then(response => response.json())
	.then(data => {
		if (data['status'] == 'cancel') {
			event.target.innerText = 'Visit Cancelled';
			event.target.classList.add("is-static");
			}
		});
};

function redirect() {
	// Just redirect to dashboard
	document.location.href = '/dogtracks';
};
