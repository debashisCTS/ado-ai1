#!/usr/bin/env python3
"""
A simple command-line todo list application that uses JSON for storage.
"""

import argparse
import json
import os
from datetime import datetime
from typing import Dict, List

# Constants
TASKS_FILE = "tasks.json"

class TodoList:
    def __init__(self, tasks_file: str = TASKS_FILE):
        self.tasks_file = tasks_file
        self.tasks = self._load_tasks()

    def _load_tasks(self) -> List[Dict]:
        """Load tasks from JSON file or return empty list if file doesn't exist."""
        if os.path.exists(self.tasks_file):
            with open(self.tasks_file, 'r') as f:
                return json.load(f)
        return []

    def _save_tasks(self) -> None:
        """Save tasks to JSON file."""
        with open(self.tasks_file, 'w') as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, description: str) -> Dict:
        """Add a new task and return it."""
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'done': False,
            'created_at': datetime.now().isoformat(),
            'completed_at': None
        }
        self.tasks.append(task)
        self._save_tasks()
        return task

    def list_tasks(self, show_all: bool = True) -> List[Dict]:
        """List all tasks or only pending ones."""
        if show_all:
            return self.tasks
        return [task for task in self.tasks if not task['done']]

def main():
    parser = argparse.ArgumentParser(description='Todo List CLI')
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Add task command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', help='Task description')

    # List tasks command
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('--all', action='store_true', help='Show all tasks including completed ones')

    args = parser.parse_args()
    todo = TodoList()

    if args.command == 'add':
        task = todo.add_task(args.description)
        print(f"Added task {task['id']}: {task['description']}")
    
    elif args.command == 'list':
        tasks = todo.list_tasks(show_all=args.all)
        if not tasks:
            print("No tasks found!")
            return

        print("\nTasks:")
        print("------")
        for task in tasks:
            status = "✓" if task['done'] else " "
            print(f"[{status}] {task['id']}. {task['description']}")
    
    else:
        parser.print_help()

if __name__ == '__main__':
    main()