"""
# File Backup Automation

A Python-based backup automation tool.

## Description

File Backup Automation creates compressed backups from selected directories.

Useful for:
- DevOps automation
- Server backups
- Data protection
- System administration

## Features

- Backup files and directories
- Create ZIP archives
- Add timestamp to backup files
- Automate backup workflow

## Requirements

- Python 3.x

## Usage

python3 file_backup.py

## Technologies

- Python
- Zipfile
- File handling

## Purpose

Created as part of a Python utilities collection focused on
automation, system administration, and DevOps tasks.

"""

import os
import zipfile
from datetime import datetime


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
    ) as backup:

        if os.path.isfile(source):

            backup.write(
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

                    backup.write(
                        file_path,
                        os.path.relpath(
                            file_path,
                            source
                        )
                    )

    return backup_path


def main():

    print("=" * 45)
    print("          FILE BACKUP TOOL")
    print("=" * 45)

    source = input(
        "Source path: "
    )

    destination = input(
        "Backup destination: "
    )

    if not os.path.exists(source):

        print("Source not found")
        return

    if not os.path.exists(destination):

        os.makedirs(destination)


    backup = create_backup(
        source,
        destination
    )

    print("\nBackup created:")
    print(backup)


if __name__ == "__main__":
    main()