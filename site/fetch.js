const urlServer = 'https://jsonplaceholder.typicode.com/users';
function sendRequest(method, url, body = null) {
    const headers = {
        'Content-Type':'application/json'
    }
    return fetch(url, {
        method: method,
        body: JSON.stringify(body),
        headers: headers
    }).then(Response => {
        return Response.json()
    })

    }

const body = {
    result: '20'

}
sendRequest('POST', urlServer, body)
    .then(data => console.log(data))
    .catch(err => console.log(err))


let result;
result = body.result;
document.getElementById("content_result").innerHTML = result;