"""
# Network Interface Info Tool

A Python-based utility that displays detailed information about network
interfaces available on the system.

## Description

Network Interface Info collects information about network adapters,
IP addresses, MAC addresses, link status, and connection speed.

Useful for:
- DevOps diagnostics
- Network troubleshooting
- System administration
- Infrastructure monitoring

## Features

- List network interfaces
- Display IPv4 addresses
- Display IPv6 addresses
- Display MAC addresses
- Show interface status
- Show link speed

## Requirements

- Python 3.x
- psutil

Install dependency:

pip3 install psutil

## Usage

python3 network_interface_info.py

## Technologies

- Python
- psutil
- Network interface APIs

## Purpose

Created as part of a Python utilities collection focused on networking,
system administration, and DevOps automation tasks.

"""

import psutil
import socket


def get_interfaces():

    interfaces = psutil.net_if_addrs()
    stats = psutil.net_if_stats()

    print("=" * 40)
    print("       NETWORK INTERFACE INFO")
    print("=" * 40)

    for name, addresses in interfaces.items():

        print(f"\nInterface: {name}")

        if name in stats:
            status = "UP" if stats[name].isup else "DOWN"
            speed = stats[name].speed

            print(f"Status : {status}")
            print(f"Speed  : {speed} Mbps")

        for address in addresses:

            if address.family == socket.AF_INET:
                print(f"IPv4   : {address.address}")

            elif address.family == socket.AF_INET6:
                print(f"IPv6   : {address.address}")

            elif str(address.family) == "AF_LINK":
                print(f"MAC    : {address.address}")


def main():
    get_interfaces()


if __name__ == "__main__":
    main()