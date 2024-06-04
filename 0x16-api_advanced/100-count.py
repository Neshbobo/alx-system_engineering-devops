#!/usr/bin/python3

import requests
import sys

def count_words(subreddit, word_list, after=None, word_count={}):
            url = f"https://www.reddit.com/r/{subreddit}/hot.json"
                headers = {"User-Agent": "MyUserAgent"}
                    params = {"after": after, "limit": 100}
                        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
                            if response.status_code == 200:
                                            data = response.json()["data"]
                                                    for child in data["children"]:
                                                                        title = child["data"]["title"].lower()
                                                                                    for word in word_list:
                                                                                                            word = word.lower()
                                                                                                                            if word in title:
                                                                                                                                                        word_count[word] = word_count.get(word, 0) + title.count(word)
                                                                                                                                                                if data["after"]:
                                                                                                                                                                                    count_words(subreddit, word_list, data["after"], word_count)
                                                                                                                                                                else:
                                                                                                                                                                                    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                                                                                                                                                                                                for word, count in sorted_words:
                                                                                                                                                                                                                        if count > 0:
                                                                                                                                                                                                                                                    print(f"{word}: {count}")
                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                        print("")

                                                                                                                                                                                                                                        if __name__ == '__main__':
                                                                                                                                                                                                                                                    if len(sys.argv) < 3:
                                                                                                                                                                                                                                                                    print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
                                                                                                                                                                                                                                                                            print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                    count_words(sys.argv[1], [x for x in sys.argv[2].split()])
