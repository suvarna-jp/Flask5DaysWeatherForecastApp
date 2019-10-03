from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, sys, json
import WeatherForecastAPIAppModel as wapi
from WeatherCommons import DEBUG_MODE

weatherapp = Flask(__name__)
weatherapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///worldcities_crisp.db'
db = SQLAlchemy(weatherapp)


class WorldCity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cityID = db.Column(db.String(20), unique=True, nullable=False)
    cityName = db.Column(db.String(80), nullable=False)
    cityCountry = db.Column(db.String(120), nullable=False)
    cityLongitude = db.Column(db.String(80), nullable=False)
    cityLatitude = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<City {self.cityName}>'

def getWeatherByCityName(city_name, country_code):
    """Reads args city_name, country_code and passes it to model's getWeatherInfo() 
    which inturn makes an api call
    @param : city_name, country_code
    @return : weatherjsonobj, errormessage
    @param for getWeatherInfo() : dict['CITY_NAME' | 'CITY_ID' | 'LAT_LON' | 'ZIP_CODE'] 
    @return from getWeatherInfo() : dict{'RESPONSE':'$EMPTY$', 'RESPONSE_OBJ':None}
    'RESPONSE':'$EMPTY$' | '$ERROR$' | '$EXCEPT$' | '$SUCCESS$'
    'RESPONSE_OBJ':None | sys.exc_info() | json_data"""

    if DEBUG_MODE:
            print("[DEBUG] :: In getWeatherByCityName()")
    
    if(city_name is None or city_name.strip() == ''):
        if DEBUG_MODE:
            print("[EMPTY] :: city_name is null/empty")
        return {"RESPONSE":"$EMPTY$", "RESPONSE_OBJ":None}

    api_response = None
    weatherjsonobj = []
    errormessage = None
    if(country_code is not None):
        # weatherobj = WorldCity.query.filter(and_(cityName==city_name, cityCountry==country_code)).all()
        # if(weatherobj is not None):
        #     api_response = wapi.getWeatherInfo({"CITY_NAME" : f"{city_name},{country_code}"})
        api_response = wapi.getWeatherInfo({"CITY_NAME" : f"{city_name},{country_code}"})
    else:
        # weatherobj = WorldCity.query.filter(cityName==city_name).all()
        # # country_code = "US"
        # if(weatherobj is not None):
        #     # api_response = wapi.getWeatherInfo({"CITY_NAME" : f"{city_name},{country_code}"})
        #     api_response = wapi.getWeatherInfo({"CITY_NAME" : f"{city_name}"})
        api_response = wapi.getWeatherInfo({"CITY_NAME" : f"{city_name}"})

    if(api_response is None):
        if DEBUG_MODE:
            print("{'RESPONSE':'$NULL$', 'RESPONSE_OBJ':None}")
        errormessage = ["Sorry! An error occured while fetching data.", 
            "Try again after some time.", "Please <a>report to admin</a> if the problem persists"]
    elif(api_response.get('RESPONSE')=='$SUCCESS$'):
        # weatherjsonobj = json.load(api_response.get('RESPONSE_OBJ'))
        weatherjsonobj = api_response.get('RESPONSE_OBJ')
        # weatherjsonobj = handleWeatherOutput(weatherjsonobj)
        if DEBUG_MODE:
            print(f"weatherjsonobj :: {weatherjsonobj}")
    elif(api_response.get('RESPONSE')=='$ERROR$'):
        if DEBUG_MODE:
            print(f"[ERROR] :: Exception occured in APIModel")
        errormessage = ["Sorry! An error occured while fetching data.", 
            "Try again after some time.", "Please <a>report to admin</a> if the problem persists"]    
    elif(api_response.get('RESPONSE')=='$EXCEPT$'):
        if DEBUG_MODE:
            print(f"[EXCEPT] :: Exception occured in APIModel")
        errormessage = ["Sorry! An error occured while fetching data.", 
            "Try again after some time.", "Please <a>report to admin</a> if the problem persists"]
    else:
        if DEBUG_MODE:
            print(f"[UNEXPECTED] :: Unexpected response from APIModel")
        errormessage = ["Sorry! An error occured while fetching data.", 
            "Try again after some time.", "Please <a>report to admin</a> if the problem persists"]

    return weatherjsonobj, errormessage


