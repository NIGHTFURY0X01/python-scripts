"""
# Ping Checker Tool

A Python-based network utility that checks the availability of a host or IP address.

## Description

Ping Checker is a lightweight networking tool designed to test connectivity between the local machine and a target host.

It uses the system ping command to determine whether a destination is reachable and measures the approximate response time.

This tool can be useful for:
- Network troubleshooting
- DevOps monitoring tasks
- Basic uptime checks
- Connectivity testing

## Features

- Check host availability
- Support hostname and IP address
- Cross-platform support (Windows/macOS/Linux)
- Detect UP or DOWN status
- Measure network latency
- Simple command-line interface

## Requirements

- Python 3.x
- Operating system ping utility

No external Python packages are required.

## Usage

Run the script:

python3 ping_checker.py


Enter a hostname or IP address:

google.com


## Example Output

===================================
          PING CHECKER
===================================

Enter host/IP: google.com

Status  : UP
Host    : google.com
Latency : 25.43 ms


## Technologies

- Python
- subprocess
- platform
- Network diagnostics


## Purpose

Created as part of a Python utilities collection focused on networking,
system administration, and DevOps automation tasks.

"""
import subprocess
import platform
import time


def ping_host(host):
    system = platform.system()

    if system == "Windows":
        command = ["ping", "-n", "1", host]
    else:
        command = ["ping", "-c", "1", host]

    try:
        start_time = time.time()

        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        end_time = time.time()

        latency = round((end_time - start_time) * 1000, 2)

        if result.returncode == 0:
            return True, latency

        return False, None

    except Exception:
        return False, None


def main():
    print("=" * 35)
    print("          PING CHECKER")
    print("=" * 35)

    host = input("Enter host/IP: ")

    status, latency = ping_host(host)

    print()

    if status:
        print(f"Status  : UP")
        print(f"Host    : {host}")
        print(f"Latency : {latency} ms")

    else:
        print(f"Status : DOWN")
        print(f"Host   : {host}")


if __name__ == "__main__":
    main()