# Webstack Monitoring Project

This project focuses on implementing web stack monitoring using Datadog. It includes tasks related to signing up for Datadog, installing the Datadog agent, setting up monitors, and creating a dashboard.


## Tasks

### Task 0: Sign up for Datadog and install datadog-agent
1. Visit [Datadog](https://www.datadoghq.com/) and sign up for a free account.
2. Use the US website (https://app.datadoghq.com) and select the US1 region.
3. Install the Datadog agent on `web-01`.
4. Create an application key.
5. Copy-paste your Datadog API key and application key in your Intranet user profile.
6. Verify that your server `web-01` is visible in Datadog under the hostname `XX-web-01`.

[alternative link to sign up for Datadog](https://www.datadoghq.eu/)

[Datadog API docs](https://docs.datadoghq.com/api/?lang=python)

[Datadog Agent](https://docs.datadoghq.com/agent/)

[Public Datadog Dashboards](https://www.datadoghq.com/dashboards/)

[Datadog API Keys](https://app.datadoghq.com/account/settings#api)

[Datadog Application Key](https://app.datadoghq.com/account/settings#api)

[Datadog Forwarder](https://docs.datadoghq.com/logs/log_collection/?tab=forwarders)

[Datadog Agent Installation](https://docs.datadoghq.com/agent/basic_agent_usage/ubuntu/?tab=agentv6)

[How to Create a Dashboard](https://docs.datadoghq.com/dashboards/)

[How to Create a Monitor](https://docs.datadoghq.com/monitors/)

[How to Set Up Autodiscovery](https://docs.datadoghq.com/agent/autodiscovery/?tab=standard)
[How to Install the Datadog Agent](https://docs.datadoghq.com/agent/basic_agent_usage/ubuntu/?tab=agentv6)

![Alt text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/314/WIxXad8.png)
 
![alt text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/314/82VsYEC.png)

![alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6a4551974aadc181e97a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231109T105218Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=67f2a40f0298eab84ac3ff45ac20d0c9850ec31d64f784266162b427607bc1bf)
### Task 1: Monitor some metrics
1. Set up a monitor to check the number of read requests issued to the device per second.
2. Set up a monitor to check the number of write requests issued to the device per second.

### Task 2: Create a dashboard
1. Create a new dashboard.
2. Add at least 4 widgets to your dashboard, monitoring whatever metrics you'd like.
3. Save the dashboard, and note down the `dashboard_id`.
4. Create a file named `2-setup_datadog` with the `dashboard_id` on the first line.

## Repository Structure

- GitHub Repository: [alx-system_engineering-devops](link-to-repo)
- Directory: [0x18-webstack_monitoring](link-to-directory)

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Copyright Information

Copyright © 2023 ALX, All rights reserved.

