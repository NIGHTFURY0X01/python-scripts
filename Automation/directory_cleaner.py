"""
# Directory Cleaner

A Python-based directory cleanup automation tool.

## Description

Directory Cleaner removes old files from a directory based on
their age.

Useful for:
- DevOps automation
- Log cleanup
- Temporary file management
- Server maintenance

## Features

- Scan directories
- Find old files
- Remove files by age
- Display deleted files
- Automate cleanup tasks

## Requirements

- Python 3.x

## Usage

python3 directory_cleaner.py

## Technologies

- Python
- OS module
- Time module
- File handling

## Purpose

Created as part of a Python utilities collection focused on
automation, system administration, and DevOps tasks.

"""

import os
import time


def clean_directory(directory, days):

    current_time = time.time()

    deleted_files = 0


    for root, dirs, files in os.walk(directory):

        for file in files:

            file_path = os.path.join(
                root,
                file
            )

            file_time = os.path.getmtime(
                file_path
            )

            age = (
                current_time - file_time
            ) / (60 * 60 * 24)


            if age > days:

                os.remove(
                    file_path
                )

                print(
                    f"Deleted: {file_path}"
                )

                deleted_files += 1


    return deleted_files



def main():

    print("=" * 45)
    print("        DIRECTORY CLEANER")
    print("=" * 45)


    directory = input(
        "Directory path: "
    )


    days = int(
        input(
            "Delete files older than (days): "
        )
    )


    if not os.path.exists(directory):

        print("Directory not found")
        return


    deleted = clean_directory(
        directory,
        days
    )


    print("\nCleanup completed")

    print(
        f"Deleted files: {deleted}"
    )


if __name__ == "__main__":
    main()