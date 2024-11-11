import requests
from ApiDatabase import getApiKey
import json
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")

def fetch_weather_data(city_name):
    get_city_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={getApiKey()}&units=metric"
    try:
         response = requests.get(get_city_url)
         response.raise_for_status()  #http error checking
         return response.json()
    except requests.exceptions.RequestException as err:
            print(f"Error fetching city data: {err}")
            return None
    

def fetch_forecast_data(lat,lon):
     url_seven_days_forecast  = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={getApiKey()}&units=metric"
     try:
          response = requests.get(url_seven_days_forecast)
          response.raise_for_status() #http error checking
          return response.json()
     except requests.exceptions.RequestException as err:
            print(f"Error fetching forecast data: {err}")
            return None
     

def process_forecast_data(data):
    daily_temps = {}

    for entry in data['list']:
        date = entry['dt_txt'].split()[0]  # get only the date part
        temp = entry['main']['temp']

        if date in daily_temps:
            daily_temps[date].append(temp)
        else:
            daily_temps[date] = [temp]

    
    return {date: sum(temps) / len(temps) for date, temps in daily_temps.items()} # calculate daily average temperatures

def save_to_file(filename, data):
    with open(filename, "w") as file:
        file.write(json.dumps(data, indent=4))

def load_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)
    
def plot_temperature(daily_avg_temps,city_name):
    dates = list(daily_avg_temps.keys())
    temperatures = list(daily_avg_temps.values())

    plt.figure(figsize=(12, 10))
    plt.plot(dates, temperatures, marker='o')
    plt.title(f"Average Daily Temperature Forecast: " + str(city_name).capitalize())
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid()
    plt.savefig("temperature_forecast.png")


def main():
    city_name = input("Enter City Name: ") #get user input

    city_data = fetch_weather_data(city_name) #try get the weather info for that city
    if city_data is None:
        print("City not found or error occurred. exit program.")
        return

    city_lat = city_data["coord"]["lat"] #assign lat
    city_lon = city_data["coord"]["lon"] #assign lon

    
    forecast_data = fetch_forecast_data(city_lat, city_lon) # try get 7-day forecast data
    if forecast_data is None:
        print("Forecast data could not be retrieved. exit program.")
        return

    file_name = "forecastFile.json"
    save_to_file(file_name, forecast_data) #save as an example

    data = load_from_file(file_name)       #load the saved file

    daily_avg_temps = process_forecast_data(data) #process the data to plot the points on graph - you can plot them directly wihout saving to .json file

    plot_temperature(daily_avg_temps,city_name) #plot the points and save to a .png file

    
if __name__ == "__main__":
     main()
