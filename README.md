# Task Manager

The Task Manager is a Python-based CLI application that helps you manage and track tasks efficiently. It includes features for adding, removing, updating, and listing tasks. The project architecture is modular and supports both command-line and future GUI integrations.

## Features

- Add, remove, update, and list tasks
- Modular design for easy extension
- Built-in tests to ensure integrity

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sumanengg/task_manager.git
   cd task_manager
   ```

2. Set up the Python environment (using virtualenv or conda):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application using the CLI:

```bash
python -m task_manager.cli
```

For more details on commands and options, run:

```bash
python -m task_manager.cli --help
```

## Running Tests

Tests are located in the `test/` directory. Run tests using:

```bash
pytest
```

## Project Structure

```
├── task_manager/
│   ├── __init__.py
│   ├── cli.py
│   ├── main.py
│   ├── manager.py
│   ├── models.py
│   └── storage.py
├── test/
│   ├── __init__.py
│   └── test_manager.py
├── setup.py
└── README.md
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.