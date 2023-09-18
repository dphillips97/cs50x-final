document.addEventListener('DOMContentLoaded', (event) => {

	console.log('Content loaded');
	document.querySelector('#btn-cancel').addEventListener("click", dashRedirect);

});


function dashRedirect(event) {
	console.log("Cancel clicked");
};