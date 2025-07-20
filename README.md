# Task Manager

A simple command-line Task Manager application written in Python. It allows you to create, list, complete, delete, and search tasks. Tasks are managed in-memory and support different types (Simple, Priority, Recurring).

## Features
- Add new tasks (Simple, Priority, Recurring)
- List all tasks
- Mark tasks as completed
- Delete tasks
- Search tasks by keyword
- Singleton TaskManager for consistent state
- In-memory storage for fast access

## Project Structure
```
task_manager/
    cli.py          # Command-line interface for user interaction
    manager.py      # TaskManager class, main logic
    models.py       # Task, TaskType, and related models
    storage.py      # Storage abstraction and in-memory implementation
test/
    test_manager.py # Unit tests for TaskManager
```

## Getting Started
1. **Clone the repository**
2. **(Optional) Create a virtual environment**
3. **Install dependencies** (if any)
4. **Run the CLI**

```sh
python task_manager/cli.py
```

## Usage
- Type `add` to create a new task
- Type `list` to view all tasks
- Type `complete <id>` to mark a task as completed
- Type `delete <id>` to delete a task
- Type `search <keyword>` to search tasks
- Type `help` for help
- Type `quit` or `exit` to exit

## Testing
Run unit tests from the project root:
```sh
python -m test.test_manager
```

## Notes
- All data is stored in memory and will be lost when the program exits.
- Extend `Storage` for persistent storage (e.g., file or database).

## License
