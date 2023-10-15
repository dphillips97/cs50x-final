document.addEventListener('DOMContentLoaded', function() {

	// Cancel and return to dashboard
	let cancelChangesBtn = document.getElementById('btn-cancel-changes');
	if (cancelChangesBtn !== null) {
		cancelChangesBtn.addEventListener('click', redirect);
	};

	// Cancel the visit request
	let cancelVisitButton = document.getElementById('btn-cancel-visit');
	if (cancelVisitButton !== null) {
		cancelVisitButton.addEventListener('click', cancelVisit);
	};

	// Filter visits
	document.addEventListener('click', filterVisits);

	// Load all visits as default
	filterVisits(event);
	
});

function filterVisits(event) {
// HTML class: filtertype 
// JS argument: filterType
// var passed to API: filterName

	// If visitsDiv exists then we're good to go
	let visitsDiv = document.querySelector('#visits-div');

	if (visitsDiv !== null) {
		
		let filterName = null;

		// Make sure clicked button has filter function
		if (event.target.tagName == 'BUTTON' && event.target.classList.contains('filter')) {
			filterName = event.target.dataset.filtertype;
		} else {
			filterName = 'all';
		}

		// Sanity check
		console.log(`Filtering for visits of type ${filterName}`);

		fetch(`/dogtracks/show-visits/${filterName}`)
		.then(response => response.text())
		.then(text => {
			visitsDiv.innerHTML = text;
		});
	};
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

function redirect() {
	// Just redirect to dashboard
	document.location.href = '/dogtracks';
};
