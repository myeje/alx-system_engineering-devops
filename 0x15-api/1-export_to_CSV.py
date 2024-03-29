#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    idUrl = "https://jsonplaceholder.typicode.com/"
    req = requests.get(idUrl + "todos", params={"userId": sys.argv[1]}).json()
    employeeId = requests.get(idUrl + "users/{}".format(sys.argv[1])).json()
    user = employeeId.get("user")

    with open("{}.csv".format(sys.argv[1]), "w", newline="") as file:
        output = csv.writer(file, quoting=csv.QUOTE_ALL)
        [output.writerow(
            [sys.argv[1], user, tsk.get("completed"), tsk.get("title")]
         ) for tsk in req]
