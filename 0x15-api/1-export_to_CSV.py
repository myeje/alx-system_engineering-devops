#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import requests
import sys
import csv

if __name__ == "__main__":
    idUrl = "https://jsonplaceholder.typicode.com/"
    req = requests.get(idUrl + "todos", params={"userId": sys.argv[1]}).json()
    employeeId = requests.get(idUrl + "users/{}".format(sys.argv[1])).json()
    user = employeeId.get("user")

    task = [pop.get("title") for pop in req if pop.get("completed") is True]
    with open('{}.csv'.format(sys.argv[1]), 'w') as f:
        for tsk in task:
            f.write('"{}","{}","{}","{}"\n'
                       .format(sys.argv[1], user, tsk.get('completed'),
                               tsk.get('title')))
