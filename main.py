from weather_disaster import Storm, Flood, Heatwave, Blizzard
from location import Location
from alert import Alert
from weather_data import WeatherData
from risks import RiskCalculator

def main():
    file = open("data.txt", "rt")
    datas = file.read().split("\n")
    risks = RiskCalculator()
    alerts = Alert()

    for i in datas:
        data = i.split(",")
        loc = Location(data[0], data[1], float(data[2]), float(data[3]))
        weather = WeatherData(int(data[4]), int(data[5]), int(data[6]), int(data[7]),
                                float(data[8]), int(data[9]))
        loc.set_weather_data(weather)
        disasters = risks.evaluate_risks(loc)
        for d in disasters:
            alerts.send_alert(d)
        alerts.show_alerts()
        alerts.clear_alerts()

    file.close()

if __name__ == "__main__":
    main()