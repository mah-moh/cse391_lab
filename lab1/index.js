const page_location = window.location.href;
const text = document.lastModified;

const date = new Date(document.lastModified);

document.getElementById('date_of_modification').innerHTML = "Last updated on " +text+ " at " +page_location;


let loader = document.getElementById("preloader");
window.addEventListener("load", function () {
  loader.style.display = "none";
});