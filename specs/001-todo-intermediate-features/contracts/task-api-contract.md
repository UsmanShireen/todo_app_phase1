# API Contract: Todo Application Intermediate Features

## Overview
This document defines the interface contracts for the Todo Application CLI operations with intermediate features.

## Task Operations (Extended)

### Add Task with Priority and Tags
- **Operation**: Create a new task with priority and tags
- **Input**: title (string, required), description (string, optional), priority (string, optional, default "Medium"), tags (list of strings, optional), due_date (datetime, optional)
- **Output**: task object with id, title, description, completed status, priority, tags, due_date
- **Success**: Returns the created task with auto-assigned ID and default priority if not specified
- **Errors**: Invalid input (empty title), invalid priority value

### Search Tasks
- **Operation**: Search tasks by keyword in title or description
- **Input**: keyword (string, required)
- **Output**: List of task objects matching the keyword
- **Success**: Returns all tasks containing the keyword in title or description
- **Errors**: None (returns empty list if no matches)

### Filter Tasks
- **Operation**: Filter tasks by criteria (status, priority, tags)
- **Input**: filter_criteria (dict with keys: status, priority, tag)
- **Output**: List of task objects matching the criteria
- **Success**: Returns tasks matching the specified filter criteria
- **Errors**: Invalid filter criteria

### Sort Tasks
- **Operation**: Sort tasks by criteria (priority, title, due_date)
- **Input**: sort_criteria (string: "priority", "title", "due_date")
- **Output**: List of task objects sorted according to criteria
- **Success**: Returns tasks sorted in the specified order
- **Errors**: Invalid sort criteria

### Update Task Attributes
- **Operation**: Update priority and tags of an existing task
- **Input**: task_id (integer), priority (string, optional), tags (list of strings, optional)
- **Output**: updated task object
- **Success**: Returns the updated task
- **Errors**: Task not found, invalid task ID, invalid priority value