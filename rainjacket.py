import requests
from datetime import datetime, timedelta

def check_weather():
    # enter your OpenWeatherMap API key here
    api_key = "YOUR_API_KEY_HERE"

    # set the location to Charlotte, NC
    location = "Charlotte,US"

    # call the OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    # check if it's currently raining
    current_weather = data["list"][0]["weather"][0]["main"].lower()
    if current_weather == "rain":
        print("It's currently raining.  You should bring a rain jacket!")
    else:
        # check if it's going to rain later in the day
        for forecast in data["list"]:
            forecast_time = datetime.fromtimestamp(forecast["dt"])
            if forecast_time.date() > datetime.now().date():
                # Check if it's going to rain within the next 10 hours
                if forecast_time <= datetime.now() + timedelta(hours=10) and forecast["weather"][0]["main"].lower() == "rain":
                    print("It's going to rain later today.  You should bring a rain jacket!")
                    return
        print("It's not going to rain today.  You don't need to bring a rain jacket.")
