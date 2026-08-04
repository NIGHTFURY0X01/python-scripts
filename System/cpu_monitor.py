"""
# CPU Monitor

A Python-based system monitoring tool that displays CPU information.

## Description

CPU Monitor collects real-time CPU statistics from the system and displays
processor usage information.

Useful for:
- DevOps monitoring
- Server troubleshooting
- System administration
- Performance analysis

## Features

- Display CPU usage percentage
- Display CPU core count
- Display CPU frequency
- Display CPU load information
- Monitor system performance

## Requirements

- Python 3.x
- psutil

Install dependency:

pip3 install psutil

## Usage

python3 cpu_monitor.py

## Technologies

- Python
- psutil
- System monitoring APIs

## Purpose

Created as part of a Python utilities collection focused on networking,
system administration, and DevOps automation tasks.

"""

import psutil
import platform
import time


def show_cpu_info():

    print("=" * 40)
    print("            CPU MONITOR")
    print("=" * 40)

    print(f"System       : {platform.system()}")
    print(f"Processor    : {platform.processor()}")

    print(f"CPU Cores    : {psutil.cpu_count()}")

    print(
        f"CPU Usage    : {psutil.cpu_percent(interval=1)}%"
    )

    frequency = psutil.cpu_freq()

    if frequency:
        print(
            f"Frequency    : {round(frequency.current,2)} MHz"
        )

    load = psutil.getloadavg() if hasattr(
        psutil, "getloadavg"
    ) else None

    if load:
        print(f"Load Average : {load}")


def main():

    show_cpu_info()


if __name__ == "__main__":
    main()