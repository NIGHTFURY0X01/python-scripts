"""
# System Info

A Python-based system information utility.

## Description

System Info collects general information about the operating system,
hardware, and runtime environment.

Useful for:
- DevOps diagnostics
- Server inventory
- System administration
- Infrastructure monitoring

## Features

- Display hostname
- Display operating system
- Display OS version
- Display architecture
- Display CPU information
- Display Python version
- Display boot time
- Display uptime

## Requirements

- Python 3.x
- psutil

Install dependency:

pip3 install psutil

## Usage

python3 system_info.py

## Technologies

- Python
- psutil
- Platform APIs

## Purpose

Created as part of a Python utilities collection focused on
system administration and DevOps automation tasks.

"""

import platform
import socket
import psutil
import datetime
import sys


def convert_seconds(seconds):

    uptime = datetime.timedelta(
        seconds=int(seconds)
    )

    return str(uptime)


def show_system_info():

    print("=" * 45)
    print("              SYSTEM INFO")
    print("=" * 45)

    print(f"Hostname       : {socket.gethostname()}")

    print(
        f"Operating System: {platform.system()}"
    )

    print(
        f"OS Version     : {platform.version()}"
    )

    print(
        f"Architecture   : {platform.machine()}"
    )

    print(
        f"Processor      : {platform.processor()}"
    )

    print(
        f"Python Version : {sys.version.split()[0]}"
    )

    boot_time = psutil.boot_time()

    boot_datetime = datetime.datetime.fromtimestamp(
        boot_time
    )

    print(
        f"Boot Time      : {boot_datetime}"
    )

    uptime_seconds = (
        datetime.datetime.now().timestamp()
        - boot_time
    )

    print(
        f"Uptime         : {convert_seconds(uptime_seconds)}"
    )


def main():

    show_system_info()


if __name__ == "__main__":
    main()