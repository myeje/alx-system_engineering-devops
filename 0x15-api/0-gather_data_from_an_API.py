#!/usr/bin/python3
"""
Python script that uses
REST API for a given employeeId ID and returns info
"""
import requests
import sys

if __name__ == "__main__":
    idUrl = "https://jsonplaceholder.typicode.com/"
    req = requests.get(idUrl + "todos", params={"userId": sys.argv[1]}).json()
    employeeId = requests.get(idUrl + "users/{}".format(sys.argv[1])).json()

    task = [pop.get("title") for pop in req if pop.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        employeeId.get("name"), len(task), len(req)))
    [print("\t {}".format(c)) for c in task]
