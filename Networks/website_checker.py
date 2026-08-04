"""
# Website Status Checker

A Python-based web monitoring utility that checks website availability.

## Description

Website Status Checker is a lightweight DevOps tool that monitors the
availability of websites by sending HTTP requests and analyzing responses.

It can be useful for:
- Website uptime monitoring
- DevOps health checks
- Network troubleshooting
- Service availability testing

## Features

- Check website availability
- Display HTTP status code
- Measure response time
- Detect connection failures
- Support HTTP and HTTPS URLs

## Requirements

- Python 3.x
- requests library

Install dependency:

pip3 install requests

## Usage

python3 website_checker.py

## Technologies

- Python
- Requests
- HTTP protocol

## Purpose

Created as part of a Python utilities collection focused on networking,
system administration, and DevOps automation tasks.

"""

import time
import requests


def check_website(url):
    try:
        start_time = time.time()

        response = requests.get(
            url,
            timeout=5
        )

        end_time = time.time()

        response_time = round(
            (end_time - start_time) * 1000,
            2
        )

        return {
            "status": "UP",
            "code": response.status_code,
            "time": response_time
        }

    except requests.exceptions.RequestException:
        return {
            "status": "DOWN",
            "code": None,
            "time": None
        }


def main():

    print("=" * 35)
    print("       WEBSITE STATUS CHECKER")
    print("=" * 35)

    url = input("Enter URL: ")

    if not url.startswith("http"):
        url = "https://" + url

    result = check_website(url)

    print("\nResult")
    print("-" * 35)

    print(f"Status : {result['status']}")
    print(f"URL    : {url}")
    print(f"Code   : {result['code']}")

    if result["time"]:
        print(f"Time   : {result['time']} ms")


if __name__ == "__main__":
    main()