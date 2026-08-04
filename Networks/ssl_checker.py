"""
# SSL Certificate Checker

A Python-based SSL certificate monitoring tool.

## Description

SSL Certificate Checker retrieves information about a website's TLS/SSL
certificate and checks its expiration date.

This tool is useful for:
- DevOps monitoring
- Server maintenance
- Certificate expiration checks
- Website security auditing

## Features

- Connect to HTTPS websites
- Retrieve SSL certificate information
- Display certificate issuer
- Show expiration date
- Calculate remaining validity days

## Requirements

- Python 3.x

## Usage

python3 ssl_checker.py

## Technologies

- Python
- SSL module
- Socket programming

## Purpose

Created as part of a Python utilities collection focused on networking,
system administration, and DevOps automation tasks.

"""

import ssl
import socket
from datetime import datetime


def get_ssl_certificate(domain):

    context = ssl.create_default_context()

    try:
        with socket.create_connection(
            (domain, 443),
            timeout=5
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=domain
            ) as ssock:

                return ssock.getpeercert()

    except Exception:
        return None


def main():

    print("=" * 35)
    print("       SSL CERTIFICATE CHECKER")
    print("=" * 35)

    domain = input("Enter domain: ")

    certificate = get_ssl_certificate(domain)

    if not certificate:
        print("\nSSL certificate not found")
        return

    issuer = dict(
        item[0]
        for item in certificate["issuer"]
    )

    expire_date = datetime.strptime(
        certificate["notAfter"],
        "%b %d %H:%M:%S %Y %Z"
    )

    remaining_days = (
        expire_date - datetime.utcnow()
    ).days


    print("\nCertificate Information")
    print("-" * 35)

    print(f"Domain  : {domain}")
    print(f"Issuer  : {issuer.get('organizationName')}")
    print(f"Expires : {expire_date}")
    print(f"Days Left : {remaining_days} days")


if __name__ == "__main__":
    main()