def getWeatherByCityID(city_id):
    """Reads args city_id, country_code and passes it to model's getWeatherInfo() 
    which inturn makes an api call
    @param : city_id, country_code
    @return : weatherjsonobj, errormessage
    @param for getWeatherInfo() : dict['CITY_NAME' | 'CITY_ID' | 'LAT_LON' | 'ZIP_CODE'] 
    @return from getWeatherInfo() : dict{'RESPONSE':'$EMPTY$', 'RESPONSE_OBJ':None}
    'RESPONSE':'$EMPTY$' | '$ERROR$' | '$EXCEPT$' | '$SUCCESS$'
    'RESPONSE_OBJ':None | sys.exc_info() | json_data"""

    if DEBUG_MODE:
            print("[DEBUG] :: In getWeatherByCityID()")
    
    if(city_id is None or city_id.strip() == ''):
        if DEBUG_MODE:
            print("[EMPTY] :: city_id is null/empty")
        return {"RESPONSE":"$EMPTY$", "RESPONSE_OBJ":None}

    api_response = None
    weatherjsonobj = []
    errormessage = None
    api_response = wapi.getWeatherInfo({"CITY_ID" : f"{city_id}"})

    if(api_response is None):
        if DEBUG_MODE:
            print("{'RESPONSE':'$NULL$', 'RESPONSE_OBJ':None}")
        errormessage = ["Sorry! An error occured while fetching data.", 
            "Try again after some time.", "Please <a>report to admin</a> if the problem persists"]
    elif(api_response.get('RESPONSE')=='$SUCCESS$'):
        # weatherjsonobj = json.load(api_response.get('RESPONSE_OBJ'))
        weatherjsonobj = api_response.get('RESPONSE_OBJ')
        # weatherjsonobj = handleWeatherOutput(weatherjsonobj)
        if DEBUG_MODE:
            print(f"weatherjsonobj :: {weatherjsonobj}")
    elif(api_response.get('RESPONSE')=='$ERROR$'):
        if DEBUG_MODE:
            print(f"[ERROR] :: Exception occured in APIModel")
        errormessage = ["Sorry! An error occured while fetching data.", 
            "Try again after some time.", "Please <a>report to admin</a> if the problem persists"]    
    elif(api_response.get('RESPONSE')=='$EXCEPT$'):
        if DEBUG_MODE:
            print(f"[EXCEPT] :: Exception occured in APIModel")
        errormessage = ["Sorry! An error occured while fetching data.", 
            "Try again after some time.", "Please <a>report to admin</a> if the problem persists"]
    else:
        if DEBUG_MODE:
            print(f"[UNEXPECTED] :: Unexpected response from APIModel")
        errormessage = ["Sorry! An error occured while fetching data.", 
            "Try again after some time.", "Please <a>report to admin</a> if the problem persists"]

    if DEBUG_MODE:
        print(f"weatherjsonobj :: {weatherjsonobj}")
        print(f"errormessage :: {errormessage}")
    return weatherjsonobj, errormessage


def getWeatherByGeoCoords(latitude, longitude):
    """Reads args latitude, longitude and passes it to model's getWeatherInfo() 
    which inturn makes an api call
    @param : latitude, longitude
    @return : weatherjsonobj, errormessage
    @param for getWeatherInfo() : dict['CITY_NAME' | 'CITY_ID' | 'LAT_LON' | 'ZIP_CODE'] 
    @return from getWeatherInfo() : dict{'RESPONSE':'$EMPTY$', 'RESPONSE_OBJ':None}
    'RESPONSE':'$EMPTY$' | '$ERROR$' | '$EXCEPT$' | '$SUCCESS$'
    'RESPONSE_OBJ':None | sys.exc_info() | json_data"""

    if DEBUG_MODE:
            print("[DEBUG] :: In getWeatherByGeoCoords()")
    
    if(latitude is None or latitude.strip() == '' or longitude is None or longitude.strip() == ''):
        if DEBUG_MODE:
            print("[EMPTY] :: latitude/longitude is null/empty")
        return {"RESPONSE":"$EMPTY$", "RESPONSE_OBJ":None}

    api_response = None
    weatherjsonobj = []
    errormessage = None
    api_response = wapi.getWeatherInfo({"LAT_LON" : None, "LAT": latitude, "LON": longitude})
    
    if(api_response is None):
        if DEBUG_MODE:
            print("{'RESPONSE':'$NULL$', 'RESPONSE_OBJ':None}")
        errormessage = ["Sorry! An error occured while fetching data.", 
            "Try again after some time.", "Please <a>report to admin</a> if the problem persists"]
    elif(api_response.get('RESPONSE')=='$SUCCESS$'):
        weatherjsonobj = api_response.get('RESPONSE_OBJ')
        if DEBUG_MODE:
            print(f"weatherjsonobj :: {weatherjsonobj}")
    elif(api_response.get('RESPONSE')=='$ERROR$'):
        if DEBUG_MODE:
            print(f"[ERROR] :: Exception occured in APIModel")
        errormessage = ["Sorry! An error occured while fetching data.", 
            "Try again after some time.", "Please <a>report to admin</a> if the problem persists"]    
    elif(api_response.get('RESPONSE')=='$EXCEPT$'):
        if DEBUG_MODE:
            print(f"[EXCEPT] :: Exception occured in APIModel")
        errormessage = ["Sorry! An error occured while fetching data.", 
            "Try again after some time.", "Please <a>report to admin</a> if the problem persists"]
    else:
        if DEBUG_MODE:
            print(f"[UNEXPECTED] :: Unexpected response from APIModel")
        errormessage = ["Sorry! An error occured while fetching data.", 
            "Try again after some time.", "Please <a>report to admin</a> if the problem persists"]

    return weatherjsonobj, errormessage


