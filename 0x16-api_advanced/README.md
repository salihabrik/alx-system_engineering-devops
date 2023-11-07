# Reddit API Project

This project is a part of the ALX System Engineering & DevOps program, focusing on advanced API usage and Python scripting. The goal of this project is to interact with the Reddit API to perform various tasks related to subreddits.


![alt text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/314/WIxXad8.png)


## Table of Contents
1. [Project Description](#project-description)
2. [Tasks](#tasks)
    - [Task 0: How many subs?](#task-0-how-many-subs)
    - [Task 1: Top Ten](#task-1-top-ten)
    - [Task 2: Recurse it!](#task-2-recurse-it)
3. [Getting Started](#getting-started)
4. [Usage](#usage)
5. [Requirements](#requirements)
6. [License](#license)

## Project Description

This project involves using the Reddit API to perform various tasks, including querying the number of subscribers for a subreddit, retrieving the titles of the top posts, and recursively fetching all hot articles for a given subreddit. Each task has specific requirements and objectives aimed at improving API usage and Python scripting skills.

## Tasks

### Task 0: How many subs?

Write a function that queries the Reddit API and returns the number of subscribers for a given subreddit. If the subreddit is invalid, the function returns 0.

### Task 1: Top Ten

Write a function that queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit. If the subreddit is invalid, it prints "None."

### Task 2: Recurse it!

Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found, the function returns None. Properly handle pagination to retrieve all hot articles for the subreddit.

## Getting Started

To get started with this project, make sure you have the following requirements in place:

- Python 3.4.3 or higher
- Ubuntu 20.04 LTS or a compatible environment
- Required Python libraries (e.g., requests)

## Usage

You can run each of the project tasks using the provided Python scripts:

- `0-main.py` for Task 0
- `1-main.py` for Task 1
- `2-main.py` for Task 2

For example, to run Task 0, use the following command:

```bash
python3 0-main.py [subreddit_name]
