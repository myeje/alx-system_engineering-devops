#!/usr/bin/python3
"""Using this REST API, for a given employee ID, returns information"""
import requests
import sys

if __name__ == "__main__":
    id_url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(id_url + "users/{}".format(sys.argv[1])).json()
    t = requests.get(id_url + "todos", params={"userId": sys.argv[1]}).json()

    dic = [pop.get("title") for pop in t if pop.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(dic), len(t)))
    [print("\t {}".format(c)) for c in dic]