# Networks

A collection of Python-based networking tools designed for network diagnostics, troubleshooting, and DevOps automation tasks.

## Overview

The `Networks` directory contains practical Python utilities for network analysis, connectivity testing, service inspection, and basic monitoring.

These tools are built to improve understanding of:

- Network programming
- TCP/IP concepts
- DNS resolution
- HTTP communication
- SSL/TLS certificates
- Network troubleshooting
- DevOps monitoring workflows

---

# Tools

## IP Information Tool

**File:**
```
ip_info.py
```

### Description

A utility that collects system and network information.

### Features

- Display hostname
- Show operating system information
- Display Python version
- Get MAC address
- Display network interfaces
- Show IPv4 addresses
- Detect VPN interfaces

### Usage

```bash
python3 ip_info.py
```

---

## Ping Checker

**File:**
```
ping_checker.py
```

### Description

A connectivity testing tool that checks whether a host or IP address is reachable.

### Features

- Check host availability
- Detect UP/DOWN status
- Support hostname and IP address
- Measure response latency

### Usage

```bash
python3 ping_checker.py
```

---

## Port Scanner

**File:**
```
port_scanner.py
```

### Description

A TCP port scanning utility for checking available ports on a target host.

### Features

- Scan TCP ports
- Detect open ports
- Check service accessibility
- Measure connection response time

### Usage

```bash
python3 port_scanner.py
```

---

## DNS Lookup Tool

**File:**
```
dns_lookup.py
```

### Description

A DNS diagnostic utility that resolves domain names and retrieves IP information.

### Features

- Resolve domain names
- Display hostname
- Display IP addresses
- Perform DNS troubleshooting

### Usage

```bash
python3 dns_lookup.py
```

---

## Website Status Checker

**File:**
```
website_checker.py
```

### Description

A website monitoring tool that checks HTTP/HTTPS availability.

### Features

- Check website availability
- Display HTTP status code
- Measure response time
- Detect connection failures
- Support HTTP and HTTPS URLs

### Requirements

Install dependency:

```bash
pip3 install requests
```

### Usage

```bash
python3 website_checker.py
```

---

## SSL Certificate Checker

**File:**
```
ssl_checker.py
```

### Description

A TLS/SSL certificate inspection tool for monitoring certificate validity.

### Features

- Retrieve SSL certificate information
- Display certificate issuer
- Show expiration date
- Calculate remaining validity days

### Usage

```bash
python3 ssl_checker.py
```

---

## Network Interface Information

**File:**
```
network_interface_info.py
```

### Description

A tool that displays detailed information about system network interfaces.

### Features

- List network interfaces
- Display IPv4 addresses
- Display IPv6 addresses
- Show MAC addresses
- Display interface status
- Show connection speed

### Requirements

Install dependency:

```bash
pip3 install psutil
```

### Usage

```bash
python3 network_interface_info.py
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/NIGHTFURY0X01/python-scripts.git
```

Navigate to Networks:

```bash
cd python-scripts/Networks
```

Install dependencies:

```bash
pip3 install psutil requests
```

---

# Technologies Used

- Python 3
- Socket Programming
- TCP/IP
- HTTP Requests
- SSL/TLS
- psutil
- Network APIs

---

# Project Goals

This collection is part of a Python utilities project focused on:

- DevOps automation
- System administration
- Network monitoring
- Infrastructure troubleshooting
- Practical Python development

---

# Author

**NIGHTFURY0X01**(**Arash**)

---

# License

This project is created for educational and personal use.