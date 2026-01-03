# Data Model: Todo Application

## Task Entity

### Attributes
- **id**: integer, auto-increment, required (unique identifier)
- **title**: string, required (task description)
- **description**: string, optional (additional details)
- **completed**: boolean, default false (completion status)

### Validation Rules
- id: Must be a positive integer, auto-assigned, unique within the system
- title: Must be a non-empty string with minimum length of 1 character
- description: Optional, can be empty string if not provided
- completed: Must be a boolean value, defaults to false when creating new tasks

### State Transitions
- New Task: id (auto-assigned), title (set by user), description (set by user or empty), completed (false)
- Completed Task: completed status changed from false to true
- Updated Task: title or description changed while preserving id
- Deleted Task: removed from the in-memory storage

## In-Memory Storage Structure
- **tasks**: Dictionary/Map with id as key and Task object as value
- **next_id**: Integer counter to track the next available ID for auto-increment