#!/usr/bin/python3
"""
Python script that uses the REST API and returns information about a given employee ID
and returns TODO list progress
"""

import requests
import csv
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    with open("{}.csv".format(userId), 'w', newline='') as csvfile:
        task_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            task_writer.writerow([int(userId), user.get('username'),
                                  task.get('completed'),
                                  task.get('title')])
