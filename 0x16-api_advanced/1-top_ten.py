#!/usr/bin/python3


"""
function that queries the Reddit API,
prints the titles of the first 10 hot posts listed 
for a given subreddit.
"""

# import json
import requests

from sys import argv


def top_ten(subreddit):
    """
    queries reddit api
    """
    # url = "https://www.reddit.com/r/{}/hot/json?limit=10".format(subreddit)
    # headers = {"User-Agent": "Dalvik/2.1.0"}
    # # params = {"limit": 10}
    # response = requests.get(url, headers=headers)
    # if response.status_code == 200:
    #     data = response.json()
    #     posts = data["data"]["children"]
    #     if not posts:
    #         print("None")
    #     else:
    #         for post in posts:
    #             print(post["data"]["title"])
    # else:
    #     print("None")
    user = {"User-Agent": "Lizzie"}
    url = requests.get(
        "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit), headers=user
    ).json()
    try:
        for post in url.get("data").get("children"):
            print(post.get("data").get("title"))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
