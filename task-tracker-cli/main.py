import argparse
from task_tracker_crud import TaskStatus, TaskTracker


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

    args = parser.parse_args()

    app = TaskTracker()

    if args.command == "add":
        app.add_task(args.description, TaskStatus(args.status))
    elif args.command == "update":
        app.update_task(args.task_id, args.description)
    elif args.command == "delete":
        app.delete_task(args.task_id)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
