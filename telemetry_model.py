import random
import time

class TelemetryModel:
    def __init__(self):
        self.data = []

    def generate_telemetry(self):
        """Simulate sensor data collection."""
        timestamp = time.strftime("%H:%M:%S")
        value = round(random.uniform(20, 100), 2)  # Simulated sensor reading
        self.data.append({"timestamp": timestamp, "value": value})
        if len(self.data) > 10:  # Store only last 10 readings
            self.data.pop(0)

    def get_telemetry(self):
        """Return the latest telemetry data."""
        return self.data
