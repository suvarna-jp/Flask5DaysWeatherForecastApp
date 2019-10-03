import requests
import sys
import WeatherCommons
from WeatherCommons import API_URL, DEBUG_MODE

API_CALL = API_URL


def getWeatherInfo(queryDict: dict):
    """Reads dictionary object and based on the key, makes an api call
    @param : dict['CITY_NAME' | 'CITY_ID' | 'LAT_LON' | 'ZIP_CODE'] 
    @return : dict{'RESPONSE':'$EMPTY$', 'RESPONSE_OBJ':None}
    'RESPONSE':'$EMPTY$' | '$ERROR$' | '$EXCEPT$' | '$SUCCESS$'
    'RESPONSE_OBJ':None | sys.exc_info() | json_data"""

    if DEBUG_MODE:
        print("[DEBUG] :: Inside getWeatherInfo()")

    global API_CALL

    API_CALL = API_URL

    if (queryDict is None or len(queryDict) <= 0):
        if DEBUG_MODE:
            print(f"[EMPTY] :: queryDict is null or empty :: {queryDict}")
        return {'RESPONSE':'$EMPTY$', 'RESPONSE_OBJ':None}
    elif ('CITY_NAME' in queryDict.keys()):
        API_CALL += '&q=' + queryDict.get('CITY_NAME') + '&units=metric'
    elif ('CITY_ID' in queryDict.keys()):
        API_CALL += '&id=' + queryDict.get('CITY_ID') + '&units=metric'
    elif ('LAT_LON' in queryDict.keys()):
        API_CALL += '&lat=' + queryDict.get('LAT') + '&lon=' + queryDict.get('LON') + '&units=metric'
    elif ('ZIP_CODE' in queryDict.keys()):
        API_CALL += '&zip=' + queryDict.get('ZIP_CODE') + '&units=metric'
    else:
        if DEBUG_MODE:
            print(f"[ERROR] :: UNEXPECTED! Reached 'else' in queryDict check :: {queryDict}")
        return {'RESPONSE':'$ERROR$', 'RESPONSE_OBJ':None}


    if DEBUG_MODE:
        print(f"[DEBUG] :: API_CALL :: {API_CALL}")

    try:
        json_data = requests.get(API_CALL).json()
        if DEBUG_MODE:
            print(f"[DEBUG] :: In Model, JSON Data :: {json_data}") 
        return {'RESPONSE':'$SUCCESS$', 'RESPONSE_OBJ':json_data}

    except:
        if DEBUG_MODE:
            print(f"[EXCEPT] :: Caught Exception during JSON call :: {sys.exc_info()}")
        return {'RESPONSE':'$EXCEPT$', 'RESPONSE_OBJ':sys.exc_info()}

