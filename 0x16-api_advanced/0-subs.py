#!/usr/bin/python3
"""function that queries the Reddit API and
returns the number of subscribers
(not active users, total subscribers)
for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers"""
    url = 'https://www.reddit.com/r/' + subreddit + "/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows)'}
    res_status = requests.get(url, headers=headers, allow_redirects=False)

    if res_status.status_code == 200:
        return res_status.json()['data']['subscribers']
    else:
        return 0
