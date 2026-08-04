"""
# Currency API Client

A Python-based currency conversion tool.

## Description

Currency API Client retrieves exchange rates and converts
between different currencies.

## Features

- Convert currencies
- Get exchange rates
- Support multiple currency codes
- Parse JSON API responses

## Requirements

- Python 3.x
- requests

## Usage

python3 currency_api.py

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


def convert_currency(
    amount,
    from_currency,
    to_currency
):

    url = (
        "https://api.frankfurter.app/latest"
    )

    params = {
        "amount": amount,
        "from": from_currency,
        "to": to_currency
    }


    try:

        response = requests.get(
            url,
            params=params
        )


        if response.status_code != 200:

            print(
                "API Error"
            )

            return


        data = response.json()


        result = data["rates"][to_currency]


        print("=" * 45)
        print("       CURRENCY CONVERTER")
        print("=" * 45)


        print(
            f"Amount : {amount} {from_currency}"
        )

        print(
            f"Result : {result} {to_currency}"
        )

        print(
            f"Rate   : {data['rates']}"
        )


    except requests.RequestException:

        print(
            "Connection error"
        )



def main():

    print("=" * 45)
    print("          CURRENCY API")
    print("=" * 45)


    amount = float(
        input(
            "Amount: "
        )
    )


    from_currency = input(
        "From currency (USD/EUR): "
    ).upper()


    to_currency = input(
        "To currency (EUR/USD): "
    ).upper()


    convert_currency(
        amount,
        from_currency,
        to_currency
    )



if __name__ == "__main__":
    main()