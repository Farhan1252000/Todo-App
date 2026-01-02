import pytest
from unittest.mock import patch
from io import StringIO
import sys
import os

# Add the parent directory to the path so we can import todo_app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from todo_app import TodoApp


class TestTodoApp:
    """Test class for the TodoApp functionality."""

    def setup_method(self):
        """Set up a fresh TodoApp instance for each test."""
        self.app = TodoApp()

    def test_add_task_success(self):
        """Test adding a task successfully."""
        task_id = self.app.add_task("Test task")
        assert task_id == 1
        assert len(self.app.tasks) == 1
        assert self.app.tasks[0]['id'] == 1
        assert self.app.tasks[0]['description'] == "Test task"
        assert self.app.tasks[0]['completed'] is False

    def test_add_task_with_whitespace(self):
        """Test adding a task with leading/trailing whitespace."""
        task_id = self.app.add_task("  Test task with spaces  ")
        assert task_id == 1
        assert self.app.tasks[0]['description'] == "Test task with spaces"

    def test_add_task_empty_description(self):
        """Test that adding a task with empty description raises ValueError."""
        with pytest.raises(ValueError):
            self.app.add_task("")

    def test_add_task_whitespace_only(self):
        """Test that adding a task with whitespace-only description raises ValueError."""
        with pytest.raises(ValueError):
            self.app.add_task("   ")

    def test_view_tasks_empty(self):
        """Test viewing tasks when the list is empty."""
        tasks = self.app.view_tasks()
        assert tasks == []

    def test_view_tasks_with_items(self):
        """Test viewing tasks when the list has items."""
        self.app.add_task("First task")
        self.app.add_task("Second task")

        tasks = self.app.view_tasks()
        assert len(tasks) == 2
        assert tasks[0]['description'] == "First task"
        assert tasks[1]['description'] == "Second task"

    def test_update_task_success(self):
        """Test updating a task successfully."""
        self.app.add_task("Original task")
        success = self.app.update_task(1, "Updated task")

        assert success is True
        assert len(self.app.tasks) == 1
        assert self.app.tasks[0]['description'] == "Updated task"

    def test_update_task_invalid_id(self):
        """Test updating a task with an invalid ID."""
        self.app.add_task("Test task")
        success = self.app.update_task(999, "Updated task")

        assert success is False

    def test_update_task_empty_description(self):
        """Test that updating a task with empty description raises ValueError."""
        self.app.add_task("Test task")
        with pytest.raises(ValueError):
            self.app.update_task(1, "")

    def test_update_task_whitespace_only(self):
        """Test that updating a task with whitespace-only description raises ValueError."""
        self.app.add_task("Test task")
        with pytest.raises(ValueError):
            self.app.update_task(1, "   ")

    def test_delete_task_success(self):
        """Test deleting a task successfully."""
        self.app.add_task("Test task")
        initial_count = len(self.app.tasks)

        success = self.app.delete_task(1)

        assert success is True
        assert len(self.app.tasks) == initial_count - 1

    def test_delete_task_invalid_id(self):
        """Test deleting a task with an invalid ID."""
        self.app.add_task("Test task")
        initial_count = len(self.app.tasks)

        success = self.app.delete_task(999)

        assert success is False
        assert len(self.app.tasks) == initial_count

    def test_mark_complete_success(self):
        """Test marking a task as complete."""
        self.app.add_task("Test task")
        success = self.app.mark_complete(1)

        assert success is True
        assert self.app.tasks[0]['completed'] is True

    def test_mark_complete_invalid_id(self):
        """Test marking a task as complete with an invalid ID."""
        self.app.add_task("Test task")
        success = self.app.mark_complete(999)

        assert success is False

    def test_mark_incomplete_success(self):
        """Test marking a task as incomplete."""
        self.app.add_task("Test task")
        self.app.mark_complete(1)  # First mark it complete
        success = self.app.mark_incomplete(1)  # Then mark it incomplete

        assert success is True
        assert self.app.tasks[0]['completed'] is False

    def test_mark_incomplete_invalid_id(self):
        """Test marking a task as incomplete with an invalid ID."""
        self.app.add_task("Test task")
        success = self.app.mark_incomplete(999)

        assert success is False

    def test_id_generation_sequential(self):
        """Test that IDs are generated sequentially."""
        id1 = self.app.add_task("First task")
        id2 = self.app.add_task("Second task")
        id3 = self.app.add_task("Third task")

        assert id1 == 1
        assert id2 == 2
        assert id3 == 3

    def test_task_exists_true(self):
        """Test that _task_exists returns True for existing tasks."""
        self.app.add_task("Test task")
        assert self.app._task_exists(1) is True

    def test_task_exists_false(self):
        """Test that _task_exists returns False for non-existing tasks."""
        self.app.add_task("Test task")
        assert self.app._task_exists(999) is False

    def test_task_exists_empty_list(self):
        """Test that _task_exists returns False when the list is empty."""
        assert self.app._task_exists(1) is False


class TestInputValidation:
    """Test input validation functions."""

    def test_validate_description_valid(self):
        """Test that valid descriptions pass validation."""
        app = TodoApp()
        assert app._validate_description("Valid description") is True
        assert app._validate_description("A") is True
        assert app._validate_description("123") is True

    def test_validate_description_empty(self):
        """Test that empty descriptions fail validation."""
        app = TodoApp()
        assert app._validate_description("") is False

    def test_validate_description_whitespace_only(self):
        """Test that whitespace-only descriptions fail validation."""
        app = TodoApp()
        assert app._validate_description("   ") is False
        assert app._validate_description("\t") is False
        assert app._validate_description("\n") is False
        assert app._validate_description(" \t\n ") is False


def test_app_initialization():
    """Test that TodoApp initializes with empty task list and ID counter."""
    app = TodoApp()
    assert app.tasks == []
    assert app.next_id == 1


if __name__ == "__main__":
    pytest.main([__file__])