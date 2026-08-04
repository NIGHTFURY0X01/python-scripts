"""
# DNS Lookup Tool

A Python-based DNS utility that retrieves domain information.

## Description

DNS Lookup Tool is a lightweight networking utility designed to resolve
domain names and display DNS-related information.

It can be useful for:
- Network troubleshooting
- DNS verification
- DevOps diagnostics
- Domain connectivity checks

## Features

- Resolve domain to IPv4 address
- Display hostname information
- Show DNS resolver information
- Support domain lookup

## Requirements

- Python 3.x

## Usage

python3 dns_lookup.py

## Technologies

- Python
- Socket programming

## Purpose

Created as part of a Python utilities collection focused on networking,
system administration, and DevOps automation tasks.

"""

import socket


def dns_lookup(domain):
    try:
        hostname = socket.gethostbyname_ex(domain)

        return {
            "hostname": hostname[0],
            "aliases": hostname[1],
            "ip_addresses": hostname[2]
        }

    except socket.gaierror:
        return None


def main():

    print("=" * 35)
    print("          DNS LOOKUP")
    print("=" * 35)

    domain = input("Enter domain: ")

    result = dns_lookup(domain)

    if result:

        print("\nDNS Information")
        print("-" * 35)

        print(f"Hostname : {result['hostname']}")

        if result["aliases"]:
            print(f"Aliases  : {result['aliases']}")

        print("IP Addresses:")

        for ip in result["ip_addresses"]:
            print(f" - {ip}")

    else:
        print("\nDomain could not be resolved")


if __name__ == "__main__":
    main()