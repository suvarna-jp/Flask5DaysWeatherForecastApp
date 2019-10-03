function checkCityName() {
    alert("Checking city name...")
}

function resetCityName() {
    alert("Shall Reset city name...")
}


//Event Handlers for Assignment 04 Submit & Reset buttons
const city_name_sbmt_btn = document.querySelector('#city_name_sbmt');

city_name_sbmt_btn.addEventListener('click', e=> {
    e.preventDefault();
    checkCityName();
})

const city_name_reset_btn = document.querySelector('#city_name_reset');

city_name_reset_btn.addEventListener('click', e=> {
    e.preventDefault();
    resetCityName();
})