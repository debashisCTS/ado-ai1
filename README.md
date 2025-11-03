# Todo List CLI Application

A simple command-line todo list application built with Python that uses JSON for task storage.

## Features

- Add new tasks with descriptions
- List all tasks or only pending tasks
- JSON-based storage for persistence
- Clean command-line interface using argparse
- Task status tracking (pending/completed)
- Timestamp recording for task creation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/debashisCTS/ado-ai1.git
cd ado-ai1
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The application provides the following commands:

### Add a Task

```bash
python src/todo.py add "Your task description"
```

### List Tasks

List pending tasks:
```bash
python src/todo.py list
```

List all tasks (including completed):
```bash
python src/todo.py list --all
```

## Project Structure

```
ado-ai1/
├── src/
│   └── todo.py      # Main application code
├── tasks.json       # Task storage file
├── requirements.txt # Python dependencies
└── README.md       # This file
```

## Future Enhancements

- Task completion functionality
- Task deletion
- Due dates for tasks
- Task categories/tags
- Task priority levels
- Data backup/export

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

This project is open source and available under the MIT License.