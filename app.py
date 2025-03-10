from flask import Flask, jsonify, render_template  # Flask framework for web application
from telemetry_model import TelemetryModel  # Custom model for telemetry data
import threading  # For running the telemetry updater in a separate thread
import time  # For simulating sensor reading intervals

app = Flask(__name__)
telemetry = TelemetryModel()
x = 0

def telemetry_updater():
    """Continuously generates telemetry data."""
    global x  # Declare x as global to modify it inside the function
    while True:
        telemetry.generate_telemetry(x)  # Corrected function call
        time.sleep(2)  # Simulate sensor reading every 2 seconds
        x += 10

@app.route('/')
def dashboard():
    """Renders the telemetry dashboard."""
    return render_template('dashboard.html')

@app.route('/data')
def get_data():
    """Provides telemetry data as JSON."""
    return jsonify(telemetry.get_telemetry())

if __name__ == '__main__':
    threading.Thread(target=telemetry_updater, daemon=True).start()
    app.run(debug=True)
