# Lab 2.4: Matplotlib and API
import matplotlib.pyplot as plt
import numpy as np
import requests
import json
from datetime import datetime

# ------------------------------
# Task 1: Plot functions
# ------------------------------

# 1.1 Plot y = log(x)
x = np.linspace(0.1, 10, 100)
y_log = np.log(x)

plt.figure()
plt.plot(x, y_log, 'b-', label='y = ln(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Logarithmic Function')
plt.legend()
plt.grid(True)
plt.show()

# 1.2 Subplots: y = 2sin(x) and y = 2cos(x) + 5
x = np.linspace(0, 2 * np.pi, 100)
y_sin = 2 * np.sin(x)
y_cos = 2 * np.cos(x) + 5

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(x, y_sin, 'r--', label='y = 2sin(x)')
ax1.set_title('Sine')
ax1.legend()
ax1.grid(True)

ax2.plot(x, y_cos, 'g-.', label='y = 2cos(x) + 5')
ax2.set_title('Cosine')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()

# ------------------------------
# Task 2: Weather API and Plots
# ------------------------------

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    
    def get_data(self, location, start_date, end_date):
        try:
            full_url = f"{self.url}/{location}/{start_date}/{end_date}?unitGroup=metric&key={self.api_key}"
            response = requests.get(full_url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print("Error:", e)
            return None
    
    def get_values(self, location, start_date, end_date):
        data = self.get_data(location, start_date, end_date)
        if not data:
            return None
        
        time = []
        temp = []
        humidity = []
        
        for day in data['days']:
            time.append(datetime.strptime(day['datetime'], '%Y-%m-%d'))
            temp.append(day['temp'])
            humidity.append(day['humidity'])
        
        return {'time': time, 'temp': temp, 'humidity': humidity}

class GraphPlotter:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 5))
    
    def plot_lines(self, x, y1, y2, labels, colors):
        self.ax.plot(x, y1, color=colors[0], label=labels[0])
        self.ax.plot(x, y2, color=colors[1], label=labels[1])
        self.ax.set_xlabel('Date')
        self.ax.set_ylabel('Values')
        self.ax.set_title('Weather Data')
        self.ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Example usage (replace 'YOUR_API_KEY' with a real key)
api_key = "TS2XWH8JJLS3T9L8B69M6PEKE"
weather = WeatherAPI(api_key)
data = weather.get_values("Kyiv", "2023-10-01", "2023-10-07")

if data:
    plotter = GraphPlotter()
    plotter.plot_lines(
        data['time'], 
        data['temp'], 
        data['humidity'], 
        labels=['Temperature (°C)', 'Humidity (%)'], 
        colors=['red', 'blue']
    )
else:
    print("Failed to get data.")