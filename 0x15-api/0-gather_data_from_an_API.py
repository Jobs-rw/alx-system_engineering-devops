#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main":
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    completed = 0
    total = 0
    tasks = []
    response2 = requests.get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    employee = None
    user_id = int(sys.argv[1])

    while employee is None and data2:
        user = data2.pop()
        if user['id'] == user_id:
            employee = user['name']

    while data:
        task = data.pop()
        if task['userId'] == user_id:
            total += 1
            if task['completed']:
                completed += 1
                tasks.append(task['title'])

    print("Employee {} is done with tasks({}/{}):".format(employee, completed, total))

    for task in tasks:
        print("\t {}".format(task))
