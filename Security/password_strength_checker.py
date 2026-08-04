"""
# Password Strength Checker

A Python-based password security analysis tool.

## Description

Password Strength Checker analyzes passwords and evaluates
their security level based on common security rules.

Useful for:
- Cybersecurity learning
- Security awareness
- Password auditing
- Secure development practices

## Features

- Check password length
- Detect uppercase letters
- Detect lowercase letters
- Detect numbers
- Detect special characters
- Calculate security score

## Requirements

- Python 3.x

## Usage

python3 password_strength_checker.py

## Technologies

- Python
- Regular Expressions

## Purpose

Created as part of a Python utilities collection focused on
Cybersecurity, DevOps, and system administration tasks.

"""

import re


def check_password(password):

    score = 0

    checks = {
        "Length (8+)": len(password) >= 8,
        "Uppercase": bool(re.search(r"[A-Z]", password)),
        "Lowercase": bool(re.search(r"[a-z]", password)),
        "Numbers": bool(re.search(r"[0-9]", password)),
        "Special Characters": bool(
            re.search(r"[@$!%*?&]", password)
        )
    }


    print("\nPassword Analysis")
    print("-" * 35)


    for name, result in checks.items():

        status = "PASS" if result else "FAIL"

        print(
            f"{name:<25}: {status}"
        )

        if result:
            score += 1


    print("-" * 35)

    print(
        f"Security Score: {score}/5"
    )


    if score <= 2:
        print("Strength: Weak")

    elif score <= 4:
        print("Strength: Medium")

    else:
        print("Strength: Strong")



def main():

    print("=" * 45)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 45)


    password = input(
        "Enter password: "
    )


    check_password(
        password
    )


if __name__ == "__main__":
    main()