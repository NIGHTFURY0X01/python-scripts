"""
# Backup Tool

A Python-based backup automation utility.

## Description

Backup Tool creates compressed backups from files or directories
with timestamped archive names.

Useful for:
- DevOps automation
- Server backup tasks
- Data protection
- System administration

## Features

- Backup files and directories
- Create ZIP archives
- Add timestamp to backups
- Display backup size
- Automate backup workflow

## Requirements

- Python 3.x

## Usage

python3 backup_tool.py

## Technologies

- Python
- zipfile
- os module
- File handling

## Purpose

Created as part of a Python utilities collection focused on
automation, system administration, and DevOps tasks.

"""

import os
import zipfile
from datetime import datetime


def get_size(path):

    size = os.path.getsize(path)

    return round(
        size / (1024 * 1024),
        2
    )


def create_backup(source, destination):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    backup_name = f"backup_{timestamp}.zip"

    backup_path = os.path.join(
        destination,
        backup_name
    )

    with zipfile.ZipFile(
        backup_path,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zip_file:

        if os.path.isfile(source):

            zip_file.write(
                source,
                os.path.basename(source)
            )

        else:

            for root, dirs, files in os.walk(source):

                for file in files:

                    file_path = os.path.join(
                        root,
                        file
                    )

                    archive_name = os.path.relpath(
                        file_path,
                        source
                    )

                    zip_file.write(
                        file_path,
                        archive_name
                    )

    return backup_path


def main():

    print("=" * 45)
    print("             BACKUP TOOL")
    print("=" * 45)

    source = input(
        "Source path: "
    )

    destination = input(
        "Backup folder: "
    )


    if not os.path.exists(source):

        print("Source does not exist")
        return


    os.makedirs(
        destination,
        exist_ok=True
    )


    backup = create_backup(
        source,
        destination
    )


    print("\nBackup completed successfully")

    print(
        f"File : {backup}"
    )

    print(
        f"Size : {get_size(backup)} MB"
    )


if __name__ == "__main__":
    main()
