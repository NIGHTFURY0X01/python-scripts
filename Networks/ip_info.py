"""
# IP Information Tool

A Python script that collects and displays basic system and network information.

## Description

IP Information Tool is a lightweight Python utility designed to inspect the current machine's network configuration.

It provides useful information for system administration and DevOps tasks, including network interfaces, IP addresses, and system details.

## Features

- Get hostname
- Display operating system information
- Display Python version
- Get MAC address
- Detect active network interfaces
- Display IPv4 addresses
- Display network interface status
- Identify VPN interfaces (such as utun on macOS)

## Requirements

- Python 3.x
- psutil

Install dependency:

pip3 install psutil


## Usage

Run the script:

python3 ip_info.py


## Example Output

===================================
          IP INFORMATION
===================================

Hostname : Your-device
OS       : Darwin 25.5.0
Python   : 3.14.2
Local IP : 10.111.2.2
MAC      : xx:xx:xx:xx:xx:xx


===================================
       NETWORK INTERFACES
===================================

Interface: en0
  IPv4 : 172.20.10.4

Interface: utun4
  IPv4 : 10.111.2.2


## Technologies

- Python
- Socket
- psutil
- Network Interface APIs


## Purpose

Created as part of a Python utilities collection focused on networking,
system administration, and DevOps automation tasks.

"""

import socket
import platform
import uuid
import psutil


def get_hostname():
    return socket.gethostname()


def get_local_ip():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
        sock.close()
        return ip

    except Exception:
        return "Unavailable"


def get_mac_address():
    mac = uuid.getnode()

    mac_address = ":".join(
        ["{:02x}".format((mac >> i) & 0xff) for i in range(40, -1, -8)]
    )

    return mac_address


def get_network_interfaces():
    interfaces = psutil.net_if_addrs()

    for name, addresses in interfaces.items():

        ipv4_addresses = []

        for address in addresses:
            if address.family == socket.AF_INET:
                ipv4_addresses.append(address.address)

        if ipv4_addresses:
            print(f"\nInterface: {name}")

            for ip in ipv4_addresses:
                print(f"  IPv4 : {ip}")


def get_gateway():
    gateways = psutil.net_if_stats()

    print("\nNetwork Status:")

    for name, info in gateways.items():
        status = "UP" if info.isup else "DOWN"
        speed = f"{info.speed} Mbps"

        print(f"{name}: {status} ({speed})")


def main():

    print("=" * 35)
    print("          IP INFORMATION")
    print("=" * 35)

    print(f"""
Hostname : {get_hostname()}
OS       : {platform.system()} {platform.release()}
Python   : {platform.python_version()}
Local IP : {get_local_ip()}
MAC      : {get_mac_address()}
""")

    print("=" * 35)
    print("       NETWORK INTERFACES")
    print("=" * 35)

    get_network_interfaces()

    print("\n" + "=" * 35)
    print("       INTERFACE STATUS")
    print("=" * 35)

    get_gateway()


if __name__ == "__main__":
    main()