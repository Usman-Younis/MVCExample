from flask import Flask, jsonify, render_template
from telemetry_model import TelemetryModel
import threading
import time

app = Flask(__name__)
telemetry = TelemetryModel()

def telemetry_updater():
    """Continuously generates telemetry data."""
    while True:
        telemetry.generate_telemetry()
        time.sleep(2)  # Simulate sensor reading every 2 seconds

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
