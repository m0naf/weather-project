from weather_data import WeatherData
from location import Location

def storm_scenario():
    location = Location("Gdansk", "Poland", 54.372158, 18.638306)
    weather = WeatherData(22, 70, 85, 60, 3, 1008)
    return location, weather

def flood_scenario():
    location = Location("Venice", "Italy")
    weather = WeatherData(18, 90, 40, 95, 5, 1001)
    return location, weather

def heatwave_scenario():
    location = Location("Madrid", "Spain")
    weather = WeatherData(42, 20, 10, 0, 0, 1005)
    return location, weather

def blizzard_scenario():
    location = Location("Oslo", "Norway")
    weather = WeatherData(-13, 80, 65, 30, 2, 995)
    return location, weather

def safe_scenario():
    location = Location("Athens", "Greece")
    weather = WeatherData(25, 50, 10, 5, 0, 1015)
    return location, weather