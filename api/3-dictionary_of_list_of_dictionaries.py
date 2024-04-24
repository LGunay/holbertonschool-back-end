#!/usr/bin/python3
"""
Starting with API
"""

if __name__ == '__main__':
    import requests
    import json
    dicti_list = []
    dicti2 = {}
    with open(f"todo_all_employees.json", "w") as f:
        user_count = len(requests.get(f'https://jsonplaceholder.typicode.com\
                                      /users/').json())
        for userid in range(1, user_count+1):
            data = requests.get(f'https://jsonplaceholder.typicode.com\
                                /users/{userid}').json().get('username')

            todos = requests\
                .get(f'https://jsonplaceholder.typicode.com/users/{userid}\
                     /todos').json()
            for tasks in todos:
                status = tasks.get("completed")
                title = tasks.get("title")
                dicti = {
                    "task": title,
                    "completed": status,
                    "username": data
                }
                dicti_list.append(dicti)
            dicti2[userid] = dicti_list
            dicti_list = []
        f.write(json.dumps(dicti2))
