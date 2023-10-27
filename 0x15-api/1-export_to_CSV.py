#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    id_url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(id_url + "users/{}".format(sys.argv[1])).json()
    t = requests.get(id_url + "todos", params={"userId": sys.argv[1]}).json()
    u = employee.get("username")

    with open("{}.csv".format(sys.argv[1]), "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        [w.writerow(
            [sys.argv[1], u, p.get("completed"), p.get("title")]
         ) for p in t]