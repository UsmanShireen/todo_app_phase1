"""
Unit tests for TaskService.

This file tests the TaskService class functionality.
"""
from src.models.task import Task
from src.services.task_service import TaskService


def test_task_service_initialization():
    """Test initializing TaskService."""
    service = TaskService()
    assert service.tasks == {}
    assert service.next_id == 1


def test_add_task():
    """Test adding a task."""
    service = TaskService()
    task = service.add_task("Test Title", "Test Description")

    assert isinstance(task, Task)
    assert task.id == 1
    assert task.title == "Test Title"
    assert task.description == "Test Description"
    assert task.completed is False

    # Check that the task is stored
    assert 1 in service.tasks
    assert service.tasks[1] == task

    # Check that next_id was incremented
    assert service.next_id == 2


def test_add_task_default_description():
    """Test adding a task with default description."""
    service = TaskService()
    task = service.add_task("Test Title")

    assert task.title == "Test Title"
    assert task.description == ""


def test_get_task_by_id():
    """Test getting a task by ID."""
    service = TaskService()
    added_task = service.add_task("Test Title")

    retrieved_task = service.get_task_by_id(1)
    assert retrieved_task == added_task
    assert retrieved_task.title == "Test Title"

    # Test getting non-existent task
    assert service.get_task_by_id(999) is None


def test_get_all_tasks():
    """Test getting all tasks."""
    service = TaskService()

    # Initially empty
    assert service.get_all_tasks() == []

    # Add some tasks
    task1 = service.add_task("Task 1")
    task2 = service.add_task("Task 2")

    all_tasks = service.get_all_tasks()
    assert len(all_tasks) == 2
    assert task1 in all_tasks
    assert task2 in all_tasks


def test_update_task():
    """Test updating a task."""
    service = TaskService()
    original_task = service.add_task("Original Title", "Original Description")

    # Update the task
    updated_task = service.update_task(1, "New Title", "New Description", True)

    assert updated_task == original_task  # Same object
    assert updated_task.title == "New Title"
    assert updated_task.description == "New Description"
    assert updated_task.completed is True

    # Verify the changes are reflected in storage
    stored_task = service.get_task_by_id(1)
    assert stored_task.title == "New Title"


def test_update_task_partial():
    """Test updating a task partially."""
    service = TaskService()
    original_task = service.add_task("Original Title", "Original Description", True)

    # Update only the title
    updated_task = service.update_task(1, title="New Title")

    assert updated_task.title == "New Title"
    assert updated_task.description == "Original Description"  # Unchanged
    assert updated_task.completed is True  # Unchanged


def test_update_nonexistent_task():
    """Test updating a non-existent task."""
    service = TaskService()

    result = service.update_task(999, "New Title")
    assert result is None


def test_delete_task():
    """Test deleting a task."""
    service = TaskService()
    service.add_task("Test Title")

    # Verify task exists
    assert service.get_task_by_id(1) is not None

    # Delete the task
    result = service.delete_task(1)
    assert result is True

    # Verify task no longer exists
    assert service.get_task_by_id(1) is None

    # Try to delete non-existent task
    result = service.delete_task(999)
    assert result is False


def test_mark_task_complete():
    """Test marking a task as complete/incomplete."""
    service = TaskService()
    task = service.add_task("Test Title")

    # Initially incomplete
    assert task.completed is False

    # Mark as complete
    updated_task = service.mark_task_complete(1, True)
    assert updated_task.completed is True

    # Mark as incomplete
    updated_task = service.mark_task_complete(1, False)
    assert updated_task.completed is False


def test_mark_nonexistent_task():
    """Test marking a non-existent task."""
    service = TaskService()

    result = service.mark_task_complete(999, True)
    assert result is None


def test_get_next_id():
    """Test getting the next available ID."""
    service = TaskService()

    assert service.get_next_id() == 1

    service.add_task("Test Title")
    assert service.get_next_id() == 2

    service.add_task("Another Title")
    assert service.get_next_id() == 3