def getWeatherByZipCode(zip_code, country_code):
    """Reads args city_id, country_code and passes it to model's getWeatherInfo() 
    which inturn makes an api call
    @param : city_id, country_code
    @return : weatherjsonobj, errormessage
    @param for getWeatherInfo() : dict['CITY_NAME' | 'CITY_ID' | 'LAT_LON' | 'ZIP_CODE'] 
    @return from getWeatherInfo() : dict{'RESPONSE':'$EMPTY$', 'RESPONSE_OBJ':None}
    'RESPONSE':'$EMPTY$' | '$ERROR$' | '$EXCEPT$' | '$SUCCESS$'
    'RESPONSE_OBJ':None | sys.exc_info() | json_data"""

    if DEBUG_MODE:
            print("[DEBUG] :: In getWeatherByZipCode()")
    
    if(zip_code is None or zip_code.strip() == ''):
        if DEBUG_MODE:
            print("[EMPTY] :: zip_code is null/empty")
        return {"RESPONSE":"$EMPTY$", "RESPONSE_OBJ":None}

    api_response = None
    weatherjsonobj = []
    errormessage = None
    if(country_code is not None):
        # weatherobj = WorldCity.query.filter(and_(cityName==city_name, cityCountry==country_code)).all()
        # if(weatherobj is not None):
        #     api_response = wapi.getWeatherInfo({"CITY_NAME" : f"{city_name},{country_code}"})
        api_response = wapi.getWeatherInfo({"ZIP_CODE" : f"{zip_code},{country_code}"})
    else:
        # weatherobj = WorldCity.query.filter(cityName==city_name).all()
        # # country_code = "US"
        # if(weatherobj is not None):
        #     # api_response = wapi.getWeatherInfo({"CITY_NAME" : f"{city_name},{country_code}"})
        #     api_response = wapi.getWeatherInfo({"CITY_NAME" : f"{city_name}"})
        api_response = wapi.getWeatherInfo({"ZIP_CODE" : f"{zip_code}"})

    if(api_response is None):
        if DEBUG_MODE:
            print("{'RESPONSE':'$NULL$', 'RESPONSE_OBJ':None}")
        errormessage = ["Sorry! An error occured while fetching data.", 
            "Try again after some time.", "Please <a>report to admin</a> if the problem persists"]
    elif(api_response.get('RESPONSE')=='$SUCCESS$'):
        # weatherjsonobj = json.load(api_response.get('RESPONSE_OBJ'))
        weatherjsonobj = api_response.get('RESPONSE_OBJ')
        # weatherjsonobj = handleWeatherOutput(weatherjsonobj)
        if DEBUG_MODE:
            print(f"weatherjsonobj :: {weatherjsonobj}")
    elif(api_response.get('RESPONSE')=='$ERROR$'):
        if DEBUG_MODE:
            print(f"[ERROR] :: Exception occured in APIModel")
        errormessage = ["Sorry! An error occured while fetching data.", 
            "Try again after some time.", "Please <a>report to admin</a> if the problem persists"]    
    elif(api_response.get('RESPONSE')=='$EXCEPT$'):
        if DEBUG_MODE:
            print(f"[EXCEPT] :: Exception occured in APIModel")
        errormessage = ["Sorry! An error occured while fetching data.", 
            "Try again after some time.", "Please <a>report to admin</a> if the problem persists"]
    else:
        if DEBUG_MODE:
            print(f"[UNEXPECTED] :: Unexpected response from APIModel")
        errormessage = ["Sorry! An error occured while fetching data.", 
            "Try again after some time.", "Please <a>report to admin</a> if the problem persists"]

    return weatherjsonobj, errormessage


def getWeather():
    
    # getWeather_response = getWeatherByCityName("Bangalore", "IN")
    # if(getWeather_response is None):
    #     pass
    # elif (getWeather_response.get('RESPONSE') == '$NULL$')

    # for data:WorldCity in weather_obj:
    #     print(data.
    return render_template('WeatherQuery.html')
