#!/usr/bin/python3

"""
 a function that returns the number of subscribers 
 (not active users, total subscribers) 
 for a given subreddit. 
 If an invalid subreddit is given, 
 the function should return 0.
"""
import requests

# from sys import argv


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    # if response.status_code == 404:
    #     return 0
    # results = response.json().get("data")
    # return results.get("subscribers")
    print("Requesting URL:", url)
    print("Headers:", headers)
    print("Response status code:", response.status_code)
    print("Response content:", response.text)
    if response.status_code == 404:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        print("Number of subscribers:", subscribers)
        return subscribers
    else:
        print("Error occurred. Returning 0 subscribers.")
        return 0

