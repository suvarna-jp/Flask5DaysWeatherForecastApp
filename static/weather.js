// Function to check if the charachter is an alphabet
function isAlpha(ch) {
    return (((ch >= 'a') && (ch <= 'z')) || ((ch >= 'A') && (ch <= 'Z')));
}

// Function to check if the input is a valid city name
function isCityNameValid(str) {
    let strArray = str.split('');
    // for(let ch=0; ch<strArray.length; ch++) {
    //     if (validateCityOrPostalCode(strArray[ch]) == false) {
    //         console.log("Char :: " + strArray[ch] + "is invalid in a City name.")
    //         return false;
    //     }
    // };
    return true;
}

function isCityIDValid(str) {
    let strArray = str.split('');
    // for(let ch=0; ch<strArray.length; ch++) {
    //     if (validateCityOrPostalCode(strArray[ch]) == false) {
    //         console.log("Char :: " + strArray[ch] + "is invalid in a City name.")
    //         return false;
    //     }
    // };
    return true;
}

function isCityLatitudeValid(str) {
    let strArray = str.split('');
    // for(let ch=0; ch<strArray.length; ch++) {
    //     if (validateCityOrPostalCode(strArray[ch]) == false) {
    //         console.log("Char :: " + strArray[ch] + "is invalid in a City name.")
    //         return false;
    //     }
    // };
    return true;
}

function isCityLongitudeValid(str) {
    let strArray = str.split('');
    // for(let ch=0; ch<strArray.length; ch++) {
    //     if (validateCityOrPostalCode(strArray[ch]) == false) {
    //         console.log("Char :: " + strArray[ch] + "is invalid in a City name.")
    //         return false;
    //     }
    // };
    return true;
}

function isCityZipCodeValid(str) {
    let strArray = str.split('');
    // for(let ch=0; ch<strArray.length; ch++) {
    //     if (validateCityOrPostalCode(strArray[ch]) == false) {
    //         console.log("Char :: " + strArray[ch] + "is invalid in a City name.")
    //         return false;
    //     }
    // };
    return true;
}

function isCountryValid(str) {
    let strArray = str.split('');
    // for(let ch=0; ch<strArray.length; ch++) {
    //     if (validateCityOrPostalCode(strArray[ch]) == false) {
    //         console.log("Char :: " + strArray[ch] + "is invalid in a City name.")
    //         return false;
    //     }
    // };
    return true;
}

// Function to check if the charachter is a digit
function isDigit(ch) {
    return ((ch >= 0) && (ch <= 9));
}

