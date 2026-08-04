# Security

A collection of Python-based cybersecurity tools focused on security analysis, file integrity monitoring, password security, and cryptographic operations.

## Overview

The `Security` directory contains practical Python utilities designed for learning cybersecurity concepts and building automation skills related to security operations.

These tools focus on:

- Password security
- Cryptography basics
- File integrity monitoring
- Hash generation
- Security automation
- DevSecOps practices

---

# Tools

## 1. Password Strength Checker

**File:**

```
password_strength_checker.py
```

### Description

Analyzes password strength based on common security requirements.

### Features

- Check password length
- Detect uppercase letters
- Detect lowercase letters
- Detect numbers
- Detect special characters
- Generate security score

### Usage

```bash
python3 password_strength_checker.py
```

---

## 2. Password Generator

**File:**

```
password_generator.py
```

### Description

Generates strong random passwords using multiple character sets.

### Features

- Generate random passwords
- Custom password length
- Include uppercase letters
- Include lowercase letters
- Include numbers
- Include special characters

### Usage

```bash
python3 password_generator.py
```

---

## 3. File Integrity Checker

**File:**

```
file_integrity_checker.py
```

### Description

Checks file integrity by comparing cryptographic hashes.

### Features

- Generate SHA256 hashes
- Detect file modifications
- Monitor important files
- Verify file integrity

### Usage

```bash
python3 file_integrity_checker.py
```

---

## 4. Hash Generator

**File:**

```
hash_generator.py
```

### Description

Generates cryptographic hashes for text and files.

### Supported Algorithms

- MD5
- SHA1
- SHA256

### Features

- Hash text input
- Hash files
- Compare file fingerprints
- Generate cryptographic identifiers

### Usage

```bash
python3 hash_generator.py
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/NIGHTFURY0X01/python-scripts.git
```

Navigate to Security:

```bash
cd python-scripts/Security
```

Run tools:

```bash
python3 tool_name.py
```

---

# Technologies Used

- Python 3
- hashlib
- Regular Expressions
- File Handling
- Cryptographic Functions

---

# Security Concepts Covered

This collection demonstrates:

- Password policies
- Hashing algorithms
- File integrity monitoring
- Basic security automation
- Cryptographic concepts
- Secure programming practices

---

# Project Goals

This collection is part of a Python utilities project focused on:

- Cybersecurity learning
- DevSecOps automation
- Security tooling development
- System administration
- Practical Python skills

---

# Future Improvements

Planned improvements:

- CLI arguments
- Configuration files
- Logging system
- Database for hash storage
- Automated integrity monitoring
- Security report generation
- Integration with security tools

---

# Author

Arash

---

# License

This project is created for educational and personal use.
