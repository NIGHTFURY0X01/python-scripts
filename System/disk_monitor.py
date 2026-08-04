"""
# Disk Usage Monitor

A Python-based system monitoring tool that displays disk usage information.

## Description

Disk Usage Monitor collects storage information from the system and shows
total space, used space, available space, and usage percentage.

Useful for:
- DevOps monitoring
- Server maintenance
- Storage management
- Infrastructure troubleshooting

## Features

- Display total disk space
- Display used disk space
- Display free disk space
- Display disk usage percentage
- Monitor root filesystem

## Requirements

- Python 3.x
- psutil

Install dependency:

pip3 install psutil

## Usage

python3 disk_monitor.py

## Technologies

- Python
- psutil
- System monitoring APIs

## Purpose

Created as part of a Python utilities collection focused on
system administration and DevOps automation tasks.

"""

import psutil
import platform


def convert_bytes(value):

    gb = value / (1024 ** 3)

    return round(gb, 2)


def show_disk_info():

    disk = psutil.disk_usage("/")

    print("=" * 40)
    print("          DISK MONITOR")
    print("=" * 40)

    print(f"System       : {platform.system()}")

    print(
        f"Total Space  : {convert_bytes(disk.total)} GB"
    )

    print(
        f"Used Space   : {convert_bytes(disk.used)} GB"
    )

    print(
        f"Free Space   : {convert_bytes(disk.free)} GB"
    )

    print(
        f"Usage        : {disk.percent}%"
    )


def main():

    show_disk_info()


if __name__ == "__main__":
    main()