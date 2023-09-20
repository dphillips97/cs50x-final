document.addEventListener('DOMContentLoaded', function() {

	document.getElementById('btn-cancel').addEventListener('click', () => {
		document.location.href = '/dogtracks';
	});

	document.getElementById('btn-remove').addEventListener('click', removePet);
});

function removePet(id) {
	let url = `http://127.0.0.1:8000/docktracks/remove-pet/${id}`;

	fetch(url, {
		method: 'DELETE',
		body: JSON.stringify({"data": id}),
		headers: {
			"Content-Type": "application/json",
			}})
	.then((res) => res.json())
	.catch((error) => console.error("Error:", error))
	.then((response) => console.log("Success:", response));
};