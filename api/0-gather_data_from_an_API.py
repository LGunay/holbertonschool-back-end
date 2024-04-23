#!/usr/bin/python3

import requests

if __name__ == '__main__':
    userid = input()
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    data = requests.get(f'https://jsonplaceholder.typicode.com/users/\
                        {userid}').json()['name']
    todos = requests.get(f'https://jsonplaceholder.typicode.com/users/\
                         {userid}/TODOS').json()
    TOTAL_NUMBER_OF_TASKS = len(todos)
    for tasks in todos:
        if tasks['completed']:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(tasks['title'])
    print(f'Employee {data} is done with tasks\
          ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
    for title in TASK_TITLE:
        print("\t "+title)
