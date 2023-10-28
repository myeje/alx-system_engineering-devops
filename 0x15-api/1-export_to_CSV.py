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
	
	with open('your_file.csv', 'w', newline='') as file:
		f = csv.writer(f, quoting=csv.QUOTE_ALL)
		for tsk in req:
			row = [sys.argv[1], user, tsk.get("completed"), tsk.get("title")]
			f.writerow(row)
