# Weather Forecast Visualization

This Python project fetches weather data for a given city using the OpenWeatherMap API, processes the data to calculate daily average temperatures, and visualizes the forecast for the next week in a line chart.

## Features

- Allows users to input a city name.
- Fetches the current weather data for the city to get its latitude and longitude.
- Uses the latitude and longitude to fetch a 7-day weather forecast.
- Processes the forecast data to calculate the average temperature for each day.
- Displays a line graph showing the average daily temperature for the next week.

## Technologies Used

- **Python 3.x**: The programming language used for the project.
- **requests**: Used for making HTTP requests to the OpenWeatherMap API.
- **matplotlib**: Used for plotting the temperature data.
- **json**: Used for handling and parsing JSON data.
- **datetime**: For working with date and time information.

## Prerequisites

Before running the project, you need to install the following dependencies:

- Python 3.x
- `requests` library
- `matplotlib` library

To install the required libraries, run:

```bash
pip install requests matplotlib

```
Get an API key from OpenWeatherMap:

1.Go to OpenWeatherMap API and create an account to obtain your free API key.
2.Save your API key:

3.Store your API key in a separate Python file (e.g., ApiDatabase.py) or replace the placeholder in the code with your key directly.
4.Run the program:
```bash
python weather_forecast.py
```
5.Input city name:
The program will prompt you to enter the name of the city you want the weather forecast for.
