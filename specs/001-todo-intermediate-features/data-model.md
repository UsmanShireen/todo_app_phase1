# Data Model: Todo Application Intermediate Features

## Task Entity (Extended)

### Attributes
- **id**: integer, auto-increment, required (unique identifier)
- **title**: string, required (task description)
- **description**: string, optional (additional details)
- **completed**: boolean, default false (completion status)
- **priority**: string, values: "High", "Medium", "Low", default "Medium" (task priority level)
- **tags**: list of strings, optional (tags associated with the task)
- **due_date**: datetime, optional (due date for the task)

### Validation Rules
- id: Must be a positive integer, auto-assigned, unique within the system
- title: Must be a non-empty string with minimum length of 1 character
- description: Optional, can be empty string if not provided
- completed: Must be a boolean value, defaults to false when creating new tasks
- priority: Must be one of "High", "Medium", "Low", defaults to "Medium" when creating new tasks
- tags: Must be a list of strings, can be empty, each tag must be a non-empty string
- due_date: Optional, if provided must be a valid datetime object

### State Transitions
- New Task: id (auto-assigned), title (set by user), description (set by user or empty), completed (false), priority (set by user or default "Medium"), tags (set by user or empty list), due_date (set by user or None)
- Completed Task: completed status changed from false to true
- Updated Task: any attributes changed while preserving id
- Deleted Task: removed from the in-memory storage

## In-Memory Storage Structure
- **tasks**: Dictionary/Map with id as key and Task object as value
- **next_id**: Integer counter to track the next available ID for auto-increment
- **tag_index**: Dictionary mapping tags to lists of task IDs for efficient filtering
- **priority_index**: Dictionary mapping priorities to lists of task IDs for efficient filtering