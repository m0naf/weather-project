class WeatherData:
    def __init__(self, temperature, humidity, wind_speed, 
                rain_chance, rain_intensity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.rain_chance = rain_chance
        self.rain_intensity = rain_intensity
        self.pressure = pressure

    def update_data(self, temperature, humidity, wind_speed,
                    rain_chance, rain_intensity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.rain_chance = rain_chance
        self.rain_intensity = rain_intensity
        self.pressure = pressure