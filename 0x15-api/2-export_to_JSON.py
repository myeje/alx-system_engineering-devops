#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    idUrl = "https://jsonplaceholder.typicode.com/"
    req = requests.get(idUrl + "todos", params={"userId": sys.argv[1]}).json()
    employeeId = requests.get(idUrl + "users/{}".format(sys.argv[1])).json()
    user = employeeId.get("user")

    with open("{}.json".format(sys.argv[1]), "w") as f:
        json.dump({sys.argv[1]: [{
                "task": pop.get("title"),
                "completed": pop.get("completed"),
                "username": user
            } for pop in req]}, f)
