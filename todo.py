import requests

API_URL = "https://jsonplaceholder.typicode.com/todos"

def get_tasks():
    response = requests.get(API_URL)
    tasks = response.json()
    for task in tasks[:5]:
        print(task["id"], "-", task["title"])

def add_task():
    title = input("Enter new task: ")
    data = {
        "title": title,
        "completed": False
    }
    response = requests.post(API_URL, json=data)
    print("Task Added:", response.json())

def update_task():
    task_id = input("Enter task id to update: ")
    data = {
        "completed": True
    }
    response = requests.put(f"{API_URL}/{task_id}", json=data)
    print("Task Updated:", response.json())

def delete_task():
    task_id = input("Enter task id to delete: ")
    response = requests.delete(f"{API_URL}/{task_id}")
    print("Task Deleted")

while True:
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        get_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        break
    else:
        print("Invalid choice")