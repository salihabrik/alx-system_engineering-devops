#!/usr/bin/python3
""""Script that returns a list of all hot articles"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list of all hot articles"""
    after = str(after)
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?after=" + after
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows)'}
    res_status = requests.get(url, headers=headers, allow_redirects=False)

    if res_status.status_code == 200:
        posts = res_status.json()['data']['children']
        for title in posts:
            hot_list.append((title['data']['title']))
        after = res_status.json()['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
