"""
# File Integrity Checker

A Python-based file integrity monitoring tool.

## Description

File Integrity Checker uses cryptographic hashes to detect
unauthorized file modifications.

Useful for:
- Cybersecurity
- File monitoring
- Malware detection
- Server security
- DevOps security practices

## Features

- Generate SHA256 hash
- Compare file hashes
- Detect file modifications
- Monitor file integrity

## Requirements

- Python 3.x

## Usage

python3 file_integrity_checker.py

## Technologies

- Python
- hashlib
- File handling

## Purpose

Created as part of a Python utilities collection focused on
Cybersecurity, DevOps, and system administration tasks.

"""

import hashlib
import os


def calculate_hash(file_path):

    sha256 = hashlib.sha256()

    try:

        with open(
            file_path,
            "rb"
        ) as file:

            while chunk := file.read(4096):

                sha256.update(chunk)


        return sha256.hexdigest()


    except FileNotFoundError:

        return None



def main():

    print("=" * 45)
    print("     FILE INTEGRITY CHECKER")
    print("=" * 45)


    file_path = input(
        "File path: "
    )


    if not os.path.exists(file_path):

        print("File not found")
        return


    file_hash = calculate_hash(
        file_path
    )


    print("\nSHA256 Hash:")
    print(file_hash)


    saved_hash = input(
        "\nEnter previous hash (optional): "
    )


    if saved_hash:

        if saved_hash == file_hash:

            print(
                "\nStatus: File is unchanged"
            )

        else:

            print(
                "\nStatus: File was modified!"
            )



if __name__ == "__main__":
    main()

