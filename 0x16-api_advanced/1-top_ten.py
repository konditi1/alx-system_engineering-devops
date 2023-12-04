#!/usr/bin/python3
"""
Module for top_ten function
"""
import requests


def top_ten(subreddit):
    """
    Retrieves the titles of the top 10 hot posts in a given subreddit.

    :param subreddit: The name of the subreddit.
    :return: None
    """
    # Reddit API endpoint for getting hot posts in a subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Custom User Agent'}

    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if the 'children' key is present
        if 'children' in data['data']:
            # Iterate over the first 10 posts and print their titles
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print("No posts found.")
    elif response.status_code == 404:
        # Subreddit not found, print None
        print(None)
    else:
        # Other error, print the status code and print None
        print(f"Error: {response.status_code}")
        print(None)
