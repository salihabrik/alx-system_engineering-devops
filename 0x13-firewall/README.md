# Firewall Configuration Project

![alt text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png)

## Project Overview

This project focuses on configuring and managing a firewall to enhance network security and control incoming and outgoing network traffic. We will use the Uncomplicated Firewall (UFW) tool to create and apply firewall rules to our server.

#

## Table of Contents

- [Project Description](#project-description)
- [Task 0: Block all incoming traffic](#task-0-block-all-incoming-traffic)
- [Task 1: Port Forwarding](#task-1-port-forwarding)
- [Repository](#repository)

## Project Description

This project involves configuring a firewall using Uncomplicated Firewall (UFW) on the web server (web-01). The primary objectives are:

- Block all incoming traffic except for specific TCP ports: 22 (SSH), 443 (HTTPS SSL), and 80 (HTTP).
- Implement port forwarding to redirect incoming traffic from port 8080/TCP to port 80/TCP.

These tasks aim to enhance the security and control of network traffic on the web server.

## Task 0: Block all incoming traffic

**Requirements:**
- Configure UFW on web-01 to block all incoming traffic, except for the following TCP ports:
  - 22 (SSH)
  - 443 (HTTPS SSL)
  - 80 (HTTP)

You should share the UFW commands used in your answer file.

For detailed instructions, refer to the task file: [0-block_all_incoming_traffic_but](./0x13-firewall/0-block_all_incoming_traffic_but)

## Task 1: Port Forwarding (Advanced)

**Requirements:**
- Configure web-01's firewall to redirect incoming traffic from port 8080/TCP to port 80/TCP.

Your answer file should be a copy of the UFW configuration file that you modified to make this happen.

For detailed instructions, refer to the task file: [100-port_forwarding](./0x13-firewall/100-port_forwarding)

## Repository

- GitHub Repository: [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)
- Directory: [0x13-firewall](https://github.com/yourusername/alx-system_engineering-devops/tree/master/0x13-firewall)

Feel free to customize this README with specific project details and additional information as needed. Good luck with your firewall configuration project!
