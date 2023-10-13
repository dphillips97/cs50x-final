document.addEventListener('DOMContentLoaded', function() {

	// Cancel and return to dashboard
	let cancelChangesBtn = document.getElementById('btn-cancel-changes');
	if (cancelChangesBtn !== null) {
		cancelChangesBtn.addEventListener('click', redirect);
	};

	// Filter visits
	document.addEventListener('click', filterVisits);

	// Cancel the visit request
	let cancelVisitButton = document.getElementById('btn-cancel-visit');
	if (cancelVisitButton !== null) {
		cancelVisitButton.addEventListener('click', cancelVisit);
	};
	
});

function filterVisits(event) {
	var filterButton = event.target;
	if (filterButton.classList.contains('filter')) {
		
		let filterName = filterButton.dataset.filtertype;
		console.log(`Filtering for visits of type ${filterName}`);

		fetch(`/dogtracks/show-visits/${filterName}`, {
			method:'GET'
		})
		.then(response => response.json())
		.then(data => {
    		data.visits.forEach(visit => {
    			console.log(`${visit['id']}`);
			}) // Close forEach
		}) // Close last 'then'
	}; // Close if
};

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

function filterVisitsRequest(event) {
	console.log('Filter by request click');
};

function redirect() {
	// Just redirect to dashboard
	document.location.href = '/dogtracks';
};
