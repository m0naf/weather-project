from weather_disaster import Storm, Flood, Heatwave, Blizzard
from alert import Alert
from tests import storm_scenario, flood_scenario, heatwave_scenario, blizzard_scenario, safe_scenario

def process_scenario(location, weather_data):
    disasters = [Storm(), Flood(), Heatwave(), Blizzard()]
    alert_system = Alert()
    print(f"\nLocation: {location}")
    any_risk = False
    for d in disasters:
        if d.evaluate_risk(weather_data):
            alert_system.send_alert(d)
            any_risk = True

    if not any_risk:
        print("No disasters detected. Conditions are safe.\n")


def main():
    scenarios = [
        storm_scenario(),
        flood_scenario(),
        heatwave_scenario(),
        blizzard_scenario(),
        safe_scenario()
    ]

    for location, weather in scenarios:
        process_scenario(location, weather)

if __name__ == "__main__":
    main()