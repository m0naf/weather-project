from weather_data import WeatherData
from weather_disaster import *
from location import Location
from risks import RiskCalculator
import unittest



class TestDisasters(unittest.TestCase):
    def test_storm(self):
        location = Location("Gdansk", "Poland", 54.372158, 18.638306)
        location.set_weather_data(WeatherData(22, 70, 85, 60, 3, 1008))
        risks = RiskCalculator()
        result = risks.evaluate_risks(location)
        self.assertTrue(any(isinstance(d, Storm) for d in result))
        
    def test_flood(self):
        location = Location("Venice", "Italy")
        location.set_weather_data(WeatherData(18, 90, 40, 95, 20, 1001))
        risks = RiskCalculator()
        result = risks.evaluate_risks(location)
        self.assertTrue(any(isinstance(d, Flood) for d in result))

    def test_heatwave(self):
        location = Location("Madrid", "Spain")
        location.set_weather_data(WeatherData(42, 20, 10, 0, 0, 1005))
        risks = RiskCalculator()
        result = risks.evaluate_risks(location)
        for d in result:
            self.assertTrue(isinstance(d, Heatwave))

    def test_blizzard(self):
        location = Location("Oslo", "Norway")
        location.set_weather_data(WeatherData(-13, 80, 65, 30, 2, 995))
        risks = RiskCalculator()
        result = risks.evaluate_risks(location)
        for d in result:
            self.assertTrue(isinstance(d, Blizzard))

    def test_safe(self):
        location = Location("Athens", "Greece")
        location.set_weather_data(WeatherData(25, 50, 10, 5, 0, 1015))
        risks = RiskCalculator()
        result = risks.evaluate_risks(location)
        self.assertTrue(len(result) == 0)

    def test_severity_storm(self):
        disaster = Storm()

        disaster.evaluate_risk(WeatherData(22, 70, 101, 60, 11, 1008))
        self.assertEqual(disaster.severity_level, SeverityLevel.Critical)

        disaster.evaluate_risk(WeatherData(22, 70, 76, 60, 7, 1008))
        self.assertEqual(disaster.severity_level, SeverityLevel.High)

        disaster.evaluate_risk(WeatherData(22, 70, 51, 60, 3, 1008))
        self.assertEqual(disaster.severity_level, SeverityLevel.Medium)

    def test_severity_flood(self):
        disaster = Flood()

        disaster.evaluate_risk(WeatherData(18, 90, 40, 95, 41, 1001))
        self.assertEqual(disaster.severity_level, SeverityLevel.Critical)

        disaster.evaluate_risk(WeatherData(18, 90, 40, 95, 16, 1001))
        self.assertEqual(disaster.severity_level, SeverityLevel.High)
    
    def test_severity_heatwave(self):
        disaster = Heatwave()

        disaster.evaluate_risk(WeatherData(41, 20, 10, 0, 0, 1005))
        self.assertEqual(disaster.severity_level, SeverityLevel.High)

        disaster.evaluate_risk(WeatherData(33, 20, 10, 0, 0, 1005))
        self.assertEqual(disaster.severity_level, SeverityLevel.Medium)
    
    def test_severity_blizzard(self):
        disaster = Blizzard()

        disaster.evaluate_risk(WeatherData(-13, 80, 65, 30, 2, 995))
        self.assertEqual(disaster.severity_level, SeverityLevel.Medium)

        disaster.evaluate_risk(WeatherData(-6, 80, 65, 30, 2, 995))
        self.assertEqual(disaster.severity_level, SeverityLevel.Light)
    
    def test_simultaneous_disasters(self):
        location = Location("Tallin", "Estonia")
        risks = RiskCalculator()

        # Storm and Flood
        location.set_weather_data(WeatherData(0, 0, 101, 0, 40, 0))
        result = risks.evaluate_risks(location)
        self.assertTrue(any(isinstance(d, Storm) for d in result))
        self.assertTrue(any(isinstance(d, Flood) for d in result))

        # Flood and Blizzard
        location.set_weather_data(WeatherData(-10, 0, 0, 0, 40, 0))
        result = risks.evaluate_risks(location)
        self.assertTrue(any(isinstance(d, Flood) for d in result))
        self.assertTrue(any(isinstance(d, Blizzard) for d in result))

        # Storm and Blizzard
        location.set_weather_data(WeatherData(-10, 0, 101, 0, 10, 0))
        result = risks.evaluate_risks(location)
        self.assertTrue(any(isinstance(d, Storm) for d in result))
        self.assertTrue(any(isinstance(d, Blizzard) for d in result))

        # Storm and Heatwave
        location.set_weather_data(WeatherData(35, 0, 101, 0, 10, 0))
        result = risks.evaluate_risks(location)
        self.assertTrue(any(isinstance(d, Storm) for d in result))
        self.assertTrue(any(isinstance(d, Heatwave) for d in result))

        # Flood and Heatwave
        location.set_weather_data(WeatherData(35, 0, 0, 0, 40, 0))
        result = risks.evaluate_risks(location)
        self.assertTrue(any(isinstance(d, Flood) for d in result))
        self.assertTrue(any(isinstance(d, Heatwave) for d in result))

        # Storm, Flood and Blizzard
        location.set_weather_data(WeatherData(-10, 0, 50, 0, 40, 0))
        result = risks.evaluate_risks(location)
        self.assertTrue(any(isinstance(d, Flood) for d in result))
        self.assertTrue(any(isinstance(d, Blizzard) for d in result))
    
if __name__ == '__main__':
    unittest.main()