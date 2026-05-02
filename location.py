class Location:
    def __init__(self, city, country, latitude = None, longtitude = None):
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longtitude = longtitude
        self.weather_data = None

    def __str__(self):
        return f"{self.city}, {self.country}"
    
    def set_weather_data(self, weather_data):
        self.weather_data = weather_data

    def get_weather_data(self):
        return self.weather_data