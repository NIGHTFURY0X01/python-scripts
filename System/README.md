# System

A collection of Python-based system monitoring and administration tools designed for DevOps automation, troubleshooting, and infrastructure analysis.

## Overview

The `System` directory contains practical Python utilities that collect system information, monitor resources, analyze processes, and inspect logs.

These tools are built to improve understanding of:

- System monitoring
- Resource management
- Process analysis
- Log analysis
- Server troubleshooting
- DevOps automation workflows

---

# Tools

## 1. CPU Monitor

**File:**

```
cpu_monitor.py
```

### Description

A CPU monitoring utility that displays processor usage and system CPU information.

### Features

- Display CPU usage percentage
- Show CPU core count
- Display CPU frequency
- Show system processor information
- Monitor CPU performance

### Usage

```bash
python3 cpu_monitor.py
```

---

## 2. Memory Monitor

**File:**

```
memory_monitor.py
```

### Description

A RAM monitoring utility that displays memory usage statistics.

### Features

- Display total RAM
- Display used RAM
- Display available RAM
- Show memory usage percentage

### Usage

```bash
python3 memory_monitor.py
```

---

## 3. Disk Monitor

**File:**

```
disk_monitor.py
```

### Description

A disk usage monitoring tool that checks storage information.

### Features

- Display total disk space
- Display used space
- Display available space
- Show disk usage percentage

### Usage

```bash
python3 disk_monitor.py
```

---

## 4. Process Viewer

**File:**

```
process_viewer.py
```

### Description

A process monitoring tool similar to basic versions of `top` and `htop`.

### Features

- Display running processes
- Show process IDs
- Display process names
- Monitor CPU usage
- Monitor memory usage
- Show top resource-consuming processes

### Usage

```bash
python3 process_viewer.py
```

---

## 5. System Info

**File:**

```
system_info.py
```

### Description

A system information collector that displays operating system and hardware details.

### Features

- Display hostname
- Show operating system information
- Display OS version
- Show system architecture
- Display Python version
- Show boot time
- Calculate system uptime

### Usage

```bash
python3 system_info.py
```

---

## 6. Log Parser

**File:**

```
log_parser.py
```

### Description

A log analysis utility that searches log files for important events.

### Features

- Read log files
- Detect errors
- Detect warnings
- Find failed operations
- Generate log reports

### Usage

```bash
python3 log_parser.py
```

Example:

```text
Enter log file path: /var/log/system.log
```

---

# Requirements

Python 3.x

Install required dependencies:

```bash
pip3 install psutil
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/NIGHTFURY0X01/python-scripts.git
```

Navigate to System:

```bash
cd python-scripts/System
```

Install dependencies:

```bash
pip3 install psutil
```

---

# Technologies Used

- Python 3
- psutil
- File Handling
- Regular Expressions
- Operating System APIs

---

# Project Goals

This collection is part of a Python utilities project focused on:

- DevOps automation
- System administration
- Server monitoring
- Infrastructure troubleshooting
- Practical Python development

---

# Future Improvements

Planned improvements:

- JSON output support
- CLI arguments
- Automated monitoring reports
- Email notifications
- Integration with monitoring systems
- Docker support

---

# Author

Arash

---

# License

This project is created for educational and personal use.