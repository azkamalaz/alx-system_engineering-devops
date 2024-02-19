#!/usr/bin/python3
"""
Python script that uses the REST API and returns information about a given employee ID
and returns TODO list progress
"""

import requests
import json

if __name__ == '__main__':
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        verify=False).json()
    user_dict = {}
    username_dict = {}
    for user in users:
        uid = user.get("id")
        user_dict[uid] = []
        username_dict[uid] = usr.get("username")
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        verify=False).json()
    for task in todo:
        task_dict = {}
        uid = task.get("userId")
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username_dict.get(uid)
        user_dict.get(uid).append(task_dict)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(user_dict, jsonfile)
