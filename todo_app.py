#!/usr/bin/env python3
"""
Todo Console Application - Phase I Implementation

A single-file Python console application that allows users to manage tasks in memory.
Features include adding, viewing, updating, deleting, and marking tasks as complete/incomplete.
All data is stored in memory during runtime with no persistence beyond the application session.
"""

from typing import List, Dict, Optional, Union


class TodoApp:
    """Main Todo Application class that manages tasks in memory."""

    def __init__(self):
        """Initialize the todo application with an empty task list."""
        self.tasks: List[Dict] = []
        self.next_id: int = 1

    def _generate_id(self) -> int:
        """
        Generate a unique sequential ID for new tasks.

        Returns:
            The next available task ID
        """
        new_id = self.next_id
        self.next_id += 1
        return new_id

    def _validate_description(self, description: str) -> bool:
        """
        Validate that a task description is not empty or contains only whitespace.

        Args:
            description: The task description to validate

        Returns:
            True if description is valid, False otherwise
        """
        return description.strip() != ""

    def _task_exists(self, task_id: int) -> bool:
        """
        Check if a task with the given ID exists in the task list.

        Args:
            task_id: The ID to check for

        Returns:
            True if task exists, False otherwise
        """
        return any(task['id'] == task_id for task in self.tasks)

    def _find_task_index(self, task_id: int) -> Optional[int]:
        """
        Find the index of a task with the given ID.

        Args:
            task_id: The ID of the task to find

        Returns:
            Index of the task if found, None otherwise
        """
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                return i
        return None

    def add_task(self, description: str) -> int:
        """
        Add a new task to the list.

        Args:
            description: The task description (non-empty)

        Returns:
            The ID of the newly created task

        Raises:
            ValueError: If description is empty or contains only whitespace
        """
        if not self._validate_description(description):
            raise ValueError("Task description cannot be empty or contain only whitespace")

        task_id = self._generate_id()
        task = {
            "id": task_id,
            "description": description.strip(),
            "completed": False
        }
        self.tasks.append(task)
        return task_id

    def view_tasks(self) -> List[Dict]:
        """
        Get all tasks in the list.

        Returns:
            List of task dictionaries with id, description, and completed status
        """
        return self.tasks.copy()

    def update_task(self, task_id: int, new_description: str) -> bool:
        """
        Update the description of an existing task.

        Args:
            task_id: The ID of the task to update
            new_description: The new description for the task

        Returns:
            True if task was updated, False if task_id not found
        """
        if not self._validate_description(new_description):
            raise ValueError("Task description cannot be empty or contain only whitespace")

        task_index = self._find_task_index(task_id)
        if task_index is None:
            return False

        self.tasks[task_index]['description'] = new_description.strip()
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task from the list.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if task was deleted, False if task_id not found
        """
        task_index = self._find_task_index(task_id)
        if task_index is None:
            return False

        del self.tasks[task_index]
        return True

    def mark_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id: The ID of the task to mark complete

        Returns:
            True if task was marked complete, False if task_id not found
        """
        task_index = self._find_task_index(task_id)
        if task_index is None:
            return False

        self.tasks[task_index]['completed'] = True
        return True

    def mark_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.

        Args:
            task_id: The ID of the task to mark incomplete

        Returns:
            True if task was marked incomplete, False if task_id not found
        """
        task_index = self._find_task_index(task_id)
        if task_index is None:
            return False

        self.tasks[task_index]['completed'] = False
        return True


def display_menu():
    """Display the main menu options to the user."""
    print("\nTodo Application")
    print("1. Add Task")
    print("2. View Task List")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete")
    print("6. Mark Task Incomplete")
    print("7. Exit")


def get_user_choice() -> int:
    """
    Get and validate user menu choice.

    Returns:
        Valid menu option number (1-7)
    """
    while True:
        try:
            choice = int(input("Choose an option: ").strip())
            if 1 <= choice <= 7:
                return choice
            else:
                print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Please enter a valid number.")


def get_task_description() -> str:
    """
    Get task description from user input.

    Returns:
        User-entered task description
    """
    return input("Enter task description: ").strip()


def get_task_id() -> int:
    """
    Get task ID from user input.

    Returns:
        Valid task ID as integer
    """
    while True:
        try:
            task_id = int(input("Enter task ID: ").strip())
            if task_id > 0:
                return task_id
            else:
                print("Please enter a positive number for the task ID.")
        except ValueError:
            print("Please enter a valid number for the task ID.")


def display_error(message: str):
    """
    Display an error message to the user.

    Args:
        message: The error message to display
    """
    print(f"Error: {message}")


def display_tasks(tasks: List[Dict]):
    """
    Display the list of tasks in a formatted table.

    Args:
        tasks: List of task dictionaries to display
    """
    if not tasks:
        print("No tasks in the list.")
        return

    print(f"{'ID':<4} | {'Description':<30} | {'Status':<12}")
    print("-" * 50)
    for task in tasks:
        status = "Complete" if task['completed'] else "Incomplete"
        desc = task['description'][:27] + "..." if len(task['description']) > 30 else task['description']
        print(f"{task['id']:<4} | {desc:<30} | {status:<12}")


def handle_add_task(app: TodoApp):
    """Handle the Add Task menu option."""
    try:
        description = get_task_description()
        task_id = app.add_task(description)
        print(f"Task added successfully with ID {task_id}.")
    except ValueError as e:
        display_error(str(e))


def handle_view_tasks(app: TodoApp):
    """Handle the View Task List menu option."""
    tasks = app.view_tasks()
    display_tasks(tasks)


def handle_update_task(app: TodoApp):
    """Handle the Update Task menu option."""
    task_id = get_task_id()
    if not app._task_exists(task_id):
        display_error("Task ID not found.")
        return

    try:
        new_description = get_task_description()
        if app.update_task(task_id, new_description):
            print(f"Task {task_id} updated successfully.")
        else:
            display_error("Task ID not found.")
    except ValueError as e:
        display_error(str(e))


def handle_delete_task(app: TodoApp):
    """Handle the Delete Task menu option."""
    task_id = get_task_id()
    if app.delete_task(task_id):
        print(f"Task {task_id} deleted successfully.")
    else:
        display_error("Task ID not found.")


def handle_mark_complete(app: TodoApp):
    """Handle the Mark Task Complete menu option."""
    task_id = get_task_id()
    if app.mark_complete(task_id):
        print(f"Task {task_id} marked as complete.")
    else:
        display_error("Task ID not found.")


def handle_mark_incomplete(app: TodoApp):
    """Handle the Mark Task Incomplete menu option."""
    task_id = get_task_id()
    if app.mark_incomplete(task_id):
        print(f"Task {task_id} marked as incomplete.")
    else:
        display_error("Task ID not found.")


def main():
    """Main function to run the Todo application."""
    app = TodoApp()

    print("Welcome to the Todo Application!")

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            handle_add_task(app)
        elif choice == 2:
            handle_view_tasks(app)
        elif choice == 3:
            handle_update_task(app)
        elif choice == 4:
            handle_delete_task(app)
        elif choice == 5:
            handle_mark_complete(app)
        elif choice == 6:
            handle_mark_incomplete(app)
        elif choice == 7:
            print("Thank you for using the Todo Application. Goodbye!")
            break


if __name__ == "__main__":
    main()