"""
# Directory Size Calculator

A Python-based directory size calculation tool.

## Description

Calculates the total size of a directory including
all files and subdirectories.

## Features

- Recursive directory scanning
- Calculate total directory size
- Convert bytes to readable units
- Handle file access errors

## Requirements

- Python 3.x

## Usage

python3 directory_size_calculator.py

## Technologies

- Python
- os module

## Purpose

Created as part of a Python utilities collection focused on
file management, automation, and system administration.

"""

import os



def format_size(size):

    units = [
        "B",
        "KB",
        "MB",
        "GB",
        "TB"
    ]

    index = 0


    while size >= 1024 and index < len(units) - 1:

        size /= 1024
        index += 1


    return f"{size:.2f} {units[index]}"



def calculate_size(directory):

    total_size = 0


    for root, directories, files in os.walk(directory):

        for file in files:

            file_path = os.path.join(
                root,
                file
            )


            try:

                total_size += os.path.getsize(
                    file_path
                )

            except (
                FileNotFoundError,
                PermissionError
            ):

                continue


    return total_size



def main():

    print("=" * 55)
    print("        DIRECTORY SIZE CALCULATOR")
    print("=" * 55)


    directory = input(
        "Directory path: "
    )


    if not os.path.isdir(directory):

        print(
            "Directory not found"
        )

        return


    size = calculate_size(
        directory
    )


    print("-" * 55)

    print(
        f"Directory : {directory}"
    )

    print(
        f"Size      : {format_size(size)}"
    )


if __name__ == "__main__":
    main()
