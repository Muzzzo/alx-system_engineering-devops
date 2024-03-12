#!/usr/bin/python3
"""
parses the title of all hot articles, and prints
a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    parses the titles and keywords
    """
    if counts is None:
        counts = {}
    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    if after:
        url += "?after={}".format(after)
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return
    data = response.json()
    posts = data["data"]["children"]
    for post in posts:
        title = post["data"]["title"].lower()
        for word in word_list:
            word = word.lower()
            if word in title:
                counts[word] = counts.get(word, 0) + title.count(word)
    next_page = data["data"]["after"]
    if next_page:
        return count_words(subreddit, word_list, after=next_page, counts=counts)
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print("{}: {}".format(word, count))

