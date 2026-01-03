#!/usr/bin/env python3
"""
Test script to verify that all intermediate features work correctly.
"""
import sys
import os

# Add the project root to the path to allow imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.models.task import Task
from src.services.task_service import TaskService
from datetime import datetime

def test_task_model():
    """Test Task model with new attributes."""
    print("Testing Task model with new attributes...")

    # Test creating a task with all new attributes
    task = Task(1, "Test task", "Test description", priority="High", tags=["work", "urgent"], due_date=datetime.now())

    assert task.priority == "High"
    assert "work" in task.tags
    assert "urgent" in task.tags
    assert task.due_date is not None

    print("✓ Task model with new attributes works correctly")

    # Test updating task attributes
    task.update(priority="Low", tags=["home", "personal"])
    assert task.priority == "Low"
    assert "home" in task.tags
    assert "personal" in task.tags

    print("✓ Task update with new attributes works correctly")

    # Test has_tag method
    assert task.has_tag("home") == True
    assert task.has_tag("HOME") == True  # Case insensitive
    assert task.has_tag("work") == False

    print("✓ has_tag method works correctly")


def test_task_service():
    """Test TaskService with new functionality."""
    print("\nTesting TaskService with new functionality...")

    service = TaskService()

    # Add tasks with different priorities and tags
    task1 = service.add_task("High priority task", "Description", priority="High", tags=["urgent", "work"])
    task2 = service.add_task("Medium priority task", "Description", priority="Medium", tags=["work"])
    task3 = service.add_task("Low priority task", "Description", priority="Low", tags=["personal"])

    # Test search functionality
    results = service.search_tasks("high")
    assert len(results) == 1
    assert results[0].title == "High priority task"

    results = service.search_tasks("task")
    assert len(results) == 3

    print("✓ Search functionality works correctly")

    # Test filter functionality
    completed_tasks = service.filter_tasks(status=True)
    assert len(completed_tasks) == 0  # No completed tasks yet

    pending_tasks = service.filter_tasks(status=False)
    assert len(pending_tasks) == 3  # All tasks are pending

    high_priority_tasks = service.filter_tasks(priority="High")
    assert len(high_priority_tasks) == 1
    assert high_priority_tasks[0].priority == "High"

    work_tasks = service.filter_tasks(tag="work")
    assert len(work_tasks) == 2  # task1 and task2 have "work" tag

    print("✓ Filter functionality works correctly")

    # Test sort functionality
    sorted_by_priority = service.sort_tasks(sort_by="priority", reverse=True)  # High first
    assert sorted_by_priority[0].priority == "High"
    assert sorted_by_priority[-1].priority == "Low"

    sorted_by_title = service.sort_tasks(sort_by="title")
    # Should be in alphabetical order
    titles = [task.title for task in sorted_by_title]
    assert titles == sorted(titles)

    print("✓ Sort functionality works correctly")

    # Test update_task_priority_tags
    updated_task = service.update_task_priority_tags(task1.id, priority="Low", tags=["updated", "test"])
    assert updated_task.priority == "Low"
    assert "updated" in updated_task.tags
    assert "test" in updated_task.tags

    print("✓ Update task priority and tags works correctly")


def test_backward_compatibility():
    """Test that existing functionality still works."""
    print("\nTesting backward compatibility...")

    service = TaskService()

    # Test adding a task with just title (old way)
    task = service.add_task("Simple task")
    assert task.title == "Simple task"
    assert task.priority == "Medium"  # Default
    assert task.tags == []  # Default
    assert task.due_date is None  # Default

    print("✓ Backward compatibility maintained")


def run_all_tests():
    """Run all tests."""
    print("Running tests for intermediate features...\n")

    test_task_model()
    test_task_service()
    test_backward_compatibility()

    print("\n✓ All tests passed! Intermediate features are working correctly.")


if __name__ == "__main__":
    run_all_tests()