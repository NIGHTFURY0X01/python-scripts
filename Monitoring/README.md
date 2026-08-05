# Monitoring

A collection of Python-based monitoring tools designed for website availability, system health checks, SSL monitoring, and infrastructure management.

## Overview

The `Monitoring` directory contains Python utilities that help monitor system resources, services, and external applications.

These tools focus on:

- Website availability monitoring
- Service health checking
- SSL certificate monitoring
- Disk usage monitoring
- DevOps infrastructure practices

---

# Tools

## 1. Website Uptime Monitor

**File:**

```
website_uptime_monitor.py
```

### Description

Checks website availability, HTTP status code, and response time.

### Features

- Check website online/offline status
- Display HTTP status code
- Measure response time
- Handle connection errors
- Detect timeout issues

### Usage

```bash
python3 website_uptime_monitor.py
```

---

## 2. Service Health Checker

**File:**

```
service_health_checker.py
```

### Description

Checks the status of system services on Linux servers using systemctl.

### Features

- Detect operating system
- Check service status
- Monitor common services
- Display running/inactive state

### Supported Services

- nginx
- apache2
- docker
- ssh
- mysql

### Usage

```bash
python3 service_health_checker.py
```

---

## 3. SSL Certificate Expiry Checker

**File:**

```
ssl_certificate_expiry_checker.py
```

### Description

Checks SSL/TLS certificate expiration dates for domains.

### Features

- Connect to HTTPS services
- Retrieve SSL certificates
- Display expiration date
- Calculate remaining days
- Warn about certificate expiration

### Usage

```bash
python3 ssl_certificate_expiry_checker.py
```

---

## 4. Disk Space Alert

**File:**

```
disk_space_alert.py
```

### Description

Monitors disk usage and provides warnings when storage usage exceeds a defined threshold.

### Features

- Display total disk space
- Display used space
- Display free space
- Calculate usage percentage
- Configurable warning threshold

### Usage

```bash
python3 disk_space_alert.py
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/NIGHTFURY0X01/python-scripts.git
```

Navigate to Monitoring:

```bash
cd python-scripts/Monitoring
```

Install dependencies:

```bash
pip3 install requests
```

Run tools:

```bash
python3 tool_name.py
```

---

# Technologies Used

- Python 3
- Requests
- SSL Module
- Socket Programming
- Subprocess
- Shutil
- HTTP Protocol

---

# Monitoring Concepts Covered

This collection demonstrates:

- Availability monitoring
- Health checks
- SSL certificate management
- Resource monitoring
- Infrastructure automation
- DevOps monitoring practices

---

# Project Goals

This collection is part of a Python utilities project focused on:

- DevOps engineering skills
- System administration
- Infrastructure monitoring
- Automation
- Practical Python development

---

# Future Improvements

Planned features:

- Continuous monitoring mode
- Configuration files
- Logging system
- Alert notifications
- Email alerts
- Discord/Slack Webhooks
- JSON and CSV reports
- Dashboard integration

---

# Author

Arash

---

# License

This project is created for educational and personal use.