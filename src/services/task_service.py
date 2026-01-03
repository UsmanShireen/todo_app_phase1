"""
Task Service - Business logic for task operations

Task ID: T005 (Create in-memory storage structure)
Part of Phase 2: Foundational (Blocking Prerequisites)

This class handles business logic for task operations with in-memory storage.
"""
from src.models.task import Task
from datetime import datetime


class TaskService:
    def __init__(self):
        """
        Initialize the TaskService with in-memory storage.

        Creates:
            - tasks: Dictionary with id as key and Task object as value
            - next_id: Integer counter to track the next available ID for auto-increment
            - tag_index: Dictionary mapping tags to lists of task IDs for efficient filtering
            - priority_index: Dictionary mapping priorities to lists of task IDs for efficient filtering
        """
        self.tasks = {}  # Dictionary with id as key and Task object as value
        self.next_id = 1  # Integer counter to track the next available ID for auto-increment
        # Indexes for efficient filtering and searching
        self.tag_index = {}  # Maps tag -> list of task IDs
        self.priority_index = {"High": [], "Medium": [], "Low": []}  # Maps priority -> list of task IDs

    def add_task(self, title, description="", priority="Medium", tags=None, due_date=None):
        """
        Add a new task with auto-incrementing ID.

        Task ID: T008 (Implement add_task method with auto-incrementing ID)
        Task ID: T010 (Add input validation for required title field)
        Part of Phase 3: User Story 1 - Add New Tasks

        Args:
            title (str): Required title of the task
            description (str, optional): Optional description of the task
            priority (str, optional): Priority level, defaults to "Medium"
            tags (list, optional): List of tags, defaults to empty list
            due_date (datetime, optional): Due date for the task

        Returns:
            Task: The newly created Task object
        """
        # Input validation for required title field
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title is required and must be a non-empty string")

        # Create the task with the next available ID
        task = Task(self.next_id, title, description, completed=False, priority=priority, tags=tags, due_date=due_date)

        # Add to the tasks dictionary
        self.tasks[self.next_id] = task

        # Update indexes
        self._update_indexes_on_add(task)

        # Increment the ID counter for the next task
        self.next_id += 1

        return task

    def get_task_by_id(self, task_id):
        """
        Retrieve a task by its ID.

        Task ID: T020 (Add error handling for invalid task IDs)
        Part of Phase 5: User Story 3 - Update and Manage Tasks

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Task: The task with the specified ID, or None if not found
        """
        return self.tasks.get(task_id)

    def get_all_tasks(self):
        """
        Retrieve all tasks.

        Task ID: T024 (Add graceful handling when all tasks are deleted)
        Part of Phase 6: Error Handling and Validation

        Returns:
            list: A list of all Task objects
        """
        return list(self.tasks.values())

    def update_task(self, task_id, title=None, description=None, completed=None, priority=None, tags=None, due_date=None):
        """
        Update an existing task by ID.

        Task ID: T014 (Implement update_task method)
        Task ID: T020 (Add error handling for invalid task IDs)
        Part of Phase 5: User Story 3 - Update and Manage Tasks

        Args:
            task_id (int): The ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task
            completed (bool, optional): New completion status for the task
            priority (str, optional): New priority level for the task
            tags (list, optional): New list of tags for the task
            due_date (datetime, optional): New due date for the task

        Returns:
            Task: The updated Task object, or None if task doesn't exist
        """
        task = self.tasks.get(task_id)
        if task:
            # Store old values for index updates
            old_priority = task.priority
            old_tags = task.tags[:]

            # Update the task
            task.update(title, description, completed, priority, tags, due_date)

            # Update indexes based on changes
            self._update_indexes_on_update(task, old_priority, old_tags)
            return task
        return None

    def delete_task(self, task_id):
        """
        Delete a task by ID.

        Task ID: T015 (Implement delete_task method)
        Part of Phase 5: User Story 3 - Update and Manage Tasks

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if it didn't exist
        """
        if task_id in self.tasks:
            task = self.tasks[task_id]
            # Remove from indexes before deleting
            self._remove_from_indexes(task)
            del self.tasks[task_id]
            return True
        return False

    def mark_task_complete(self, task_id, completed=True):
        """
        Mark a task as complete or incomplete.

        Task ID: T016 (Implement mark_task_complete method)
        Part of Phase 5: User Story 3 - Update and Manage Tasks

        Args:
            task_id (int): The ID of the task to update
            completed (bool): The completion status to set (default True)

        Returns:
            Task: The updated Task object, or None if task doesn't exist
        """
        task = self.tasks.get(task_id)
        if task:
            # Store old values for index updates
            old_priority = task.priority
            old_tags = task.tags[:]

            task.update(completed=completed)

            # Update indexes based on changes (priority and tags didn't change, but still need to call this to maintain consistency)
            self._update_indexes_on_update(task, old_priority, old_tags)
            return task
        return None

    def task_exists(self, task_id):
        """
        Check if a task exists by ID.

        Task ID: T020 (Add error handling for invalid task IDs)
        Part of Phase 5: User Story 3 - Update and Manage Tasks

        Args:
            task_id (int): The ID of the task to check

        Returns:
            bool: True if the task exists, False otherwise
        """
        return task_id in self.tasks

    def get_next_id(self):
        """
        Get the next available ID.

        Returns:
            int: The next available ID for a new task
        """
        return self.next_id

    def _update_indexes_on_add(self, task):
        """
        Update indexes when a task is added.

        Args:
            task (Task): The task that was added
        """
        # Add to priority index
        self.priority_index[task.priority].append(task.id)

        # Add to tag index
        for tag in task.tags:
            tag_lower = tag.lower()
            if tag_lower not in self.tag_index:
                self.tag_index[tag_lower] = []
            self.tag_index[tag_lower].append(task.id)

    def _update_indexes_on_update(self, task, old_priority, old_tags):
        """
        Update indexes when a task is updated.

        Args:
            task (Task): The task that was updated
            old_priority (str): The old priority value
            old_tags (list): The old tags list
        """
        # Remove from old priority index
        if task.id in self.priority_index[old_priority]:
            self.priority_index[old_priority].remove(task.id)

        # Add to new priority index
        if task.id not in self.priority_index[task.priority]:
            self.priority_index[task.priority].append(task.id)

        # Remove from old tag indexes
        for old_tag in old_tags:
            old_tag_lower = old_tag.lower()
            if old_tag_lower in self.tag_index and task.id in self.tag_index[old_tag_lower]:
                self.tag_index[old_tag_lower].remove(task.id)
                # Clean up empty lists
                if not self.tag_index[old_tag_lower]:
                    del self.tag_index[old_tag_lower]

        # Add to new tag indexes
        for new_tag in task.tags:
            new_tag_lower = new_tag.lower()
            if new_tag_lower not in self.tag_index:
                self.tag_index[new_tag_lower] = []
            if task.id not in self.tag_index[new_tag_lower]:
                self.tag_index[new_tag_lower].append(task.id)

    def _remove_from_indexes(self, task):
        """
        Remove a task from all indexes.

        Args:
            task (Task): The task to remove from indexes
        """
        # Remove from priority index
        if task.id in self.priority_index[task.priority]:
            self.priority_index[task.priority].remove(task.id)

        # Remove from tag indexes
        for tag in task.tags:
            tag_lower = tag.lower()
            if tag_lower in self.tag_index and task.id in self.tag_index[tag_lower]:
                self.tag_index[tag_lower].remove(task.id)
                # Clean up empty lists
                if not self.tag_index[tag_lower]:
                    del self.tag_index[tag_lower]

    def search_tasks(self, keyword):
        """
        Search tasks by keyword in title and description.

        Args:
            keyword (str): The keyword to search for

        Returns:
            list: List of tasks that match the keyword
        """
        if not keyword or not isinstance(keyword, str):
            return []

        keyword_lower = keyword.lower().strip()
        if not keyword_lower:
            return []

        matching_tasks = []
        for task in self.tasks.values():
            if (keyword_lower in task.title.lower() or
                keyword_lower in task.description.lower()):
                matching_tasks.append(task)

        return matching_tasks

    def filter_tasks(self, status=None, priority=None, tag=None):
        """
        Filter tasks by status, priority, or tag.

        Args:
            status (bool, optional): Filter by completion status (True for completed, False for pending)
            priority (str, optional): Filter by priority level
            tag (str, optional): Filter by tag

        Returns:
            list: List of tasks that match the filter criteria
        """
        filtered_tasks = list(self.tasks.values())

        # Filter by status
        if status is not None:
            filtered_tasks = [task for task in filtered_tasks if task.completed == status]

        # Filter by priority
        if priority is not None:
            if priority in ["High", "Medium", "Low"]:
                filtered_tasks = [task for task in filtered_tasks if task.priority == priority]

        # Filter by tag
        if tag is not None and isinstance(tag, str) and tag.strip():
            tag_lower = tag.strip().lower()
            filtered_tasks = [task for task in filtered_tasks if task.has_tag(tag)]

        return filtered_tasks

    def sort_tasks(self, sort_by="id", reverse=False):
        """
        Sort tasks by various criteria.

        Args:
            sort_by (str): Criteria to sort by ('id', 'title', 'priority', 'due_date')
            reverse (bool): Whether to sort in reverse order

        Returns:
            list: List of tasks sorted by the specified criteria
        """
        tasks = list(self.tasks.values())

        if sort_by == "priority":
            # Define priority order: High > Medium > Low
            priority_order = {"High": 3, "Medium": 2, "Low": 1}
            tasks.sort(key=lambda task: priority_order[task.priority], reverse=reverse)
        elif sort_by == "title":
            tasks.sort(key=lambda task: task.title.lower(), reverse=reverse)
        elif sort_by == "due_date":
            # Sort by due date, with None values at the end
            tasks.sort(key=lambda task: (task.due_date is None, task.due_date), reverse=reverse)
        elif sort_by == "id":
            tasks.sort(key=lambda task: task.id, reverse=reverse)

        return tasks

    def get_tasks_by_priority(self, priority):
        """
        Get tasks by priority level.

        Args:
            priority (str): The priority level to filter by

        Returns:
            list: List of tasks with the specified priority
        """
        if priority not in ["High", "Medium", "Low"]:
            return []

        task_ids = self.priority_index.get(priority, [])
        return [self.tasks[task_id] for task_id in task_ids if task_id in self.tasks]

    def get_tasks_by_tag(self, tag):
        """
        Get tasks by tag.

        Args:
            tag (str): The tag to filter by

        Returns:
            list: List of tasks with the specified tag
        """
        if not tag or not isinstance(tag, str) or not tag.strip():
            return []

        tag_lower = tag.strip().lower()
        task_ids = self.tag_index.get(tag_lower, [])
        return [self.tasks[task_id] for task_id in task_ids if task_id in self.tasks]

    def update_task_priority_tags(self, task_id, priority=None, tags=None):
        """
        Update priority and tags of a task.

        Args:
            task_id (int): The ID of the task to update
            priority (str, optional): New priority level
            tags (list, optional): New list of tags

        Returns:
            Task: The updated Task object, or None if task doesn't exist
        """
        return self.update_task(task_id, priority=priority, tags=tags)