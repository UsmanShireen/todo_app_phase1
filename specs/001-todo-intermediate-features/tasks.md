---
description: "Task list for Intermediate Level Todo Application implementation"
---

# Tasks: Todo Application Intermediate Features

**Input**: Design documents from `/specs/001-todo-intermediate-features/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] INT-001 Verify existing project structure with src/, models/, services/, cli/ directories
- [ ] INT-002 [P] Backup existing task.py file before modifications
- [ ] INT-003 [P] Backup existing task_service.py file before modifications
- [ ] INT-004 [P] Backup existing main.py file before modifications

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] INT-005 Extend Task model with priority, tags, and due_date attributes in src/models/task.py
- [ ] INT-006 [P] Update TaskService with indexing functionality in src/services/task_service.py
- [ ] INT-007 [P] Update TaskService with search, filter, and sort methods in src/services/task_service.py
- [ ] INT-008 [P] Update CLI menu structure in src/cli/main.py with new options for intermediate features

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Tasks with Priority and Tags (Priority: P1) 🎯 MVP

**Goal**: Enable users to add tasks with priority levels (High, Medium, Low) and tags (work, home, study) to better organize their todo list.

**Independent Test**: User can start the app, select the "Add Task" option, enter a title, description, priority level, and tags, and see the task appear in their list with the specified attributes.

### Implementation for User Story 1

- [ ] INT-009 [P] [US1] Update Task class constructor to accept priority, tags, and due_date parameters in src/models/task.py
- [ ] INT-010 [US1] Add validation for priority values (High, Medium, Low) in src/models/task.py
- [ ] INT-011 [US1] Add validation for tags (list of non-empty strings) in src/models/task.py
- [ ] INT-012 [US1] Update add_task method in TaskService to accept priority, tags, and due_date in src/services/task_service.py
- [ ] INT-013 [US1] Update add_task functionality to initialize indexes in src/services/task_service.py
- [ ] INT-014 [US1] Update add_task menu flow to accept priority and tags input in src/cli/main.py
- [ ] INT-015 [US1] Add clear prompts for priority selection (High/Medium/Low) in src/cli/main.py
- [ ] INT-016 [US1] Add comma-separated input for multiple tags in src/cli/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Search and Filter Tasks (Priority: P1)

**Goal**: Enable users to search and filter their tasks by keyword, priority, status, or tags to quickly find relevant tasks.

**Independent Test**: User can select search/filter options and see filtered results based on their criteria.

### Implementation for User Story 2

- [ ] INT-017 [P] [US2] Implement search_tasks method with keyword matching in src/services/task_service.py
- [ ] INT-018 [P] [US2] Implement filter_tasks method with status/priority/tag filtering in src/services/task_service.py
- [ ] INT-019 [US2] Add search functionality to CLI menu in src/cli/main.py
- [ ] INT-020 [US2] Add filter functionality to CLI menu in src/cli/main.py
- [ ] INT-021 [US2] Add search keyword input interface in src/cli/main.py
- [ ] INT-022 [US2] Add filter selection interface with multiple criteria in src/cli/main.py
- [ ] INT-023 [US2] Add search results display with clear indication in src/cli/main.py
- [ ] INT-024 [US2] Add filter results display with active filter indicators in src/cli/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Sort Tasks (Priority: P2)

**Goal**: Enable users to sort their tasks by priority, title, or due date to better organize their workflow.

**Independent Test**: User can select sort options and see tasks rearranged according to their criteria.

### Implementation for User Story 3

- [ ] INT-025 [P] [US3] Implement sort_tasks method with different criteria in src/services/task_service.py
- [ ] INT-026 [US3] Add sort functionality to CLI menu in src/cli/main.py
- [ ] INT-027 [US3] Add sort selection interface with different sort options in src/cli/main.py
- [ ] INT-028 [US3] Add sort results display with clear indication of sort criteria in src/cli/main.py

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task Attributes (Priority: P2)

**Goal**: Enable users to update priority and tags on existing tasks to reflect changing needs.

**Independent Test**: User can select an existing task and modify its priority level and tags.

### Implementation for User Story 4

- [ ] INT-029 [P] [US4] Implement update_task_priority_tags method in src/services/task_service.py
- [ ] INT-030 [US4] Update existing update_task method to handle priority and tags in src/services/task_service.py
- [ ] INT-031 [US4] Add manage task attributes functionality to CLI menu in src/cli/main.py
- [ ] INT-032 [US4] Add task attribute update interface in src/cli/main.py
- [ ] INT-033 [US4] Update task display format to show priority and tags in src/cli/main.py
- [ ] INT-034 [US4] Add formatted display with visual indicators for priority in src/cli/main.py
- [ ] INT-035 [US4] Add formatted display with brackets for tags in src/cli/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Error Handling and Validation (Priority: P2)

**Goal**: Ensure robust error handling and input validation for new features

**Independent Test**: Application handles invalid inputs gracefully without crashing

### Implementation for Error Handling

- [ ] INT-036 [P] Add validation for invalid priority values in src/models/task.py
- [ ] INT-037 [P] Add validation for invalid tag inputs in src/models/task.py
- [ ] INT-038 Add clear error messages for invalid priority inputs in src/cli/main.py
- [ ] INT-039 Add clear error messages for invalid tag inputs in src/cli/main.py
- [ ] INT-040 Add error handling for empty search queries in src/cli/main.py
- [ ] INT-041 Add graceful handling for no matches in search/filter in src/cli/main.py

**Checkpoint**: Application is robust against invalid inputs for new features

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] INT-042 [P] Update task display format to show all attributes consistently
- [ ] INT-043 [P] Add backward compatibility for existing tasks without priority/tags
- [ ] INT-044 [P] Update documentation and comments for new features
- [ ] INT-045 Code cleanup and refactoring for new functionality
- [ ] INT-046 [P] Update existing tests to account for new attributes
- [ ] INT-047 Run quickstart validation with new features

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable

### Within Each User Story

- Models before services
- Services before CLI implementation
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add tasks with priority/tags)
4. **STOP and VALIDATE**: Test User Story 1 functionality
5. Deploy/Demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add Error Handling → Test comprehensively → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing (if tests requested)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence