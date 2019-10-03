from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, sys, json

weatherapp = Flask(__name__)
weatherapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///worldcities.db'
# weatherapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///worldcities_test.db'
db = SQLAlchemy(weatherapp)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cityID = db.Column(db.String(20), unique=True, nullable=False)
    cityName = db.Column(db.String(80), nullable=False)
    cityCountry = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<City {self.cityName}>'

class WorldCity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cityID = db.Column(db.String(20), unique=True, nullable=False)
    cityName = db.Column(db.String(80), nullable=False)
    cityCountry = db.Column(db.String(120), nullable=False)
    cityLongitude = db.Column(db.String(80), nullable=False)
    cityLatitude = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<City {self.cityName}>'

def tryWritingUsingJson():
    try:
        data = {}
        data['people'] = []
        data['people'].append({
            'name': 'Scott',
            'website': 'stackabuse.com',
            'from': 'Nebraska'
        })
        data['people'].append({
            'name': 'Larry',
            'website': 'google.com',
            'from': 'Michigan'
        })
        data['people'].append({
            'name': 'Tim',
            'website': 'apple.com',
            'from': 'Alabama'
        })

        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)
    except:
        print("Sorry! Exception Occured :: ", sys.exc_info())

    print("Done!! ")

def populateCityUsingJson():
    datastore = []
    try:
        with open('city.list.json', encoding="utf8") as json_file:
            datastore = json.load(json_file)
    except:
        print("Sorry! Exception Occured while loading file :: ", sys.exc_info())

    db.create_all()
    #Use the new datastore datastructure
    try:
        print("---id---", "-----name-----", "-----country-----", "---coord-lon---", "---coord-lat---")
        for data in datastore:
            print(data["id"], data["name"], data["country"], data["coord"]["lon"], data["coord"]["lat"])
            citydata = WorldCity(
                cityID=data["id"], 
                cityName=data["name"], 
                cityCountry=data["country"],
                cityLongitude=data["coord"]["lon"], 
                cityLatitude=data["coord"]["lat"])
            # print("Again!! citydata ::: ", citydata)
            db.session.add(citydata)
            db.session.commit()
    except:
        print("Sorry! Exception Occured while populating DB Table WorldCity :: ", sys.exc_info())


def populateCity():
    try:
        f = open("static/World_CityID_CityName_Country_TuplesList.txt", "r", encoding="utf8") 
        # f = open("static/ids_cities_countries_List.txt", "r", encoding="utf8")
        city_list = f.read()
        city_list = city_list[1:-1]
        city_list = city_list.split(',')
        city_id = None
        city_name = None
        city_country = None
        citycounter = 0
        iter_count = 0
        row_count = 0
        records_count = 0
        for city_iter in city_list:
            # print("city_iter ::::", city_iter)
            # print("citycounter ::::", citycounter)
            quote_counter = city_iter.count("'")
            dblquote_counter = city_iter.count('"') 
            if(quote_counter >= 2):
                city_iter = city_iter[city_iter.index("'")+1:city_iter.rindex("'")]
            elif(dblquote_counter >= 2):
                city_iter = city_iter[city_iter.index('"')+1:city_iter.rindex('"')]
            elif(city_iter.strip() == ''):
                city_iter = city_iter
                print("TO BE NOTED ::: EMPTY VALUE Coming in ::::: ", city_iter)
            else:
                city_iter = city_iter
                print("TO BE NOTED ::: Special Character Here ::::: ", city_iter)

            if(city_iter.strip() == ''):
                city_iter = 'EMPTY_VALUE'
                print("TO BE NOTED ::: EMPTY VALUE FOUND ::::: ", city_iter)

            iter_count += 1
            if(citycounter == 0):
                # print(city_iter)
                city_id = city_iter
                print(city_id)
                citycounter += 1
                # print("continuing...loop")
                continue
            elif(citycounter == 1):
                # print(city_iter)
                city_name = city_iter
                print(city_name)
                citycounter += 1
                # print("continuing...loop")
                continue
            elif(citycounter == 2):
                # print(city_iter)
                city_country = city_iter
                print(city_country)
                # print("checking if...loop")
                row_count += 1

            if(citycounter == 2 and city_id is not None and city_id.strip() != '' and city_name is not None and city_name.strip() != '' and city_country is not None and city_country.strip() != ''):
                print(f"city_id == {city_id} || city_name == {city_name} || city_country == {city_country} || citycounter == {citycounter}")
                cityitem = City(cityID=city_id, cityName=city_name, cityCountry=city_country)
                # print("Again!! cityitem ::: ", cityitem)
                db.session.add(cityitem)
                db.session.commit()
                # print("COMMITTED ::: ", cityitem)
                records_count += 1
                city_id = None
                city_name = None
                city_country = None
                citycounter = 0
                # print(f"city_id == {city_id} || city_name == {city_name} || city_country == {city_country} || citycounter == {citycounter}")
                continue
        print("iter_count ::: ", iter_count)
        print("row_count ::: ", row_count)
        print("records_count ::: ", records_count)
    except:
        print("Exception occured :::: ", sys.exc_info())
    else:
        print("Done!!!")
    finally:
        f.close()
        print("Closed File")

    print("Congratulations!!")


if __name__ == "__main__":
    # db.create_all()
    # populateCity()
    # tryWritingUsingJson()
    populateCityUsingJson()
    