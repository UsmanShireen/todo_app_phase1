"""
Task Model - Represents a single todo item

Task ID: T004 (Create Task model class)
Part of Phase 2: Foundational (Blocking Prerequisites)

This class defines the Task entity with id, title, description, and completed attributes.
"""
from datetime import datetime

class Task:
    def __init__(self, task_id, title, description="", completed=False, priority="Medium", tags=None, due_date=None):
        """
        Initialize a new Task instance.

        Task ID: T007 (Implement Task class constructor with validation)
        Part of Phase 3: User Story 1 - Add New Tasks

        Args:
            task_id (int): Unique identifier for the task
            title (str): Required title of the task
            description (str, optional): Optional description of the task
            completed (bool, optional): Completion status, defaults to False
            priority (str, optional): Priority level, defaults to "Medium"
            tags (list, optional): List of tags, defaults to empty list
            due_date (datetime, optional): Due date for the task
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("task_id must be a positive integer")

        if not isinstance(title, str) or not title.strip():
            raise ValueError("title must be a non-empty string")

        if not isinstance(description, str):
            raise ValueError("description must be a string")

        # Task ID: T023 (Add validation for very long text inputs)
        if len(title) > 1000:  # Reasonable limit for task title
            raise ValueError("title must be 1000 characters or less")

        if len(description) > 10000:  # Reasonable limit for task description
            raise ValueError("description must be 10000 characters or less")

        if not isinstance(completed, bool):
            raise ValueError("completed must be a boolean")

        # Validate priority
        if not isinstance(priority, str):
            raise ValueError("priority must be a string")
        if priority not in ["High", "Medium", "Low"]:
            raise ValueError("priority must be one of: 'High', 'Medium', 'Low'")

        # Validate tags
        if tags is None:
            tags = []
        if not isinstance(tags, list):
            raise ValueError("tags must be a list of strings")
        for tag in tags:
            if not isinstance(tag, str) or not tag.strip():
                raise ValueError("each tag must be a non-empty string")

        # Validate due_date
        if due_date is not None and not isinstance(due_date, datetime):
            raise ValueError("due_date must be a datetime object or None")

        self.id = task_id
        self.title = title.strip()
        self.description = description.strip()
        self.completed = completed
        self.priority = priority
        self.tags = [tag.strip() for tag in tags if tag.strip()]  # Clean up tags
        self.due_date = due_date

    def __str__(self):
        """String representation of the task."""
        status = "✓" if self.completed else "○"
        priority_indicator = self.priority[0]  # H for High, M for Medium, L for Low
        tags_str = f" [{', '.join(self.tags)}]" if self.tags else ""
        due_date_str = f" (Due: {self.due_date.strftime('%Y-%m-%d')})" if self.due_date else ""
        return f"[{status}] {self.id}. [{priority_indicator}] {self.title} - {self.description}{tags_str}{due_date_str}"

    def __repr__(self):
        """Developer representation of the task."""
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed}, priority='{self.priority}', tags={self.tags}, due_date={self.due_date})"

    def to_dict(self):
        """Convert task to dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "priority": self.priority,
            "tags": self.tags,
            "due_date": self.due_date.isoformat() if self.due_date else None
        }

    def update(self, title=None, description=None, completed=None, priority=None, tags=None, due_date=None):
        """
        Update task attributes.

        Args:
            title (str, optional): New title for the task
            description (str, optional): New description for the task
            completed (bool, optional): New completion status for the task
            priority (str, optional): New priority level for the task
            tags (list, optional): New list of tags for the task
            due_date (datetime, optional): New due date for the task
        """
        if title is not None:
            if not isinstance(title, str) or not title.strip():
                raise ValueError("title must be a non-empty string")
            self.title = title.strip()

        if description is not None:
            if not isinstance(description, str):
                raise ValueError("description must be a string")
            self.description = description.strip()

        if completed is not None:
            if not isinstance(completed, bool):
                raise ValueError("completed must be a boolean")
            self.completed = completed

        if priority is not None:
            if not isinstance(priority, str):
                raise ValueError("priority must be a string")
            if priority not in ["High", "Medium", "Low"]:
                raise ValueError("priority must be one of: 'High', 'Medium', 'Low'")
            self.priority = priority

        if tags is not None:
            if not isinstance(tags, list):
                raise ValueError("tags must be a list of strings")
            for tag in tags:
                if not isinstance(tag, str) or not tag.strip():
                    raise ValueError("each tag must be a non-empty string")
            self.tags = [tag.strip() for tag in tags if tag.strip()]

        if due_date is not None:
            if due_date is not None and not isinstance(due_date, datetime):
                raise ValueError("due_date must be a datetime object or None")
            self.due_date = due_date

    def has_tag(self, tag):
        """
        Check if the task has a specific tag.

        Args:
            tag (str): The tag to check for

        Returns:
            bool: True if the task has the tag, False otherwise
        """
        if not isinstance(tag, str) or not tag.strip():
            raise ValueError("tag must be a non-empty string")
        return tag.strip().lower() in [t.lower() for t in self.tags]