from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os, sys, json, WeatherModel as wmdl
from WeatherCommons import DEBUG_MODE


initial = True
file_path = os.path.abspath(os.getcwd())+"\database.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+file_path
# db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


@app.route("/")
@app.route("/index")
def hello():
    return render_template('index.html')


@app.route("/adduser", methods=['GET', 'POST'])
def adduser():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        useritem = User(username=name, email=email)
        try:
            db.session.add(useritem)
            db.session.commit()
            users = User.query.all()
        except:
            if('sqlalchemy.exc.IntegrityError' in sys.exc_info):
                return render_template('adduser.html', name=name, email=email, msg='ALREADYADDED', users=users)
            else:
                return render_template('adduser.html', name=name, email=email, msg='FAILED', users=users)
        return render_template('adduser.html', name=useritem.username, email=useritem.email, msg='SUCCESS', users=users)
    else:
        users = User.query.all()
        return render_template('adduser.html', name='<Username>', email='<default@email.com>', msg='',  users=users)


@app.route("/users")
def api_call():
    users = User.query.all()
    usersjson = {}
    userslist = []
    for user in users:
        userslist.append({'username':user.username, 'email':user.email})
    print(userslist)
    usersjson={'USERS':userslist}
    print(usersjson)

    return json.dumps(usersjson)


@app.route("/login")
def hello_login():
    return render_template('login.html')


@app.route("/about")
def hello_about():
    return render_template('about.html')


@app.route("/contact")
def hello_contact():
    return render_template('contact.html')


@app.route("/weatherbase")
def weatherbase():
    return render_template('weatherbase.html')


@app.route("/weatherForecastApp")
def weatherForecastApp():
    return render_template('WeatherForecastApp.html')


@app.route("/weatherOptions")
def getWeatherOptions():
    return render_template('WeatherQueryOptions.html')


@app.route("/weathersearchcityname", methods=['GET', 'POST'])
def weathersearchcityname():
    if DEBUG_MODE:
        print("In [app.py]:weathersearchcityname()")
        print(f"request.method :: {request.method}")
    cityweather = None
    errormessage = None
    if request.method == 'POST':
        city_name = request.form.get('input_city_name')
        country_code = request.form.get('input_country_code')
        if DEBUG_MODE:
            print(f"city_name :: {city_name}")
            print(f"country_code :: {country_code}")
        cityweather, errormessage = wmdl.getWeatherByCityName(city_name, country_code)
        if DEBUG_MODE:
            print(f"cityweather :: {cityweather}")
            print(f"errormessage :: {errormessage}")
        return render_template('weathersearchcityname.html', cityweather=cityweather, errormessage=errormessage)
        # return render_template('WeatherForecastApp.html', cityweather=cityweather, errormessage=errormessage)

    else:
        if DEBUG_MODE:
            print(f"In else... Redirecting to weathersearchcityname.html")
        return render_template('weathersearchcityname.html')
        # return render_template('WeatherForecastApp.html')



@app.route("/weathersearchcityid", methods=['GET', 'POST'])
def weathersearchcityid():
    if DEBUG_MODE:
        print("In [app.py]:weathersearchcityid()")
        print(f"request.method :: {request.method}")
    cityweather = None
    errormessage = None
    if request.method == 'POST':
        city_id = request.form.get('input_city_id')
        if DEBUG_MODE:
            print(f"city_id :: {city_id}")
        cityweather, errormessage = wmdl.getWeatherByCityID(city_id)
        if DEBUG_MODE:
            print(f"cityweather :: {cityweather}")
            print(f"errormessage :: {errormessage}")
        return render_template('weathersearchcityid.html', cityweather=cityweather, errormessage=errormessage)
    else:
        if DEBUG_MODE:
            print(f"In else... Redirecting to weathersearchcityid.html")
        return render_template('weathersearchcityid.html')


@app.route("/weathersearchgeocoord", methods=['GET', 'POST'])
def weathersearchgeocoord():
    if DEBUG_MODE:
        print("In [app.py]:weathersearchgeocoord()")
        print(f"request.method :: {request.method}")
    cityweather = None
    errormessage = None
    if request.method == 'POST':
        geo_lat = request.form.get('input_latitude')
        geo_lon = request.form.get('input_longitude')
        if DEBUG_MODE:
            print(f"geo_lat :: {geo_lat}")
            print(f"geo_lon :: {geo_lon}")
        cityweather, errormessage = wmdl.getWeatherByGeoCoords(geo_lat, geo_lon)
        if DEBUG_MODE:
            print(f"cityweather :: {cityweather}")
            print(f"errormessage :: {errormessage}")
        return render_template('weathersearchgeocoord.html', cityweather=cityweather, errormessage=errormessage)
    else:
        if DEBUG_MODE:
            print(f"In else... Redirecting to weathersearchgeocoord.html")
        return render_template('weathersearchgeocoord.html')
        

@app.route("/weathersearchzipcode", methods=['GET', 'POST'])
def weathersearchzipcode():
    if DEBUG_MODE:
        print("In [app.py]:weathersearchzipcode()")
        print(f"request.method :: {request.method}")
    cityweather = None
    errormessage = None
    if request.method == 'POST':
        zip_code = request.form.get('input_zip_code')
        country_code = request.form.get('input_country_code')
        if DEBUG_MODE:
            print(f"zip_code :: {zip_code}")
            print(f"country_code :: {country_code}")
        cityweather, errormessage = wmdl.getWeatherByZipCode(zip_code, country_code)
        if DEBUG_MODE:
            print(f"cityweather :: {cityweather}")
            print(f"errormessage :: {errormessage}")
        return render_template('weathersearchzipcode.html', cityweather=cityweather, errormessage=errormessage)
    else:
        if DEBUG_MODE:
            print(f"In else... Redirecting to weathersearchzipcode.html")
        return render_template('weathersearchzipcode.html')


if __name__ == "__main__":
    # if initial == True:
    #     # db.create_all()
    #     # admin = User(username='admin', email='admin@123.com')
    #     # guest = User(username='guest', email='guest@123.com')
    #     # db.session.add(admin)
    #     # db.session.add(guest)
    #     # db.session.commit()
    #     # initial = False
    app.run(debug = True)