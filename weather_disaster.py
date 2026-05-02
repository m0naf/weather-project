from weather_data import WeatherData

class Disaster:
    def __init__(self, name):
        self.name = name
        self.severity_level = None
    def evaluate_risk(self, weather_data):
        print("Each disaster must implements it's own logic")

class Storm(Disaster):
    def __init__(self):
        super().__init__("Storm")
    def evaluate_risk(self, weather_data):
        if weather_data.wind_speed > 75 and weather_data.rain_intensity >= 3.0 :
            self.severity_level = 'Medium'
            return True
        return False

class Flood(Disaster):
    def __init__(self):
        super().__init__('Flood')
    def evaluate_risk(self, weather_data):
        if weather_data.rain_intensity >= 4.0 :
            self.severity_level = 'Critical'
            return True
        return False
    
class Heatwave(Disaster):
    def __init__(self):
        super().__init__('Heatwave')
    def evaluate_risk(self, weather_data):
        if weather_data.temperature > 32 :
            self.severity_level = 'Medium'
            return True
        return False

class Blizzard(Disaster):
    def __init__(self):
        super().__init__('Blizzard')
    def evaluate_risk(self, weather_data):
        if weather_data.temperature < -9 :
            self.severity_level = 'High'
            return True
        return False