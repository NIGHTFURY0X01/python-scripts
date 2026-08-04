"""
# GitHub API Client

A Python-based GitHub API client.

## Description

GitHub API Client retrieves public GitHub user information
using GitHub REST API.

## Features

- Get GitHub user information
- Display username
- Show public repositories count
- Show followers
- Show following
- Display profile URL

## Requirements

- Python 3.x
- requests

## Usage

python3 github_api_client.py

## Technologies

- Python
- Requests
- REST API
- JSON

## Purpose

Created as part of a Python utilities collection focused on
API integration, DevOps, and automation.

"""

import requests


def get_github_user(username):

    url = f"https://api.github.com/users/{username}"

    try:

        response = requests.get(
            url
        )

        if response.status_code != 200:

            print("User not found")
            return


        data = response.json()


        print("=" * 45)
        print("       GITHUB USER INFO")
        print("=" * 45)


        print(
            f"Username : {data['login']}"
        )

        print(
            f"Name     : {data['name']}"
        )

        print(
            f"Repos    : {data['public_repos']}"
        )

        print(
            f"Followers: {data['followers']}"
        )

        print(
            f"Following: {data['following']}"
        )

        print(
            f"Profile  : {data['html_url']}"
        )


    except requests.RequestException:

        print(
            "API connection error"
        )



def main():

    print("=" * 45)
    print("       GITHUB API CLIENT")
    print("=" * 45)


    username = input(
        "GitHub username: "
    )


    get_github_user(
        username
    )


if __name__ == "__main__":
    main()