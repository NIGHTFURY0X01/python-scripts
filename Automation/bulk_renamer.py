"""
# Bulk Renamer

A Python-based bulk file renaming automation tool.

## Description

Bulk Renamer allows users to rename multiple files in a directory
using a custom prefix and automatic numbering.

Useful for:
- File management automation
- Backup organization
- Data organization
- System administration tasks

## Features

- Rename multiple files
- Add custom prefix
- Add automatic numbering
- Preserve file extensions
- Preview rename operations

## Requirements

- Python 3.x

## Usage

python3 bulk_renamer.py

## Technologies

- Python
- OS module
- File handling

## Purpose

Created as part of a Python utilities collection focused on
automation, system administration, and DevOps tasks.

"""

import os


def rename_files(directory, prefix):

    files = []

    for file in os.listdir(directory):

        path = os.path.join(
            directory,
            file
        )

        if os.path.isfile(path):
            files.append(file)


    files.sort()

    counter = 1


    for file in files:

        old_path = os.path.join(
            directory,
            file
        )

        name, extension = os.path.splitext(
            file
        )

        new_name = (
            f"{prefix}_{counter}{extension}"
        )

        new_path = os.path.join(
            directory,
            new_name
        )


        os.rename(
            old_path,
            new_path
        )

        print(
            f"{file} -> {new_name}"
        )

        counter += 1



def main():

    print("=" * 45)
    print("           BULK RENAMER")
    print("=" * 45)


    directory = input(
        "Directory path: "
    )

    prefix = input(
        "New file prefix: "
    )


    if not os.path.exists(directory):

        print("Directory not found")
        return


    rename_files(
        directory,
        prefix
    )


    print("\nRename completed!")


if __name__ == "__main__":
    main()