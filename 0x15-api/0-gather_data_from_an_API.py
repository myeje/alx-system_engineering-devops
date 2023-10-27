#!/usr/bin/python3
"""
Python script that uses
REST API for a given employee ID and returns info
"""
import sys
import requests

if __name__ == '__main__':
    employeeInfo = requests.get(id_url + "users/{}".format(sys.argv[1])).json()
    req = requests.get(id_url + "todos", params={"userId": sys.argv[1]}).json()
    idUrl = "https://jsonplaceholder.typicode.com/"
    task = [pop.get("title") for pop in req if pop.get("completed") is True]
    print("employeeInfo {} is done with tasks({}/{}):".format(
		employeeInfo.get("name"), len(task), len(req)))
    [print("\t {}".format(c)) for c in task]