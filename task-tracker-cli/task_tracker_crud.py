import json
import threading
import os
from enum import Enum
from datetime import datetime


class TaskStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"


class TaskTracker:
    # singleton instance
    _instance = None
    # thread lock for safety
    _lock = threading.Lock()
    DATA_FILE = "tasks.json"

    def __new__(cls, *args, **kwargs):
        """Ensure only one instance exists - thread safe"""
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(TaskTracker, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):  # Run only once per instance
            print("🔹 Running __init__")
            self._initialized = True
            self._ensure_file()

    def _ensure_file(self):
        """Create the file if it does not exist or is corrupted."""
        if not os.path.exists(self.DATA_FILE):
            self._save_data({"tasks": []})
        else:
            try:
                self._load_data()
            except (json.JSONDecodeError, FileNotFoundError):
                print("⚠️  Corrupted or missing file. Creating a new one.")
                self._save_data({"tasks": []})

    def _save_data(self, data):
        """Save data to JSON file."""
        with open(self.DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def _load_data(self):
        """Read data from JSON file"""
        try:
            with open(self.DATA_FILE, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def add_task(self, description, status=TaskStatus.TODO):
        """Add a new task to the task list."""
        if not isinstance(status, TaskStatus):  # ✅ Ensure valid status
            raise ValueError("Invalid status. Use TaskStatus Enum.")

        data = self._load_data()
        new_id = len(data["tasks"]) + 1
        timestamp = datetime.now().isoformat()

        new_task = {
            "id": new_id,
            "description": description,
            "status": status.value,  # ✅ Store as string
            "createdAt": timestamp,
            "updatedAt": timestamp,
        }

        data["tasks"].append(new_task)
        self._save_data(data)

        print(f"✅ Task added: {new_task}")

    def update_task(self, task_id, description):
        """Update a task in the task list"""

        data = self._load_data()

        if "tasks" not in data or not isinstance(data["tasks"], list):
            print("⚠️ No tasks found.")
            return

        timestamp = datetime.now().isoformat()

        # find and update the task
        updated = False
        for task in data["tasks"]:
            if task["id"] == task_id:
                task.update(
                    {
                        "description": description,
                        "updatedAt": timestamp,
                    }
                )
                updated = True
                break  # Exit loop after updating the task

        if updated:
            self._save_data(data)
            print(f"Task {task_id} updated successfully.")
        else:
            print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        """Delete a task in the task list"""

        data = self._load_data()

        if "tasks" not in data or not isinstance(data["tasks"], list):
            print("⚠️ No tasks found.")
            return

        new_tasks = [task for task in data["tasks"] if task["id"] != task_id]

        if len(new_tasks) == len(data["tasks"]):
            print(f"Task with ID {task_id} not found.")
            return

        data["tasks"] = new_tasks
        self._save_data(data)

        print(f"Task {task_id} removed successfully.")
