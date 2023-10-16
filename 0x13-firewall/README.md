# Firewall Configuration Project

![Alt text](https://www.ionos.com/digitalguide/fileadmin/DigitalGuide/Screenshots_2018/Firewall-EN.png)

## Project Overview

This project focuses on configuring and managing a firewall to enhance network security and control incoming and outgoing network traffic. We will use the Uncomplicated Firewall (UFW) tool to create and apply firewall rules to our server.

## Table of Contents

- [Project Overview](#project-overview)
- [Tasks](#tasks)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Tasks

The project consists of the following tasks:

1. **Block All Incoming Traffic Except Essential Ports**
   - In this task, we will configure the UFW firewall to block all incoming traffic while allowing specific TCP ports (22 for SSH, 443 for HTTPS SSL, and 80 for HTTP).
   - File: [0-block_all_incoming_traffic_but](./0x13-firewall/0-block_all_incoming_traffic_but)

2. **Port Forwarding (Advanced)**
   - This task involves implementing port forwarding to redirect incoming traffic on port 8080/TCP to port 80/TCP on the server.
   - File: [100-port_forwarding](./0x13-firewall/100-port_forwarding)

## Requirements

Before starting the project, make sure you have the following:

- Access to the target server(s) (e.g., web-01) for firewall configuration.
- Familiarity with the UFW (Uncomplicated Firewall) utility.
- Proper SSH access to your server to execute commands.
- Necessary permissions to modify firewall settings.

