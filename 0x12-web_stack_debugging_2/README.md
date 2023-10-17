# Web Stack Debugging Project

This project is part of the ALX DevOps curriculum and focuses on web stack debugging in an Ubuntu 20.04 environment. The goal of this project is to complete two tasks related to system administration, scripting, and debugging.

## Table of Contents

- [Project Description](#project-description)
- [Tasks](#tasks)
  - [Task 0: Run software as another user](#task-0-run-software-as-another-user)
  - [Task 1: Run Nginx as Nginx](#task-1-run-nginx-as-nginx)
- [Requirements](#requirements)
- [Usage](#usage)
- [Contributors](#contributors)

## Project Description

In this project, we perform web stack debugging and system administration tasks using Bash scripting. The tasks are designed to enhance our understanding of running processes as specific users and securing web servers by running them under less privileged users.

## Tasks

### Task 0: Run software as another user

- The Bash script accepts one argument, which is a username.
- The script runs the `whoami` command under the user specified as an argument.

### Task 1: Run Nginx as Nginx

- This task aims to configure the Nginx web server to run as the `nginx` user.
- Nginx should listen on all active IPs on port 8080.
- The task should be completed without using `apt-get remove`.

## Requirements

- All scripts are interpreted on Ubuntu 20.04 LTS.
- Each script must end with a newline.
- Bash scripts should be executable.
- Bash scripts should pass Shellcheck without any errors.
- The first line of all Bash scripts should be `#!/usr/bin/env bash`.
- A README.md file at the root of the project folder is mandatory.

## Usage

To run each task's script, follow the instructions provided in the task descriptions. For example:

For Task 0:

```bash
./0-iamsomeoneelse <username>
