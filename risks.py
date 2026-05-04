from weather_disaster import Storm, Flood, Heatwave, Blizzard

class RiskCalculator:
    def evaluate_risks(self, location):
        result = []
        if location.weather_data == None:
            return result
        disasters = [Storm(), Flood(), Heatwave(), Blizzard()]
        for d in disasters:
            if d.evaluate_risk(location.weather_data):
                result.append(d)
        return result