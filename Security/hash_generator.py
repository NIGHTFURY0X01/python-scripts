"""
# Hash Generator

A Python-based hash generation tool.

## Description

Hash Generator creates cryptographic hashes for text and files.
Hashes are used for data verification, integrity checking, and security.

Useful for:
- Cybersecurity
- File verification
- Digital forensics
- Secure development
- DevOps security

## Features

- Generate MD5 hash
- Generate SHA1 hash
- Generate SHA256 hash
- Hash text input
- Hash files

## Requirements

- Python 3.x

## Usage

python3 hash_generator.py

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


def generate_hash(data, algorithm):

    hash_function = hashlib.new(
        algorithm
    )

    hash_function.update(
        data
    )

    return hash_function.hexdigest()



def hash_text(text):

    data = text.encode()

    print("\nHash Results")
    print("-" * 40)

    for algorithm in [
        "md5",
        "sha1",
        "sha256"
    ]:

        print(
            f"{algorithm.upper()}:"
        )

        print(
            generate_hash(
                data,
                algorithm
            )
        )

        print()



def hash_file(file_path):

    try:

        with open(
            file_path,
            "rb"
        ) as file:

            data = file.read()


        print("\nHash Results")
        print("-" * 40)


        for algorithm in [
            "md5",
            "sha1",
            "sha256"
        ]:

            print(
                f"{algorithm.upper()}:"
            )

            print(
                generate_hash(
                    data,
                    algorithm
                )
            )

            print()


    except FileNotFoundError:

        print("File not found")



def main():

    print("=" * 45)
    print("          HASH GENERATOR")
    print("=" * 45)


    choice = input(
        "1) Text\n2) File\nChoose: "
    )


    if choice == "1":

        text = input(
            "Enter text: "
        )

        hash_text(
            text
        )


    elif choice == "2":

        file_path = input(
            "File path: "
        )

        if os.path.exists(file_path):

            hash_file(
                file_path
            )

        else:

            print(
                "File not found"
            )


    else:

        print(
            "Invalid option"
        )


if __name__ == "__main__":
    main()

