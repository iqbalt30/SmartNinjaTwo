import pyowm as pm
import sys


class Weather:
    def __init__(self, temperature, wind, humidity):
        self.temperature = temperature
        self.wind = wind
        self.humidity = humidity

    def print_data(self):
        return "Temperature in Celsius: {}, " \
               "Wind speed and direction: {}, " \
               "Humidity in percent: {}" \
            .format(self.temperature, self.wind, self.humidity)


def display_weather(location):
    key = input('Enter Your OpenWeatherAPI Key: ')
    owm = pm.OWM(key)

    observation = owm.weather_at_place(location)
    w = observation.get_weather()

    weather_instance = Weather(w.get_temperature('celsius'), w.get_wind(), w.get_humidity())
    print(weather_instance.print_data())


if __name__ == "__main__":
    keyword = sys.argv[1]
    display_weather(keyword)
