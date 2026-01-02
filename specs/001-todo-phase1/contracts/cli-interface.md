# CLI Interface Contract: Todo Console Application

## Core Application Interface

### Main Application Class
```python
class TodoApp:
    def __init__(self):
        """Initialize the todo application with an empty task list"""

    def run(self):
        """Start the main application loop"""

    def add_task(self, description: str) -> int:
        """
        Add a new task to the list
        Args:
            description: The task description (non-empty)
        Returns:
            The ID of the newly created task
        Raises:
            ValueError: If description is empty or contains only whitespace
        """

    def view_tasks(self) -> list:
        """
        Get all tasks in the list
        Returns:
            List of task dictionaries with id, description, and completed status
        """

    def update_task(self, task_id: int, new_description: str) -> bool:
        """
        Update the description of an existing task
        Args:
            task_id: The ID of the task to update
            new_description: The new description for the task
        Returns:
            True if task was updated, False if task_id not found
        """

    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task from the list
        Args:
            task_id: The ID of the task to delete
        Returns:
            True if task was deleted, False if task_id not found
        """

    def mark_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete
        Args:
            task_id: The ID of the task to mark complete
        Returns:
            True if task was marked complete, False if task_id not found
        """

    def mark_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete
        Args:
            task_id: The ID of the task to mark incomplete
        Returns:
            True if task was marked incomplete, False if task_id not found
        """
```

## CLI Interface Functions

### Menu Display
```python
def display_menu():
    """Display the main menu options to the user"""
```

### User Input Handlers
```python
def get_user_choice() -> int:
    """
    Get and validate user menu choice
    Returns:
        Valid menu option number (1-7)
    """

def get_task_description() -> str:
    """
    Get task description from user input
    Returns:
        User-entered task description
    """

def get_task_id() -> int:
    """
    Get task ID from user input
    Returns:
        Valid task ID as integer
    """
```