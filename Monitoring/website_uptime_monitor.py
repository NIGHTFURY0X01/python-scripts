"""
# Website Uptime Monitor

A Python-based website monitoring tool.

## Description

Website Uptime Monitor checks whether a website is online,
measures response time, and displays the HTTP status code.

Useful for:
- DevOps monitoring
- Website availability checks
- Infrastructure monitoring
- Server health verification

## Features

- Check website availability
- Display HTTP status code
- Measure response time
- Handle connection errors

## Requirements

- Python 3.x
- requests

## Usage

python3 website_uptime_monitor.py

## Technologies

- Python
- Requests
- HTTP
- REST

## Purpose

Created as part of a Python utilities collection focused on
monitoring, DevOps, and system administration.

"""

import requests
import time


def check_website(url):

    try:

        start_time = time.perf_counter()

        response = requests.get(
            url,
            timeout=10
        )

        end_time = time.perf_counter()

        response_time = (
            end_time - start_time
        ) * 1000


        print("=" * 50)
        print("        WEBSITE UPTIME MONITOR")
        print("=" * 50)

        print(
            f"Website      : {url}"
        )

        print(
            f"Status Code  : {response.status_code}"
        )

        print(
            f"Response Time: {response_time:.2f} ms"
        )


        if response.status_code == 200:

            print(
                "Status       : ONLINE"
            )

        else:

            print(
                "Status       : ERROR"
            )


    except requests.exceptions.ConnectionError:

        print(
            "\nConnection failed."
        )

    except requests.exceptions.Timeout:

        print(
            "\nRequest timed out."
        )

    except requests.RequestException as error:

        print(
            f"\nError: {error}"
        )


def main():

    print("=" * 50)
    print("        WEBSITE UPTIME MONITOR")
    print("=" * 50)

    url = input(
        "Website URL: "
    )

    check_website(
        url
    )


if __name__ == "__main__":
    main()