# API Contract: Todo Application

## Overview
This document defines the interface contracts for the Todo Application CLI operations.

## Task Operations

### Add Task
- **Operation**: Create a new task
- **Input**: title (string, required), description (string, optional)
- **Output**: task object with id, title, description, completed status
- **Success**: Returns the created task with auto-assigned ID
- **Errors**: Invalid input (empty title)

### View All Tasks
- **Operation**: Retrieve all tasks in the system
- **Input**: None
- **Output**: List of task objects
- **Success**: Returns all tasks with their details
- **Errors**: None (returns empty list if no tasks)

### Update Task
- **Operation**: Update an existing task by ID
- **Input**: task_id (integer), title (string, optional), description (string, optional)
- **Output**: updated task object
- **Success**: Returns the updated task
- **Errors**: Task not found, invalid task ID

### Delete Task
- **Operation**: Remove a task by ID
- **Input**: task_id (integer)
- **Output**: success confirmation
- **Success**: Task removed from system
- **Errors**: Task not found, invalid task ID

### Mark Task Complete/Incomplete
- **Operation**: Toggle completion status of a task
- **Input**: task_id (integer), completed (boolean)
- **Output**: updated task object
- **Success**: Returns task with updated completion status
- **Errors**: Task not found, invalid task ID