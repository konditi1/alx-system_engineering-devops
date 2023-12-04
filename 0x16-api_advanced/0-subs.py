#!/usr/bin/python3
""" Retrieves the number of subscribers for a given subreddit.
"""
import requests
""" Retrieves the number of subscribers for a given subreddit.
"""


def number_of_subscribers(subreddit):
    """
     Retrieves the number of subscribers for a given subreddit.

    :param subreddit: The name of the subreddit.
    :return:  The number of subscribers, or 0 if the subreddit doesn't exist.
    """
    # Reddit API endpoint for getting subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Custom User Agent'}

    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the number of subscribers from the response
        subscribers = data['data']['subscribers']

        return subscribers
    elif response.status_code == 404:
        # Subreddit not found, return 0
        return 0
    else:
        # Other error, print the status code and return 0
        print(f"Error: {response.status_code}")
        return 0
