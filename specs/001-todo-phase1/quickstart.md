# Quickstart Guide: Phase I Todo Console Application

## Running the Application

1. Ensure Python 3.8+ is installed on your system
2. Run the application:
   ```bash
   python todo_app.py
   ```

## Available Commands

Once the application starts, you'll see a menu with the following options:

1. **Add Task** - Enter a new task description
2. **View Task List** - Display all tasks with their status
3. **Update Task** - Modify an existing task by ID
4. **Delete Task** - Remove a task by ID
5. **Mark Task Complete** - Change task status to complete
6. **Mark Task Incomplete** - Change task status to incomplete
7. **Exit** - Quit the application

## Example Usage

```
Todo Application
1. Add Task
2. View Task List
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit
Choose an option: 1
Enter task description: Buy groceries
Task added successfully with ID 1.

Choose an option: 2
ID  | Description     | Status
----|-----------------|--------
1   | Buy groceries   | Incomplete

Choose an option: 5
Enter task ID to mark complete: 1
Task 1 marked as complete.
```

## Error Handling

- Invalid task IDs will result in error messages
- Empty task descriptions are not allowed
- Attempting operations on non-existent tasks will show an error