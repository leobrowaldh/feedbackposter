#!/usr/bin/env python3

import os
import requests

folder = './test'
address = 'http://34.68.103.173/feedback/'

# Iterating through folder:
for filename in os.listdir(folder):
    print('opening {}'.format(filename))
    file = os.path.join(folder, filename)
    # If not folder, populate dictionary:
    if os.path.isfile(file):
        feed_dict = {}
        with open(file) as textfile:
            feed_dict["title"] = textfile.readline().strip()
            feed_dict["name"] = textfile.readline().strip()
            feed_dict["date"] = textfile.readline().strip()
            feed_dict["feedback"] = textfile.read().strip()
    # Posting the dictionary:
    print('posting {}'.format(filename))
    response = requests.post(address, json=feed_dict)
    # Check success and print status code:
    print(response.raise_for_status())
    print('status code: {}'.format(response.status_code))
