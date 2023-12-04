#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Retrieves the titles of the top 10 hot posts in a given subreddit.

    :param subreddit: The name of the subreddit.
    :param hot_list: The list of hot articles.
    :return: The list of hot articles.
    """
    # Initialize hot_list if not provided
    if hot_list is None:
        hot_list = []
    if hot_list is None:
        hot_list = []

    # Reddit API endpoint for getting hot posts in a subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'

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
            # Iterate over the posts and add their titles to hot_list
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])

            # Check if there are more pages (pagination)
            after = data['data']['after']
            if after is not None:
                # Recursively call the function with the new 'after' parameter
                recurse(subreddit, hot_list)
            else:
                # No more pages, return the accumulated hot_list
                return hot_list
        else:
            # No posts found, return None
            return None
    elif response.status_code == 404:
        # Subreddit not found, return None
        return None
    else:
        # Other error, print the status code and return None
        print(f"Error: {response.status_code}")
        return None
