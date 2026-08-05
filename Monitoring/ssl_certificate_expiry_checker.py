"""
# SSL Certificate Expiry Checker

A Python-based SSL certificate monitoring tool.

## Description

SSL Certificate Expiry Checker retrieves the SSL certificate
from a remote server and displays its expiration date along
with the number of days remaining.

Useful for:
- DevOps monitoring
- Website administration
- Certificate management
- Infrastructure monitoring

## Features

- Check SSL certificate expiration
- Display expiration date
- Calculate remaining days
- Warn about expiring certificates

## Requirements

- Python 3.x

## Usage

python3 ssl_certificate_expiry_checker.py

## Technologies

- Python
- socket
- ssl
- datetime

## Purpose

Created as part of a Python utilities collection focused on
monitoring, DevOps, and system administration.

"""

import socket
import ssl
from datetime import datetime


def check_certificate(hostname):

    try:

        context = ssl.create_default_context()

        with socket.create_connection(
            (hostname, 443),
            timeout=10
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=hostname
            ) as secure_socket:

                certificate = (
                    secure_socket.getpeercert()
                )

        expiry = datetime.strptime(
            certificate["notAfter"],
            "%b %d %H:%M:%S %Y %Z"
        )

        remaining_days = (
            expiry - datetime.utcnow()
        ).days

        print("=" * 55)
        print("     SSL CERTIFICATE EXPIRY CHECKER")
        print("=" * 55)

        print(f"Host            : {hostname}")
        print(f"Expires On      : {expiry}")
        print(f"Days Remaining  : {remaining_days}")

        if remaining_days > 30:

            print("Certificate     : VALID")

        elif remaining_days > 7:

            print("Certificate     : EXPIRING SOON")

        else:

            print("Certificate     : CRITICAL")


    except Exception as error:

        print(f"\nError: {error}")


def main():

    print("=" * 55)
    print("     SSL CERTIFICATE EXPIRY CHECKER")
    print("=" * 55)

    hostname = input(
        "Domain: "
    ).strip()

    check_certificate(
        hostname
    )


if __name__ == "__main__":
    main()

