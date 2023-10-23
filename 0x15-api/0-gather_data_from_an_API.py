#!/usr/bin/python3
"""
    Retrieve and display the TODO list progress for a given employee.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieve and display the TODO list progress for a given employee.

    Args:
        employee_id (int): ID of employee for whom to retr TODO list progress.

    Returns:
        None
    """
    # Define the URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user information
    response_user = requests.get(user_url)
    user_data = response_user.json()
    employee_name = user_data.get("name")

    # Fetch TODO list information
    response_todo = requests.get(todo_url)
    todo_list = response_todo.json()

    # Calculate progress
    total_tasks = len(todo_list)
    done_tasks = sum(1 for task in todo_list if task["completed"])

    # Display progress
    print_employee = "Employee {} is done with" .format(employee_name)
    print_employee_sec = " tasks({}/{}):" .format(done_tasks, total_tasks)
    print("{}{}".format(print_employee, print_employee_sec))
    for task in todo_list:
        if task["completed"]:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
