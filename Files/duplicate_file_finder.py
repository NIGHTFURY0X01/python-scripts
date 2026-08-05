"""
# Duplicate File Finder

A Python-based duplicate file detection tool.

## Description

Finds duplicate files by comparing SHA256 hashes.

## Features

- Scan directories recursively
- Calculate SHA256 hashes
- Detect duplicate files
- Display duplicate groups

## Requirements

- Python 3.x

## Usage

python3 duplicate_file_finder.py

## Technologies

- Python
- hashlib
- os

## Purpose

Created as part of a Python utilities collection focused on
file management, automation, and system administration.

"""

import os
import hashlib



def calculate_hash(file_path):

    sha256 = hashlib.sha256()

    try:

        with open(
            file_path,
            "rb"
        ) as file:

            while chunk := file.read(4096):

                sha256.update(
                    chunk
                )

        return sha256.hexdigest()


    except PermissionError:

        return None



def find_duplicates(directory):

    hashes = {}

    duplicates = {}


    for root, dirs, files in os.walk(directory):

        for filename in files:

            file_path = os.path.join(
                root,
                filename
            )


            file_hash = calculate_hash(
                file_path
            )


            if file_hash is None:

                continue


            if file_hash in hashes:

                if file_hash not in duplicates:

                    duplicates[file_hash] = [
                        hashes[file_hash]
                    ]


                duplicates[file_hash].append(
                    file_path
                )


            else:

                hashes[file_hash] = file_path


    return duplicates



def main():

    print("=" * 60)
    print("             DUPLICATE FILE FINDER")
    print("=" * 60)


    directory = input(
        "Directory path: "
    )


    if not os.path.exists(directory):

        print(
            "Directory not found"
        )

        return


    duplicates = find_duplicates(
        directory
    )


    print("\nDuplicate Files")
    print("-" * 60)


    if not duplicates:

        print(
            "No duplicate files found."
        )

        return


    count = 1


    for file_hash, files in duplicates.items():

        print(
            f"\nGroup {count}"
        )

        for file in files:

            print(
                f" - {file}"
            )

        count += 1



if __name__ == "__main__":
    main()