#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    idUrl = "https://jsonplaceholder.typicode.com/"
    req = requests.get(idUrl + "todos", params={"userId": sys.argv[1]}).json()
    employeeId = requests.get(idUrl + "users/{}".format(sys.argv[1])).json()
    user = employeeId.get("user")
    result = {sys.argv[1]: []}

    for tsk in req:
        task = tsk.get("title")
        completed = tsk.get("completed")
        result[sys.argv[1]].append({
            "task": task,
            "completed": completed,
            "username": user
        })

    with open("{}.json".format(sys.argv[1]), "w") as file:
        json.dump(result, file)
