# Files

A collection of Python-based file management and analysis tools.

## Overview

The `Files` directory contains Python utilities designed for managing, analyzing, and processing files.

These tools focus on:

- File management
- File integrity verification
- Duplicate detection
- PDF automation
- Storage analysis
- System administration tasks

---

# Tools

## 1. PDF Merger

**File:**

```
pdf_merger.py
```

### Description

Combines multiple PDF files into a single PDF document.

### Features

- Merge multiple PDF files
- Maintain page order
- Create output PDF files
- Handle missing files

### Requirements

Install dependency:

```bash
pip3 install pypdf
```

### Usage

```bash
python3 pdf_merger.py
```

---

## 2. Duplicate File Finder

**File:**

```
duplicate_file_finder.py
```

### Description

Finds duplicate files by comparing SHA256 hashes.

### Features

- Recursive directory scanning
- SHA256 file comparison
- Detect identical files
- Display duplicate groups

### Usage

```bash
python3 duplicate_file_finder.py
```

---

## 3. File Hasher (SHA256)

**File:**

```
file_hasher.py
```

### Description

Generates SHA256 cryptographic hashes for files.

### Features

- Generate SHA256 hash
- Verify file fingerprints
- Support large files
- File integrity checking

### Usage

```bash
python3 file_hasher.py
```

---

## 4. Directory Size Calculator

**File:**

```
directory_size_calculator.py
```

### Description

Calculates the total size of directories including all subdirectories and files.

### Features

- Recursive directory scanning
- Calculate storage usage
- Convert bytes to readable formats
- Handle permission errors

### Usage

```bash
python3 directory_size_calculator.py
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/NIGHTFURY0X01/python-scripts.git
```

Navigate to Files:

```bash
cd python-scripts/Files
```

Install required dependencies:

```bash
pip3 install pypdf
```

Run tools:

```bash
python3 tool_name.py
```

---

# Technologies Used

- Python 3
- hashlib
- os module
- pypdf
- File System Operations

---

# File Management Concepts Covered

This collection demonstrates:

- Recursive file scanning
- Hash-based file comparison
- Cryptographic hashing
- PDF processing
- Storage analysis
- File automation

---

# Project Goals

This collection is part of a Python utilities project focused on:

- Python development
- Automation skills
- DevOps practices
- System administration
- File management

---

# Future Improvements

Planned features:

- Command-line arguments
- Progress indicators
- Logging system
- File deletion confirmation
- GUI interface
- Scheduled cleanup tasks
- Cloud storage integration

---

# Author

Arash

---

# License

This project is created for educational and personal use.