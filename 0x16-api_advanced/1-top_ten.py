#!/usr/bin/python3
"""Reddit API Query Module for Retrieving Hot Posts"""


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts of the specified subreddit.
    If the subreddit is invalid or an error occurs, it returns None."""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in sub_info.json().get("data").get("children")]
