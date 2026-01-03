<!--
Sync Impact Report:
- Version change: 0.1.0 → 1.0.0
- Modified principles: All principles updated with specific content for Todo App Phase I
- Added sections: Core Principles (6), Additional Constraints, Development Workflow, Governance
- Removed sections: None
- Templates requiring updates: N/A
- Follow-up TODOs: None
-->
# Todo App Phase I Constitution

## Core Principles

### I. Spec-Driven Development Mandatory
All development must follow Spec-Driven Development methodology: Specifications written → Plans created → Tasks defined → Implementation follows. No code implementation without prior specification and planning approval.

### II. Console-Based Application Only
The application must be a pure console/CLI application with no GUI components. All interactions occur through text-based menu interfaces, command inputs, and text output.

### III. In-Memory Task Storage
All task data must be stored in memory only with no persistent storage to files, databases, or external systems. Data will be lost when the application terminates.

### IV. Python 3.13+ Requirement
All code must be written in Python 3.13 or higher. All dependencies and libraries must be compatible with this Python version requirement.

### V. Beginner-Friendly Code
Code must be simple, clean, and accessible to beginners. Use clear variable names, simple control structures, minimal abstraction layers, and comprehensive comments explaining complex logic.

### VI. Menu-Driven CLI Interface
The user interface must be structured as a menu-driven system with numbered options, clear prompts, and intuitive navigation. Users interact through selecting menu items and entering text responses.

## Additional Constraints

- No manual code writing allowed - all implementation must be generated through SDD tools and processes
- No external dependencies beyond standard Python 3.13+ libraries unless absolutely necessary
- Maximum application size should remain under 1000 lines of code for maintainability
- No networking, file I/O, or database connections allowed in Phase I
- Simple, synchronous execution model without threading or async patterns

## Development Workflow

- All changes must follow the red-green-refactor TDD cycle
- Code reviews must verify compliance with all constitution principles
- Implementation must be broken into small, testable increments
- No speculative generality - implement only required functionality
- All user stories must be validated through specification before implementation

## Governance

This constitution supersedes all other development practices for Todo App Phase I. All code submissions, pull requests, and reviews must verify compliance with these principles. Any deviation requires explicit constitution amendment with documented justification.

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02
