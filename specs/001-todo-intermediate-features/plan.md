# Implementation Plan: Todo Application Intermediate Features

**Branch**: `001-todo-intermediate-features` | **Date**: 2026-01-02 | **Spec**: [specs/001-todo-intermediate-features/spec.md](specs/001-todo-intermediate-features/spec.md)
**Input**: Feature specification from `/specs/001-todo-intermediate-features/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Extension of the console-based Python todo application with intermediate-level organization and usability features. This includes priority levels (High, Medium, Low), tags support, search functionality, filtering capabilities, and sorting options. The application maintains a menu-driven interface approach while adding sophisticated task management features.

## Technical Context

**Language/Version**: Python 3.13+ (as required by constitution)
**Primary Dependencies**: Standard Python 3.13+ libraries only (no external dependencies)
**Storage**: In-memory list/dictionary storage (as required by constitution and spec)
**Testing**: pytest for unit and integration tests (standard Python testing framework)
**Target Platform**: Cross-platform console application (Linux, macOS, Windows)
**Project Type**: Single console application - extends existing structure
**Performance Goals**: Sub-2 second response time for user actions including search/filter/sort operations
**Constraints**: <200MB memory usage, console-only interface, no network/file I/O beyond requirements
**Scale/Scope**: Single user application, up to 1000 tasks in memory, under 1000 lines of code

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ Spec-Driven Development Mandatory: Following proper sequence (spec → plan → tasks → implementation)
- ✅ Console-Based Application Only: Implementation will be pure CLI with text-based menu interface
- ✅ In-Memory Task Storage: Will use Python data structures only, no file/database persistence
- ✅ Python 3.13+ Requirement: Implementation will target Python 3.13+ compatibility
- ✅ Beginner-Friendly Code: Will use simple control structures, clear variable names, minimal abstractions
- ✅ Menu-Driven CLI Interface: Will implement numbered menu system with clear prompts

All constitution gates pass. No violations detected.

## Detailed Implementation Requirements

### 1. Task Data Model Changes

**File**: `src/models/task.py`
- Add `priority` attribute (string, values: "High", "Medium", "Low", default: "Medium")
- Add `tags` attribute (list of strings, default: empty list)
- Add `due_date` attribute (datetime, optional)
- Update constructor to accept priority, tags, and due_date parameters
- Add validation for priority values (must be one of "High", "Medium", "Low")
- Add validation for tags (must be list of non-empty strings)
- Add `update_priority_tags` method to update priority and tags
- Add `has_tag` method to check if task has a specific tag

### 2. Task Service Enhancements

**File**: `src/services/task_service.py`
- Add `tag_index` dictionary mapping tags to lists of task IDs for efficient filtering
- Add `priority_index` dictionary mapping priorities to lists of task IDs for efficient filtering
- Update `add_task` method to accept priority, tags, and due_date parameters
- Add `search_tasks` method for keyword-based search in title and description
- Add `filter_tasks` method with parameters for status, priority, and tag filtering
- Add `sort_tasks` method with parameter for different sort criteria (priority, title, due_date)
- Add `update_task_priority_tags` method to update priority and tags of existing tasks
- Update indexes when tasks are added, updated, or deleted
- Add `get_tasks_by_priority` method for priority-based retrieval
- Add `get_tasks_by_tag` method for tag-based retrieval

### 3. Search, Filter, and Sort Logic

**Search Implementation**:
- Case-insensitive substring matching in title and description
- Return list of tasks matching the keyword
- Support for partial matches

**Filter Implementation**:
- Filter by completion status (completed/pending)
- Filter by priority (High/Medium/Low)
- Filter by tags (tasks with specific tag)
- Support for combining multiple filters

**Sort Implementation**:
- Sort by priority (High > Medium > Low)
- Sort alphabetically by title (A-Z)
- Sort by due date (chronological order)
- Default sort by ID if no due date exists

### 4. CLI Menu Updates

**File**: `src/cli/main.py`
- Add "Search Tasks" menu option (new option #7)
- Add "Filter Tasks" menu option (new option #8)
- Add "Sort Tasks" menu option (new option #9)
- Add "Manage Task Attributes" menu option (new option #10) for updating priority/tags
- Update "Add Task" flow to include priority and tags input
- Update task display format to show priority and tags
- Add search functionality with keyword input
- Add filter selection interface with multiple criteria
- Add sort selection interface with different sort options
- Add task attribute update interface

### 5. User-Friendly Console Interface

- Clear prompts for priority selection (High/Medium/Low)
- Comma-separated input for multiple tags
- Formatted display showing priority with visual indicators (e.g., H/M/L)
- Formatted display showing tags in brackets [tag1, tag2]
- Clear error messages for invalid inputs
- Search results with highlighted matches
- Filter results with clear indication of active filters
- Sort results with clear indication of sort criteria

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-intermediate-features/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── models/
│   └── task.py          # Extended Task class definition and management
├── services/
│   └── task_service.py  # Extended business logic for task operations with search/filter/sort
└── cli/
    └── main.py          # Extended application entry point with enhanced menu system

tests/
├── unit/
│   ├── test_task.py     # Unit tests for extended Task model
│   └── test_task_service.py  # Unit tests for extended task service
└── integration/
    └── test_cli_flow.py # Integration tests for enhanced CLI interactions
```

**Structure Decision**: Single project structure selected with logical separation of concerns, extending existing modules:
- `models/` extends Task model with priority, tags, and due_date attributes
- `services/` extends TaskService with search, filter, and sort functionality
- `cli/` extends main CLI with new menu options for intermediate features

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | N/A | N/A |
