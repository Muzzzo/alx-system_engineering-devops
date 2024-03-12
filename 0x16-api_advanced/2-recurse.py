#!/usr/bin/python3

"""
function that queries the Reddit API,
returns a list containing the titles of all hot articles
for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    retrieve title fo hot articles on a given sub
    """

    headers = {"User-Agent": "RedditClient/1.0"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += f"?after={after}".format(after)
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    data = response.json()
    posts = data.get("data", {}).get("children", [])
    titles = [post["data"]["title"] for post in posts]
    hot_list.extend(titles)
    next_page = data["data"]["after"]
    if next_page:
        return recurse(subreddit, hot_list, next_page)
    else:
        return hot_list
