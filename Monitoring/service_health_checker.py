"""
# Service Health Checker

A Python-based service monitoring tool.

## Description

Service Health Checker verifies whether common Linux services
are running by using systemctl.

Useful for:
- DevOps monitoring
- Linux administration
- Infrastructure monitoring
- Server maintenance

## Features

- Detect operating system
- Check service status
- Display active/inactive state
- Handle unavailable services

## Requirements

- Python 3.x
- Linux (systemctl)

## Usage

python3 service_health_checker.py

## Technologies

- Python
- subprocess
- platform

## Purpose

Created as part of a Python utilities collection focused on
monitoring, DevOps, and system administration.

"""

import platform
import subprocess


SERVICES = [
    "nginx",
    "apache2",
    "docker",
    "ssh",
    "mysql"
]


def check_service(service):

    try:

        result = subprocess.run(
            [
                "systemctl",
                "is-active",
                service
            ],
            capture_output=True,
            text=True
        )

        status = result.stdout.strip()

        if status == "active":

            print(
                f"{service:<12} : RUNNING"
            )

        elif status:

            print(
                f"{service:<12} : {status.upper()}"
            )

        else:

            print(
                f"{service:<12} : NOT INSTALLED"
            )

    except FileNotFoundError:

        print(
            "systemctl is not available on this system."
        )


def main():

    print("=" * 50)
    print("        SERVICE HEALTH CHECKER")
    print("=" * 50)

    system = platform.system()

    print(f"Operating System: {system}")

    if system != "Linux":

        print(
            "\nThis version supports Linux systems that use systemctl."
        )

        return

    print("\nService Status")
    print("-" * 50)

    for service in SERVICES:

        check_service(service)


if __name__ == "__main__":
    main()