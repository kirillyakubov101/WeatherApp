import requests
from  ApiDatabase import getApiKey
import json
import datetime
import matplotlib.pyplot as plt

user_input = input("Enter City Name: ")
get_city_url = f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={getApiKey()}&units=metric"
req = requests.get(get_city_url).json()
city_lat = (req["coord"]["lat"])
city_lon = (req["coord"]["lon"])

url_seven_days_forecast = f"https://api.openweathermap.org/data/2.5/forecast?lat={city_lat}&lon={city_lon}&appid={getApiKey()}&units=metric"
req = requests.get(url_seven_days_forecast).json()
fileName = "forecastFile.json"
# Save the response to JSON file
fileName = "forecastFile.json"

with open(fileName, "w") as file:
    file.write(json.dumps(req, indent=4))

# Read data from JSON file
with open(fileName, 'r') as file:
    data = json.load(file)

# Parse and organize data by date
daily_temps = {}

for entry in data['list']:
    # Get date and temperature
    date = entry['dt_txt'].split()[0]  # Extract only the date part
    temp = entry['main']['temp']

    # Accumulate temps by date
    if date in daily_temps:
        daily_temps[date].append(temp)
    else:
        daily_temps[date] = [temp]

# Calculate daily average temperatures
avg_daily_temps = {date: sum(temps) / len(temps) for date, temps in daily_temps.items()}

# Plotting
dates = list(avg_daily_temps.keys())
temperatures = list(avg_daily_temps.values())

plt.figure(figsize=(10, 5))
plt.plot(dates, temperatures, marker='o')
plt.title(f"Average Daily Temperature Forecast")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid()
plt.show()
