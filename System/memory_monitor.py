"""
# Memory Monitor

A Python-based system monitoring tool that displays RAM usage information.

## Description

Memory Monitor collects real-time memory statistics from the system,
including total memory, used memory, available memory, and usage percentage.

Useful for:
- DevOps monitoring
- Server troubleshooting
- System administration
- Performance analysis

## Features

- Display total RAM
- Display used RAM
- Display available RAM
- Display RAM usage percentage
- Display memory statistics

## Requirements

- Python 3.x
- psutil

Install dependency:

pip3 install psutil

## Usage

python3 memory_monitor.py

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


def show_memory_info():

    memory = psutil.virtual_memory()

    print("=" * 40)
    print("          MEMORY MONITOR")
    print("=" * 40)

    print(f"System        : {platform.system()}")

    print(
        f"Total RAM     : {convert_bytes(memory.total)} GB"
    )

    print(
        f"Used RAM      : {convert_bytes(memory.used)} GB"
    )

    print(
        f"Available RAM : {convert_bytes(memory.available)} GB"
    )

    print(
        f"Usage         : {memory.percent}%"
    )


def main():
    show_memory_info()


if __name__ == "__main__":
    main()