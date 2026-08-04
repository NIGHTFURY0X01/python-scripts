"""
# Port Scanner Tool

A Python-based network utility that checks open ports on a target host.

## Description

Port Scanner is a lightweight tool designed to identify available TCP ports
on a target machine.

It can be used for:
- Network troubleshooting
- Learning TCP communication
- Basic security auditing
- DevOps network checks

## Features

- Scan TCP ports
- Check open and closed ports
- Support hostname and IP address
- Measure connection response time
- Simple command-line interface

## Requirements

- Python 3.x

## Usage

python3 port_scanner.py

## Technologies

- Python
- Socket programming

## Purpose

Created as part of a Python utilities collection focused on networking,
system administration, and DevOps automation tasks.

"""

import socket
import time


def scan_port(host, port):
    try:
        start = time.time()

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((host, port))

        end = time.time()

        latency = round((end - start) * 1000, 2)

        sock.close()

        if result == 0:
            return True, latency

        return False, None

    except Exception:
        return False, None


def main():

    print("=" * 35)
    print("          PORT SCANNER")
    print("=" * 35)

    host = input("Enter host/IP: ")

    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))

    print("\nScanning...\n")

    for port in range(start_port, end_port + 1):

        is_open, latency = scan_port(host, port)

        if is_open:
            print(
                f"[OPEN] Port {port} | {latency} ms"
            )


if __name__ == "__main__":
    main()