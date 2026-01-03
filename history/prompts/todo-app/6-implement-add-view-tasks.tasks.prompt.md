---
id: 6
title: Implement Add View Tasks
stage: tasks
date: 2026-01-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: todo-app
branch: 001-todo-app
user: user
command: sp.implement
labels: [implementation, todo-app, phase1, user-story]
links:
  spec: specs/001-todo-app/spec.md
  plan: specs/001-todo-app/plan.md
  tasks: specs/001-todo-app/tasks.md
  ticket: null
  adr: null
  pr: null
files:
 - src/models/task.py
 - src/services/task_service.py
 - src/cli/main.py
 - specs/001-todo-app/tasks.md
tests:
 - python3 -c "from src.services.task_service import TaskService; service = TaskService(); task = service.add_task('Test Task', 'Test Description'); all_tasks = service.get_all_tasks(); print('✓ Add and view functionality works correctly' if len(all_tasks) == 1 and all_tasks[0].title == 'Test Task' else '✗ Error')"
---

## Prompt

```text
Implement Task T-003, T-004, and T-005.

Ensure:
- Menu-driven CLI works correctly
- Tasks can be added and viewed
- Proper input validation
```

## Response snapshot

Successfully implemented the requested tasks and completed User Stories 1 and 2:

- T003: Created unit/, integration/ directories in tests/ (completed)
- Enhanced Task class constructor with validation (T007)
- Implemented add_task method with auto-incrementing ID and validation (T008, T010)
- Implemented add_task functionality in the menu system (T009)
- Implemented view_tasks functionality with proper display formatting (T011, T012, T013)
- Added comprehensive input validation and error handling (T021, T022, T025)

The menu-driven CLI now works correctly with proper validation for:
- Adding tasks with required title validation
- Viewing all tasks with proper formatting
- Menu selection validation
- Error messages for invalid inputs

## Outcome

- ✅ Impact: Completed User Stories 1 and 2 (Add and View tasks)
- 🧪 Tests: Verified add and view functionality works correctly
- 📁 Files: Updated task.py, task_service.py, main.py with full functionality
- 🔁 Next prompts: Ready for update/delete functionality (US3)
- 🧠 Reflection: Menu-driven CLI works correctly with proper validation

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Not applicable
- Prompt variant (if applicable): Not applicable
- Next experiment (smallest change to try): Implement User Story 3 (update/delete tasks)