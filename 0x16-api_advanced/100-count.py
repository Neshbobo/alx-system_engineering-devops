#!/usr/bin/python3
"""
Function to count words in all hot posts of a given Reddit subreddit.
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
        """
    Recursive function that queries the Reddit API, parses the title of all
        hot articles, and prints a sorted count of given keywords
    """
            if not word_list or word_list == [] or not subreddit:
                        return

                        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
                            headers = {"User-Agent": "Mozilla/5.0"}

                                params = {"limit": 100}
                                    if after:
                                                params["after"] = after

                                                    response = requests.get(url,
