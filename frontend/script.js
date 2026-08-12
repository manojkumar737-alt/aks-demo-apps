async function checkHealth(){

    const response = await fetch("http://localhost:5000/health");

    const data = await response.json();

    document.getElementById("status").innerHTML =
    "Backend Status : " + data.status;

}