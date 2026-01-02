# Data Model: Phase I Todo Console Application

## Task Entity

**Representation**: Dictionary with the following fields:
- `id`: Integer - Unique identifier for the task (auto-incremented)
- `description`: String - The task description (non-empty, trimmed)
- `completed`: Boolean - Completion status (default: False)

**Validation rules**:
- ID must be a positive integer
- Description must not be empty or contain only whitespace after trimming
- Completed status must be a boolean value

**Example**:
```python
{
    "id": 1,
    "description": "Complete the project",
    "completed": False
}
```

## Task List Entity

**Representation**: Python list containing Task entities
- Maintains order of task creation
- Provides O(1) access to tasks by index when needed
- Supports all required operations (add, remove, update, iterate)

**Constraints**:
- All IDs must be unique within the list
- IDs must be sequential starting from 1
- No duplicate tasks allowed

## State Transitions

**Task completion states**:
- Incomplete (completed: False) → Complete (completed: True)
- Complete (completed: True) → Incomplete (completed: False)

**Operations that modify state**:
- Add task: Creates new task with ID and sets completed to False
- Update task: Modifies task description
- Mark complete/incomplete: Changes completed status
- Delete task: Removes task from list