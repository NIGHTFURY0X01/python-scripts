"""
# Random Quote API

A Python-based random quote generator.

## Description

Random Quote API retrieves random inspirational quotes
from an online API.

## Features

- Get random quotes
- Display author information
- API integration
- JSON response handling

## Requirements

- Python 3.x
- requests

## Usage

python3 random_quote_api.py

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


def get_random_quote():

    url = "https://api.quotable.io/random"


    try:

        response = requests.get(
            url
        )


        if response.status_code != 200:

            print(
                "API Error"
            )

            return


        data = response.json()


        print("=" * 45)
        print("          RANDOM QUOTE")
        print("=" * 45)


        print(
            "\nQuote:"
        )

        print(
            data["content"]
        )


        print(
            "\nAuthor:"
        )

        print(
            data["author"]
        )


    except requests.RequestException:

        print(
            "Connection error"
        )



def main():

    print("=" * 45)
    print("       RANDOM QUOTE API")
    print("=" * 45)


    get_random_quote()



if __name__ == "__main__":
    main()