"""
# Weather API Client

A Python-based weather information client.

## Description

Weather API Client retrieves current weather information
using OpenWeather API.

## Features

- Get current weather
- Display temperature
- Show humidity
- Display weather condition
- Show wind speed
- API integration

## Requirements

- Python 3.x
- requests
- OpenWeather API Key

## Usage

python3 weather_api.py

## Technologies

- Python
- Requests
- REST API
- JSON

## Purpose

Created as part of a Python utilities collection focused on
API integration, automation, and DevOps skills.

"""

import requests


API_KEY = "YOUR_API_KEY"


def get_weather(city):

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
    )

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }


    try:

        response = requests.get(
            url,
            params=params
        )


        if response.status_code != 200:

            print(
                "City not found or API error"
            )

            return


        data = response.json()


        print("=" * 45)
        print("          WEATHER INFO")
        print("=" * 45)


        print(
            f"City       : {data['name']}"
        )

        print(
            f"Country    : {data['sys']['country']}"
        )

        print(
            f"Temperature: {data['main']['temp']} °C"
        )

        print(
            f"Humidity   : {data['main']['humidity']}%"
        )

        print(
            f"Condition  : {data['weather'][0]['description']}"
        )

        print(
            f"Wind Speed : {data['wind']['speed']} m/s"
        )


    except requests.RequestException:

        print(
            "Connection error"
        )



def main():

    print("=" * 45)
    print("          WEATHER API")
    print("=" * 45)


    city = input(
        "City name: "
    )


    get_weather(
        city
    )


if __name__ == "__main__":
    main()
