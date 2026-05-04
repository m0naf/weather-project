from enum import Enum

class Disaster:
    def __init__(self, name):
        self.name = name
        self.severity_level = None
    def evaluate_risk(self, weather_data):
        print("Each disaster must implements it's own logic")

class SeverityLevel(Enum):
    Light = 0
    Medium = 1
    High = 2
    Critical = 3

class Storm(Disaster):
    def __init__(self):
        super().__init__("Storm")
    def evaluate_risk(self, weather_data):
        if weather_data.wind_speed >= 100 and weather_data.rain_intensity >= 11.0 :
            self.severity_level = SeverityLevel.Critical
            return True
        if weather_data.wind_speed >= 75 and weather_data.rain_intensity >= 7.0 :
            self.severity_level = SeverityLevel.High
            return True
        if weather_data.wind_speed >= 50 and weather_data.rain_intensity >= 3.0 :
            self.severity_level = SeverityLevel.Medium
            return True
        return False

class Flood(Disaster):
    def __init__(self):
        super().__init__('Flood')
    def evaluate_risk(self, weather_data):
        if weather_data.rain_intensity >= 40.0 :
            self.severity_level = SeverityLevel.Critical
            return True
        if weather_data.rain_intensity >= 15.0 :
            self.severity_level = SeverityLevel.High
            return True
        return False
    
class Heatwave(Disaster):
    def __init__(self):
        super().__init__('Heatwave')
    def evaluate_risk(self, weather_data):
        if weather_data.temperature > 40 :
            self.severity_level = SeverityLevel.High
            return True
        if weather_data.temperature > 32 :
            self.severity_level = SeverityLevel.Medium
            return True
        return False

class Blizzard(Disaster):
    def __init__(self):
        super().__init__('Blizzard')
    def evaluate_risk(self, weather_data):
        if weather_data.temperature < -11 :
            self.severity_level = SeverityLevel.Medium
            return True
        if weather_data.temperature < -5 :
            self.severity_level = SeverityLevel.Light
            return True
        return False