function validateCityOrPostalCode(value) {
    // return /^([0-9]{5}|[a-zA-Z][a-zA-Z ]{0,49})$/.test(value);
    return /^[a-zA-Z\u0080-\u024F]+(?:. |-| |')*/.test(value)
}

// Function to check if the charachter is a digit
function isNumber(str) {
    let strArray = str.split('');
    for(let ch=0; ch<strArray.length; ch++) {
        if (isDigit(strArray[ch]) == false) {
            return false;
        }
    };
    return true;
}

function searchWeather() {
    console.log("Redirecting to Weather search page");

    let searchOption = null

    const ele = document.getElementsByName('searchOption'); 
              
    for(i = 0; i < ele.length; i++) { 
        if(ele[i].checked) 
        {
            console.log("Selected Search by :: " + ele[i].id)
            searchOption = ele[i].id
        }         
    } 

    if(searchOption != null)
    {
        if(searchOption == 'city_name'){
            console.log("Redirecting to /weathersearchcityname");
            document.location.href='/weathersearchcityname';
        }
        else if(searchOption == 'city_id'){
            console.log("Redirecting to /weathersearchcityid");
            document.location.href='/weathersearchcityid';
        }
        else if(searchOption == 'geo_co_ord'){
            console.log("Redirecting to /weathersearchgeocoord");
            document.location.href='/weathersearchgeocoord';
        }
        else if(searchOption == 'zip_code'){
            console.log("Redirecting to /weathersearchzipcode");
            document.location.href='/weathersearchzipcode';
        }
    }    
}

function submitCityName() {
    const city_name = document.getElementById('input_city_name').value;
    const country_code = document.getElementById('input_country_code').value;

    console.log("Validating city_name : " + city_name);
    console.log("Validating country_code : " + country_code);
  
    if(isCityNameValid(city_name)){
        console.log(city_name + "is valid!");
    }
    else{
        console.log(city_name + " is INVALID");
        alert("Please Enter a valid City Name");
        document.getElementById('input_city_name').focus();
    }
    
    if(isCountryValid(country_code)){
        console.log(country_code + "is valid!");
    }
    else{
        console.log(country_code + " is INVALID");
        alert("Please Enter a valid Country Code");
        document.getElementById('input_country_code').focus();
    }
    
    document.getElementById("searchCityNameForm").method = 'POST';
    document.getElementById("searchCityNameForm").submit();
}

function resetCityName() {
    document.getElementById('input_city_name').value = "";
    document.getElementById('input_country_code').value = "";
    console.log("1");
    document.getElementById('input_city_name').innerText = "";
    document.getElementById('input_country_code').innerText = "";
    console.log("2");
    if(document.getElementById('cityweather') != null) {
        document.getElementById('cityweather').style.display = "none";
        console.log("3");
    }
    if(document.getElementById('errormessage2') != null) {
        document.getElementById('errormessage2').style.display = "none";
        console.log("4");
    }
    if(document.getElementById('errormessage') != null) {
        document.getElementById('errormessage').style.display = "none";
        console.log("5");
    }
}

function submitCityID() {
    const city_id = document.getElementById('input_city_id').value;
    console.log("Validating city : " + city_id);
  
    if(isCityIDValid(city_id)){
        console.log(city_id + "is valid!");
        document.getElementById("searchCityIDForm").method = 'POST';
        document.getElementById("searchCityIDForm").submit();
    }
    else{
        console.log(city_id + " is INVALID");
        alert("Please Enter a valid City ID");
        document.getElementById('input_city_id').focus();
    }

}

function resetCityID() {
    document.getElementById('input_city_id').value = "";
    console.log("1");
    document.getElementById('input_city_id').innerText = "";
    console.log("2");
    if(document.getElementById('cityweather') != null) {
        document.getElementById('cityweather').style.display = "none";
        console.log("3");
    }
    if(document.getElementById('errormessage2') != null) {
        document.getElementById('errormessage2').style.display = "none";
        console.log("4");
    }
    if(document.getElementById('errormessage') != null) {
        document.getElementById('errormessage').style.display = "none";
        console.log("5");
    }
}

function submitGeoCoords() {
    const city_latitude = document.getElementById('input_latitude').value;
    const city_longitude = document.getElementById('input_longitude').value;
    console.log("Validating city_latitude : " + city_latitude);
    console.log("Validating city_longitude : " + city_longitude);

  
    if(isCityLatitudeValid(city_latitude)){
        console.log(city_latitude + "is valid!");        
    }
    else{
        console.log(city_latitude + " is INVALID");
        alert("Please Enter a valid City Latitude");
        document.getElementById('input_latitude').focus();
    }

    if(isCityLongitudeValid(city_longitude)){
        console.log(city_longitude + "is valid!");        
    }
    else{
        console.log(city_longitude + " is INVALID");
        alert("Please Enter a valid City Longitude");
        document.getElementById('input_longitude').focus();
    }

    document.getElementById("searchGeoCoordsForm").method = 'POST';
    document.getElementById("searchGeoCoordsForm").submit();

}

function resetGeoCoords() {
    document.getElementById('input_latitude').value = "";
    document.getElementById('input_longitude').value = "";
    console.log("1");
    document.getElementById('input_latitude').innerText = "";
    document.getElementById('input_longitude').innerText = "";
    console.log("2");
    if(document.getElementById('cityweather') != null) {
        document.getElementById('cityweather').style.display = "none";
        console.log("3");
    }
    if(document.getElementById('errormessage2') != null) {
        document.getElementById('errormessage2').style.display = "none";
        console.log("4");
    }
    if(document.getElementById('errormessage') != null) {
        document.getElementById('errormessage').style.display = "none";
        console.log("5");
    }
}

function submitZipCode() {
    const city_zip_code = document.getElementById('input_zip_code').value;
    const country_code = document.getElementById('input_country_code').value;

    console.log("Validating input_zip_code : " + city_zip_code);
    console.log("Validating input_country_code : " + country_code);
  
    if(isCityZipCodeValid(city_zip_code)){
        console.log(city_zip_code + "is valid!");
    }
    else{
        console.log(city_zip_code + " is INVALID");
        alert("Please Enter a valid City Zip Code");
        document.getElementById('input_zip_code').focus();
    }

    if(isCountryValid(country_code)){
        console.log(country_code + "is valid!");
    }
    else{
        console.log(country_code + " is INVALID");
        alert("Please Enter a valid Country Code");
        document.getElementById('input_country_code').focus();
    }
    
    document.getElementById("searchZipCodeForm").method = 'POST';
    document.getElementById("searchZipCodeForm").submit();
}

function resetZipCode() {
    document.getElementById('input_zip_code').value = "";
    document.getElementById('input_country_code').value = "";
    console.log("1");
    document.getElementById('input_zip_code').innerText = "";
    document.getElementById('input_country_code').innerText = "";
    console.log("2");
    if(document.getElementById('cityweather') != null) {
        document.getElementById('cityweather').style.display = "none";
        console.log("3");
    }
    if(document.getElementById('errormessage2') != null) {
        document.getElementById('errormessage2').style.display = "none";
        console.log("4");
    }
    if(document.getElementById('errormessage') != null) {
        document.getElementById('errormessage').style.display = "none";
        console.log("5");
    }
}

function backToSearchTypePage() {
    window.location.href = "/weatherOptions";
    // window.location.replace("/weatherOptions");
}


//Event Handlers for City Name page Submit & Reset buttons
const city_name_sbmt_btn = document.querySelector('#city_name_sbmt');

if(city_name_sbmt_btn != null) {
    city_name_sbmt_btn.addEventListener('click', e=> {
        e.preventDefault();
        submitCityName();
    })
}

const city_name_reset_btn = document.querySelector('#city_name_reset');

if(city_name_reset_btn != null) {
    city_name_reset_btn.addEventListener('click', e=> {
        e.preventDefault();
        resetCityName();
    })
}

const back_search_type_btn = document.querySelector('#btn_back_search_type');

if(back_search_type_btn != null) {
    console.log("back_search_type_btn is not null");
    back_search_type_btn.addEventListener('click', e=> {
        e.preventDefault();
        console.log("Redirecting back to Search Page");
        backToSearchTypePage();
    })
}

//Event Handlers for City ID page Submit & Reset buttons
const city_id_sbmt_btn = document.querySelector('#city_id_sbmt');

if(city_id_sbmt_btn != null) {
    city_id_sbmt_btn.addEventListener('click', e=> {
        e.preventDefault();
        console.log("Inside city_id_sbmt_btn")
        submitCityID();
    })
}

const city_id_reset_btn = document.querySelector('#city_id_reset');

if(city_id_reset_btn != null) {
    city_id_reset_btn.addEventListener('click', e=> {
        e.preventDefault();
        resetCityID();
    })
}

//Event Handlers for Geo Coords page Submit & Reset buttons
const geo_coords_sbmt_btn = document.querySelector('#lat_lon_sbmt');

if(geo_coords_sbmt_btn != null) {
    geo_coords_sbmt_btn.addEventListener('click', e=> {
        e.preventDefault();
        submitGeoCoords();
    })
}

const geo_coords_reset_btn = document.querySelector('#lat_lon_reset');

if(geo_coords_reset_btn != null) {
    geo_coords_reset_btn.addEventListener('click', e=> {
        e.preventDefault();
        resetGeoCoords();
    })
}

//Event Handlers for Zip Code page Submit & Reset buttons
const zip_code_sbmt_btn = document.querySelector('#zip_code_sbmt');

if(zip_code_sbmt_btn != null) {
    zip_code_sbmt_btn.addEventListener('click', e=> {
        e.preventDefault();
        submitZipCode();
    })
}

const zip_code_reset_btn = document.querySelector('#zip_code_reset');

if(zip_code_reset_btn != null) {
    zip_code_reset_btn.addEventListener('click', e=> {
        e.preventDefault();
        resetZipCode();
    })
}
