from requests import Request, Session, Response
import os

def get_weather(lat, long, apiKey):
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {
            'lat': lat,
            'lon': long,
            'appid': apiKey
        }
        session = Session()
        request = Request('GET', url, params=params)
        prepped = request.prepare()
        response = session.send(prepped)
        return response.json()
    except Exception as e:
        return e


lat = os.environ['LAT']
long = os.environ['LONG']
apiKey = os.environ['API_KEY']

print(get_weather(lat,long,apiKey))