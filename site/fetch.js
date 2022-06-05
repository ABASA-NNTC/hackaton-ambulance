const SERVER_URL ='https://d5d8-93-120-231-18.eu.ngrok.io'
function sendToServer(data) {
	var formData = new FormData();
	formData.append("weather", JSON.stringify(data));
	formData.append("date", JSON.stringify(data));
	let fetchData = {
		method: 'POST',
		body: formData,
		headers: {
			//'Access-Control-Allow-Origin': '*'
		},  
	};

	return fetch(SERVER_URL + "/predict", fetchData)
		.then((resp) => resp.json())
		.then(function (data) {
			console.log(data);
			drawGJS(data);
		});
}
var currentdate = new Date(2022, 4, 5)
sendToServer(currentdate)