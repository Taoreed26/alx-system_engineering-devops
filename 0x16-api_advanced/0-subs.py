#!/usr/bin/python3
'''This module the functions used in working with the Reddit API.
'''
import requests


BASE_URL = 'https://www.reddit.com'
'''This is Reddit's base API URL.
'''


def number_of_subscribers(subreddit):
    '''This retrieves number of the subscribers in a given sub-reddit.
    '''
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }
    res = requests.get(
        '{}/r/{}/about/.json'.format(BASE_URL, subreddit),
        headers=api_headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        return res.json()['data']['subscribers']
    return 0
