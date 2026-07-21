import axios from "axios";

const API = axios.create({
    baseURL: "http://localhost:8000",

});
fetch("http://localhost:8000/devices/")
    .then(response => response.json())
    .then(data => console.log(data));
export default API;

