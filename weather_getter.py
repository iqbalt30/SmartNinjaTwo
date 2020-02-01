import pyowm as pm
import sys


def display_weather(location):
    key = input('Enter Your OpenWeatherAPI Key: ')
    owm = pm.OWM(key)

    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    print(w.get_temperature('celsius'))


if __name__ == "__main__":
    keyword = sys.argv[1]
    display_weather(keyword)