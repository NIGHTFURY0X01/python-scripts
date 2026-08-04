"""
# Password Generator

A Python-based secure password generation tool.

## Description

Password Generator creates strong random passwords using a combination
of letters, numbers, and special characters.

Useful for:
- Cybersecurity learning
- Secure account creation
- Password management
- Security automation

## Features

- Generate random passwords
- Custom password length
- Use uppercase letters
- Use lowercase letters
- Use numbers
- Use special characters

## Requirements

- Python 3.x

## Usage

python3 password_generator.py

## Technologies

- Python
- Random module
- String module

## Purpose

Created as part of a Python utilities collection focused on
Cybersecurity, DevOps, and system administration tasks.

"""

import random
import string


def generate_password(length):

    characters = (
        string.ascii_letters
        + string.digits
        + "!@#$%^&*()_+-="
    )

    password = "".join(
        random.choice(characters)
        for _ in range(length)
    )

    return password


def main():

    print("=" * 45)
    print("       PASSWORD GENERATOR")
    print("=" * 45)

    try:

        length = int(
            input(
                "Password length: "
            )
        )

        if length < 4:

            print(
                "Password length should be at least 4"
            )

            return


        password = generate_password(
            length
        )

        print("\nGenerated Password:")
        print(password)


    except ValueError:

        print(
            "Please enter a valid number"
        )


if __name__ == "__main__":
    main()

