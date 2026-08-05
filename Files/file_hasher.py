"""
# File Hasher (SHA256)

A Python-based file hashing utility.

## Description

Generates SHA256 cryptographic hashes for files.

Useful for:
- File verification
- Integrity checking
- Security analysis
- Digital forensics

## Features

- Generate SHA256 hash
- Read large files safely
- Verify file fingerprints

## Usage

python3 file_hasher.py

## Technologies

- Python
- hashlib

"""

import hashlib
import os


def calculate_sha256(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:

        while chunk := file.read(4096):

            sha256.update(chunk)

    return sha256.hexdigest()



def main():

    print("=" * 50)
    print("          FILE HASHER SHA256")
    print("=" * 50)


    file_path = input(
        "File path: "
    )


    if not os.path.exists(file_path):

        print("File not found")
        return


    file_hash = calculate_sha256(
        file_path
    )


    print("-" * 50)

    print(
        f"File   : {file_path}"
    )

    print(
        f"SHA256 : {file_hash}"
    )


if __name__ == "__main__":
    main()