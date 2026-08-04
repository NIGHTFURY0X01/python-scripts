"""
# File Organizer

A Python-based file organization automation tool.

## Description

File Organizer automatically sorts files into folders based on their
extensions.

Useful for:
- File management automation
- Desktop organization
- System administration tasks
- Learning Python automation

## Features

- Scan directories
- Detect file extensions
- Create categorized folders
- Move files automatically
- Organize documents, images, videos, and archives

## Requirements

- Python 3.x

## Usage

python3 file_organizer.py

## Technologies

- Python
- OS module
- File handling

## Purpose

Created as part of a Python utilities collection focused on
automation, system administration, and DevOps tasks.

"""

import os
import shutil


FILE_TYPES = {

    "Images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".webp"
    ],

    "Documents": [
        ".pdf",
        ".docx",
        ".txt",
        ".xlsx",
        ".pptx"
    ],

    "Videos": [
        ".mp4",
        ".mkv",
        ".mov"
    ],

    "Archives": [
        ".zip",
        ".tar",
        ".gz",
        ".rar"
    ],

    "Code": [
        ".py",
        ".js",
        ".html",
        ".css",
        ".sh"
    ]

}


def get_category(extension):

    for category, extensions in FILE_TYPES.items():

        if extension.lower() in extensions:
            return category

    return "Other"


def organize_files(directory):

    for filename in os.listdir(directory):

        file_path = os.path.join(
            directory,
            filename
        )

        if os.path.isfile(file_path):

            extension = os.path.splitext(
                filename
            )[1]

            category = get_category(
                extension
            )

            folder = os.path.join(
                directory,
                category
            )

            os.makedirs(
                folder,
                exist_ok=True
            )

            shutil.move(
                file_path,
                os.path.join(
                    folder,
                    filename
                )
            )

            print(
                f"Moved: {filename} -> {category}"
            )


def main():

    print("=" * 45)
    print("          FILE ORGANIZER")
    print("=" * 45)

    directory = input(
        "Directory path: "
    )

    if not os.path.exists(directory):

        print("Directory not found")
        return

    organize_files(directory)

    print("\nOrganization completed!")


if __name__ == "__main__":
    main()