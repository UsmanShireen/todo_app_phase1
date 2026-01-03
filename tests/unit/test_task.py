"""
Unit tests for Task model.

This file tests the Task class functionality.
"""
import pytest
from src.models.task import Task


def test_task_creation():
    """Test creating a basic task."""
    task = Task(1, "Test Title", "Test Description", False)
    assert task.id == 1
    assert task.title == "Test Title"
    assert task.description == "Test Description"
    assert task.completed is False


def test_task_creation_defaults():
    """Test creating a task with default values."""
    task = Task(1, "Test Title")
    assert task.id == 1
    assert task.title == "Test Title"
    assert task.description == ""
    assert task.completed is False


def test_task_str_representation():
    """Test string representation of task."""
    task = Task(1, "Test Title", "Test Description", False)
    str_repr = str(task)
    assert "○" in str_repr  # Not completed
    assert "1." in str_repr
    assert "Test Title" in str_repr

    task.completed = True
    str_repr_completed = str(task)
    assert "✓" in str_repr_completed  # Completed


def test_task_repr_representation():
    """Test developer representation of task."""
    task = Task(1, "Test Title", "Test Description", False)
    repr_str = repr(task)
    assert "Task(id=1" in repr_str
    assert "title='Test Title'" in repr_str
    assert "description='Test Description'" in repr_str
    assert "completed=False" in repr_str


def test_task_to_dict():
    """Test converting task to dictionary."""
    task = Task(1, "Test Title", "Test Description", True)
    task_dict = task.to_dict()
    assert task_dict["id"] == 1
    assert task_dict["title"] == "Test Title"
    assert task_dict["description"] == "Test Description"
    assert task_dict["completed"] is True


def test_task_update():
    """Test updating task attributes."""
    task = Task(1, "Original Title", "Original Description", False)

    # Update all attributes
    task.update("New Title", "New Description", True)

    assert task.title == "New Title"
    assert task.description == "New Description"
    assert task.completed is True


def test_task_update_partial():
    """Test updating task attributes partially."""
    task = Task(1, "Original Title", "Original Description", False)

    # Update only title
    task.update(title="New Title")

    assert task.title == "New Title"
    assert task.description == "Original Description"  # Unchanged
    assert task.completed is False  # Unchanged


def test_task_invalid_id():
    """Test creating task with invalid ID."""
    with pytest.raises(ValueError):
        Task("invalid", "Test Title")


def test_task_invalid_title():
    """Test creating task with invalid title."""
    with pytest.raises(ValueError):
        Task(1, "")  # Empty title

    with pytest.raises(ValueError):
        Task(1, "   ")  # Whitespace only title


def test_task_invalid_completed():
    """Test creating task with invalid completed value."""
    with pytest.raises(ValueError):
        Task(1, "Test Title", "Test Description", "invalid")