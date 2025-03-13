import unittest
from unittest.mock import patch
from task_tracker import TaskStatus, TaskTracker
import main  # Import your CLI script


class TestTaskTrackerCLI(unittest.TestCase):
    def setUp(self):
        """Set up a mock TaskTracker instance before each test."""
        self.patcher = patch("main.TaskTracker")  # Mock TaskTracker in main.py
        self.MockTaskTracker = self.patcher.start()
        self.mock_app = self.MockTaskTracker.return_value

    def tearDown(self):
        """Stop the patcher after each test."""
        self.patcher.stop()

    def test_add_task(self):
        """Test adding a task via CLI."""
        with patch("sys.argv", ["main.py", "add", "Test task"]):
            main.main()
            self.mock_app.add_task.assert_called_once_with("Test task", TaskStatus.TODO)

    def test_add_task_with_status(self):
        """Test adding a task with a specified status via CLI."""
        with patch("sys.argv", ["main.py", "add", "Test task", "--status", "in-progress"]):
            main.main()
            self.mock_app.add_task.assert_called_once_with("Test task", TaskStatus.IN_PROGRESS)

    def test_update_task(self):
        """Test updating a task via CLI."""
        with patch("sys.argv", ["main.py", "update", "1", "Updated task"]):
            main.main()
            self.mock_app.update_task.assert_called_once_with(1, "Updated task")

    def test_delete_task(self):
        """Test deleting a task via CLI."""
        with patch("sys.argv", ["main.py", "delete", "1"]):
            main.main()
            self.mock_app.delete_task.assert_called_once_with(1)

    def test_mark_task_in_progress(self):
        """Test marking a task as in-progress via CLI."""
        with patch("sys.argv", ["main.py", "mark-in-progress", "1"]):
            main.main()
            self.mock_app.update_task_status.assert_called_once_with(TaskStatus.IN_PROGRESS, 1)

    def test_mark_task_done(self):
        """Test marking a task as done via CLI."""
        with patch("sys.argv", ["main.py", "mark-done", "1"]):
            main.main()
            self.mock_app.update_task_status.assert_called_once_with(TaskStatus.DONE, 1)

    def test_list_tasks_no_filter(self):
        """Test listing all tasks via CLI."""
        with patch("sys.argv", ["main.py", "list"]):
            main.main()
            self.mock_app.list_tasks.assert_called_once_with(None)

    def test_list_tasks_done(self):
        """Test listing done tasks via CLI."""
        with patch("sys.argv", ["main.py", "list", "done"]):
            main.main()
            self.mock_app.list_tasks.assert_called_once_with(TaskStatus.DONE)

    def test_list_tasks_in_progress(self):
        """Test listing in-progress tasks via CLI."""
        with patch("sys.argv", ["main.py", "list", "in-progress"]):
            main.main()
            self.mock_app.list_tasks.assert_called_once_with(TaskStatus.IN_PROGRESS)

    def test_list_tasks_todo(self):
        """Test listing TODO tasks via CLI."""
        with patch("sys.argv", ["main.py", "list", "todo"]):
            main.main()
            self.mock_app.list_tasks.assert_called_once_with(TaskStatus.TODO)


if __name__ == "__main__":
    unittest.main()
