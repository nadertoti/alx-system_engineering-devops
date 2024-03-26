#!/usr/bin/python3
"""
Displays the completed tasks of an employee identified by their unique ID.

This script takes an employee ID as input and retrieves the associated user details
along with their to-do list from a designated JSONPlaceholder API endpoint.
It subsequently presents the tasks accomplished by the employee.
"""

import requests
import sys


if __name__ == "__main__":
    # Define the base URL for the JSONPlaceholder API
    api_url = "https://jsonplaceholder.typicode.com/"

    # Obtain employee information based on the provided employee ID
    employee_id = sys.argv[1]
    user_info = requests.get(api_url + "users/{}".format(employee_id)).json()

    # Fetch the to-do list corresponding to the employee ID
    todo_params = {"userId": employee_id}
    user_todos = requests.get(api_url + "todos", todo_params).json()

    # Extract completed tasks and determine their count
    completed_tasks = [task.get("title") for task in user_todos if task.get("completed")]

    # Print the employee's name and the total number of completed tasks
    print("Tasks completed by {} ({} out of {}):".format(
        user_info.get("name"), len(completed_tasks), len(user_todos)))

    # Display completed tasks individually with appropriate indentation
    [print("\t{}".format(task)) for task in completed_tasks]
