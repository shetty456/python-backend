import argparse
from task_tracker import TaskStatus, TaskTracker


def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # add task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")
    # Normally here we are not intending to pass any other status than TODO
    add_parser.add_argument(
        "--status",
        type=str,
        choices=[status.value for status in TaskStatus],
        default=TaskStatus.TODO.value,
        help="Task status (default: todo)",
    )

    # update task
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("task_id", type=int, help="Task id")
    update_parser.add_argument("description", type=str, help="Task description")

    # delete task
    delete_parser = subparsers.add_parser("delete", help="delete a task")
    delete_parser.add_argument("task_id", type=int, help="Task id")

    # task status updates
    # mark-in-progress
    mark_in_progress_parser = subparsers.add_parser(
        "mark-in-progress", help="mark-in-progress a task"
    )
    mark_in_progress_parser.add_argument("task_id", type=int, help="Task id")

    # mark-done
    mark_done_parser = subparsers.add_parser("mark-done", help="mark-done a task")
    mark_done_parser.add_argument("task_id", type=int, help="Task id")

    # listing of tasks
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "filter", nargs="?", choices=["done", "todo", "in-progress"], help="Filter tasks by status"
    )

    args = parser.parse_args()

    app = TaskTracker()

    if args.command == "add":
        app.add_task(args.description, TaskStatus(args.status))
    elif args.command == "update":
        app.update_task(args.task_id, args.description)
    elif args.command == "delete":
        app.delete_task(args.task_id)
    elif args.command in ["mark-in-progress", "mark-done"]:
        status = (
            TaskStatus.IN_PROGRESS
            if args.command == "mark-in-progress"
            else TaskStatus.DONE
        )
        app.update_task_status(status, args.task_id)
    elif args.command == "list":
        status = (
            TaskStatus.DONE
            if args.filter == "done"
            else (
                TaskStatus.IN_PROGRESS
                if args.filter == "in-progress"
                else TaskStatus.TODO if args.filter == "todo" else None
            )  # Show all tasks if no filter is provided
        )
        app.list_tasks(status)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
