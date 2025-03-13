# Task Tracker CLI

## Overview
Task Tracker CLI is a simple command-line tool for managing tasks in a to-do list. Users can add, update, delete, and track tasks using a JSON file as the backend storage. This project is built using barebones Python with no external dependencies.

## Features
- **Task Management**
  - Add a Task: `task-cli add "Buy groceries"`
  - Update a Task: `task-cli update 1 "Buy groceries and cook dinner"`
  - Delete a Task: `task-cli delete 1`
- **Task Status Updates**
  - Mark as In Progress: `task-cli mark-in-progress 1`
  - Mark as Done: `task-cli mark-done 1`
- **Task Listing**
  - List all tasks: `task-cli list`
  - List completed tasks: `task-cli list done`
  - List pending tasks: `task-cli list todo`
  - List tasks in progress: `task-cli list in-progress`

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/shetty456/python-backend.git
   cd python-backend/task-tracker-cli
   ```
2. Ensure you have Python installed (Python 3 recommended).
3. Run the CLI tool using the following command:
   ```sh
   python main.py
   ```

## Task Data Structure
Tasks are stored in a JSON file (`tasks.json`) with the following format:
```json
{
    "tasks": [
        {
            "id": 1,
            "description": "Buy groceries",
            "status": "todo",
            "createdAt": "2025-03-12T08:00:00",
            "updatedAt": "2025-03-12T08:00:00"
        }
    ]
}
```

## Usage
### Adding a Task
```sh
python main.py add "Buy groceries"
```
### Updating a Task
```sh
python main.py update 1 "Buy groceries and cook dinner"
```
### Deleting a Task
```sh
python main.py delete 1
```
### Changing Task Status
```sh
python main.py mark-in-progress 1
python main.py mark-done 1
```
### Listing Tasks
```sh
python main.py list
python main.py list done
python main.py list todo
python main.py list in-progress
```

## Technical Details
- **Programming Language:** Python (No external dependencies)
- **Storage:** JSON file (`tasks.json`)
- **Command Handling:** `argparse`
- **Error Handling:** Graceful handling of missing tasks, invalid inputs, and corrupted JSON files

## License
This project is licensed under the MIT License.

## Author
Sunil Hanamshetty

