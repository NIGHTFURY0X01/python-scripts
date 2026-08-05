"""
# Disk Space Alert

A Python-based disk usage monitoring tool.

## Description

Disk Space Alert checks disk usage and warns when usage
exceeds a specified threshold.

Useful for:
- DevOps monitoring
- Server administration
- Infrastructure monitoring
- Storage management

## Features

- Display total disk space
- Display used disk space
- Display free disk space
- Show disk usage percentage
- Configurable warning threshold

## Requirements

- Python 3.x

## Usage

python3 disk_space_alert.py

## Technologies

- Python
- shutil

## Purpose

Created as part of a Python utilities collection focused on
monitoring, DevOps, and system administration.

"""

import shutil


def bytes_to_gb(size):

    return round(
        size / (1024 ** 3),
        2
    )


def check_disk(threshold):

    total, used, free = shutil.disk_usage("/")

    usage_percent = (
        used / total
    ) * 100

    print("=" * 50)
    print("           DISK SPACE ALERT")
    print("=" * 50)

    print(
        f"Total Space : {bytes_to_gb(total)} GB"
    )

    print(
        f"Used Space  : {bytes_to_gb(used)} GB"
    )

    print(
        f"Free Space  : {bytes_to_gb(free)} GB"
    )

    print(
        f"Usage       : {usage_percent:.2f}%"
    )

    print(
        f"Threshold   : {threshold}%"
    )

    print("-" * 50)

    if usage_percent >= threshold:

        print("Status      : WARNING")

    else:

        print("Status      : HEALTHY")


def main():

    print("=" * 50)
    print("           DISK SPACE ALERT")
    print("=" * 50)

    try:

        threshold = float(
            input(
                "Warning threshold (%): "
            )
        )

    except ValueError:

        print(
            "Invalid number."
        )

        return

    check_disk(
        threshold
    )


if __name__ == "__main__":
    main()