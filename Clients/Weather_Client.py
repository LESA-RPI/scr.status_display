from pyowm import OWM
from pytz import timezone, utc
from Client_util import *
    
def data_organizer(raw_api_dict):
    data = dict(
        temp=raw_api_dict.get_temperature('fahrenheit')['temp'],
        pressure=raw_api_dict.get_pressure()['press'],
        humidity=raw_api_dict.get_humidity(),
        sunrise=time_converter(raw_api_dict.get_sunrise_time('date')),
        sunset=time_converter(raw_api_dict.get_sunset_time('date')),
        status=raw_api_dict.get_detailed_status(),
        icon=raw_api_dict.get_weather_icon_name()
    )
    return data
        
def time_converter(TT):
    T = TT.replace(tzinfo = utc)
    T = T.astimezone(timezone('America/New_York'))
    converted_time = T.strftime('%H:%M:%S')
    return converted_time

if __name__ == "__main__":
    while True:
        owm = OWM('f38bad7ebd2079684d1bbe9fce79b11a')
	try:
        	obs = owm.weather_at_coords(42.729173,-73.677731)
        	w = obs.get_weather()
        	post_request('Status_Weather', { "temp":     data_organizer(w)['temp'],
                                         "pressure": data_organizer(w)['pressure'],
                                         "humidity": data_organizer(w)['humidity'],
                                         "sunset":   data_organizer(w)['sunset'],
                                         "sunrise":  data_organizer(w)['sunrise'],
                                         "icon":     data_organizer(w)['icon']})    
        except:
		print "error reading weather information"
	time.sleep(1)
