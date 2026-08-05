"""
# PDF Merger

A Python-based PDF merging tool.

## Description

Combines multiple PDF files into a single PDF document.

## Features

- Merge multiple PDF files
- Maintain page order
- Create output PDF file
- Handle file errors

## Requirements

- Python 3.x
- pypdf

## Usage

python3 pdf_merger.py

## Technologies

- Python
- pypdf

## Purpose

Created as part of a Python utilities collection focused on
file management and automation.

"""

from pypdf import PdfWriter
import os



def merge_pdfs(pdf_files, output_file):

    writer = PdfWriter()


    for pdf in pdf_files:

        if not os.path.exists(pdf):

            print(
                f"File not found: {pdf}"
            )

            continue


        writer.append(pdf)


    with open(
        output_file,
        "wb"
    ) as file:

        writer.write(file)


    writer.close()



def main():

    print("=" * 50)
    print("             PDF MERGER")
    print("=" * 50)


    files = input(
        "PDF files (separated by comma): "
    )


    pdf_files = [
        file.strip()
        for file in files.split(",")
    ]


    output = input(
        "Output file name: "
    )


    if not output.endswith(".pdf"):

        output += ".pdf"


    merge_pdfs(
        pdf_files,
        output
    )


    print("-" * 50)

    print(
        f"Created: {output}"
    )



if __name__ == "__main__":
    main()