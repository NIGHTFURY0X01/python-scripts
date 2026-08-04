"""
# Process Viewer

A Python-based system monitoring tool that displays running processes.

## Description

Process Viewer collects information about active processes and shows
resource usage including CPU and memory consumption.

Useful for:
- DevOps monitoring
- Server troubleshooting
- Performance analysis
- System administration

## Features

- Display running processes
- Show process ID (PID)
- Show process name
- Display CPU usage
- Display memory usage
- Display top resource-consuming processes

## Requirements

- Python 3.x
- psutil

Install dependency:

pip3 install psutil

## Usage

python3 process_viewer.py

## Technologies

- Python
- psutil
- System process APIs

## Purpose

Created as part of a Python utilities collection focused on
system administration and DevOps automation tasks.

"""

import psutil
import platform


def get_processes():

    processes = []

    for process in psutil.process_iter(
        [
            "pid",
            "name",
            "cpu_percent",
            "memory_percent"
        ]
    ):

        try:
            info = process.info

            # Fix missing values
            if info["cpu_percent"] is None:
                info["cpu_percent"] = 0

            if info["memory_percent"] is None:
                info["memory_percent"] = 0

            processes.append(info)

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    return processes


def show_processes():

    print("=" * 70)
    print("                    PROCESS VIEWER")
    print("=" * 70)

    print(f"System: {platform.system()}")

    processes = get_processes()

    # Sort by CPU usage
    processes.sort(
        key=lambda x: x["cpu_percent"],
        reverse=True
    )

    print()

    print(
        f"{'PID':<10}"
        f"{'NAME':<30}"
        f"{'CPU %':<10}"
        f"{'RAM %'}"
    )

    print("-" * 70)

    for process in processes[:10]:

        name = process["name"] or "Unknown"

        print(
            f"{str(process['pid']):<10}"
            f"{name[:28]:<30}"
            f"{round(process['cpu_percent'],2):<10}"
            f"{round(process['memory_percent'],2)}"
        )


def main():

    show_processes()


if __name__ == "__main__":
    main()