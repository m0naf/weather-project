from weather_disaster import Storm, Flood, Heatwave, Blizzard
class Alert:
    def __init__(self):
        self.active_alerts = []

    def show_alerts(self):
        for alert in self.active_alerts:
            print(alert) 

    def send_alert(self, disaster):
        alert_message = f"ALERT: {disaster.name} is detected. Severity: {disaster.severity_level}"
        self.active_alerts.append(alert_message)
    
    def clear_alerts(self):
        self.active_alerts.clear()