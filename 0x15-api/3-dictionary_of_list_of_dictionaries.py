#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests

if __name__ == "__main__":
    idUrl = "https://jsonplaceholder.typicode.com/"
    employeeId = requests.get(idUrl + "users/{}".format(sys.argv[1])).json()

    with open("todo_all_employees.json", "w") as file:
        json.dump({
            tsk.get("id"): [{
                "task": tasks.get("title"),
                "completed": tasks.get("completed"),
                "username": tsk.get("username")
            } for tasks in requests.get(idUrl + "todos",
                                      params={"userId": tsk.get("id")}).json()]
            for tsk in employeeId}, file)
