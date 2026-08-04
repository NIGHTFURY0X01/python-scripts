"""
# Log Parser

A Python-based log analysis tool.

## Description

Log Parser reads log files and analyzes their contents to identify
important events such as errors, warnings, and failed operations.

Useful for:
- DevOps troubleshooting
- Server monitoring
- Log analysis
- Incident investigation

## Features

- Read log files
- Count ERROR messages
- Count WARNING messages
- Display matched log lines
- Analyze application/system logs

## Requirements

- Python 3.x

## Usage

python3 log_parser.py

## Technologies

- Python
- File handling
- Regular expressions

## Purpose

Created as part of a Python utilities collection focused on
system administration and DevOps automation tasks.

"""

import re
import os


def analyze_logs(file_path):

    errors = []
    warnings = []

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            for line_number, line in enumerate(
                file,
                start=1
            ):

                if re.search(
                    r"error|failed|critical",
                    line,
                    re.IGNORECASE
                ):
                    errors.append(
                        (line_number, line.strip())
                    )

                if re.search(
                    r"warning|warn",
                    line,
                    re.IGNORECASE
                ):
                    warnings.append(
                        (line_number, line.strip())
                    )

        return errors, warnings

    except FileNotFoundError:

        return None, None


def main():

    print("=" * 45)
    print("             LOG PARSER")
    print("=" * 45)

    log_file = input(
        "Enter log file path: "
    )

    if not os.path.exists(log_file):

        print("\nFile not found")
        return


    errors, warnings = analyze_logs(
        log_file
    )


    print("\nLog Report")
    print("-" * 45)

    print(
        f"Errors   : {len(errors)}"
    )

    print(
        f"Warnings : {len(warnings)}"
    )


    if errors:

        print("\nERROR EVENTS")

        for number, line in errors[:5]:

            print(
                f"[Line {number}] {line}"
            )


    if warnings:

        print("\nWARNING EVENTS")

        for number, line in warnings[:5]:

            print(
                f"[Line {number}] {line}"
            )


if __name__ == "__main__":
    main()