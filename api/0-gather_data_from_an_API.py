#!/usr/bin/python3

import requests
import sys

if __name__ == '__main__':
    userid = sys.argv[1]
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    data = requests\
        .get(f'https://jsonplaceholder.typicode.com/users/{userid}')\
        .json()['name']
    todos = requests\
        .get(f'https://jsonplaceholder.typicode.com/users/{userid}/todos')\
        .json()
    TOTAL_NUMBER_OF_TASKS = len(todos)
    for tasks in todos:
        if tasks['completed']:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(tasks['title'])
    print(f'Employee {data} is done with tasks'
          f'({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
    for title in TASK_TITLE:
        print(f'\t {title}')
