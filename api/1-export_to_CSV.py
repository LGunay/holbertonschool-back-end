#!/usr/bin/python3
"""
Starting with API
"""

if __name__ == '__main__':
    import requests
    import sys
    userid = sys.argv[1]
    data = requests\
        .get(f'https://jsonplaceholder.typicode.com/users/{userid}')\
        .json().get('name')
    todos = requests\
        .get(f'https://jsonplaceholder.typicode.com/users/{userid}/todos')\
        .json()
    dat = ''
    for tasks in todos:
        status = tasks.get("completed")
        title = tasks.get("title")
        dat += f'"{userid}","{data}","{status}","{title}"\n'
    with open(f'{userid}.csv', 'w') as f:
        f.write(dat)
