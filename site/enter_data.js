//Запись даты в переменную
let userDate;
let myDate;
function value_date() {
	userDate = document.getElementById('enterDate');
	myDate = userDate.value;
	sendToServer(myDate)
};

enterDate.onclick = value_date;

const SERVER_URL ='https://d5d8-93-120-231-18.eu.ngrok.io'
function sendToServer(data) {
	var formData = new FormData();
	formData.append("weather", JSON.stringify(data));
	formData.append("date", JSON.stringify(data));
	let fetchData = {
		method: 'POST',
		body: formData
	};

	return fetch(SERVER_URL + "/predict", fetchData)
		.then((resp) => resp.json())
		.then(function (data) {
			let prediction = data["prediction"]
			console.log(prediction);
			document.getElementById('contentResult').innerHTML = prediction;
		});
}
