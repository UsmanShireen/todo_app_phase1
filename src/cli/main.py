"""
Todo Application - Main Entry Point

Task ID: T006 (Create main menu loop structure)
Task ID: T009 (Implement add_task functionality in the menu system)
Part of Phase 2: Foundational and Phase 3: User Story 1

This file serves as the main application entry point with menu loop structure.
"""
from src.services.task_service import TaskService


def main():
    """Main application entry point with menu loop structure."""
    service = TaskService()  # Initialize the task service

    print("Welcome to the Todo Application!")

    while True:
        print("\n" + "="*40)
        print("TODO APPLICATION MENU")
        print("="*40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. Search Tasks")
        print("7. Filter Tasks")
        print("8. Sort Tasks")
        print("9. Manage Task Attributes")
        print("10. Exit")
        print("-"*40)

        try:
            choice = input("Enter your choice (1-10): ").strip()

            # Task ID: T021 (Add comprehensive error handling for invalid menu selections)
            # Validate menu selection
            if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                print("Invalid choice. Please enter a number between 1-10.")
                continue

            if choice == '1':
                # Task ID: T009 (Implement add_task functionality in the menu system)
                add_task_menu(service)
            elif choice == '2':
                view_tasks_menu(service)
            elif choice == '3':
                update_task_menu(service)
            elif choice == '4':
                delete_task_menu(service)
            elif choice == '5':
                mark_task_menu(service)
            elif choice == '6':
                search_tasks_menu(service)
            elif choice == '7':
                filter_tasks_menu(service)
            elif choice == '8':
                sort_tasks_menu(service)
            elif choice == '9':
                manage_task_attributes_menu(service)
            elif choice == '10':
                # Task ID: T027 (Implement clean exit functionality)
                print("Goodbye!")
                break
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


def add_task_menu(service):
    """Handle the add task functionality.

    Task ID: T022 (Add validation for empty title inputs)
    Task ID: T025 (Implement clear success and error messages)
    """
    print("\n--- Add New Task ---")

    try:
        title = input("Enter task title: ").strip()

        # Validate title input
        if not title:
            print("Error: Task title is required!")
            return

        description = input("Enter task description (optional, press Enter to skip): ").strip()

        # Get priority
        print("Select priority level:")
        print("1. High")
        print("2. Medium (default)")
        print("3. Low")
        priority_choice = input("Enter choice (1-3, press Enter for Medium): ").strip()

        priority = "Medium"  # Default
        if priority_choice == "1":
            priority = "High"
        elif priority_choice == "3":
            priority = "Low"
        elif priority_choice == "2":
            priority = "Medium"
        elif priority_choice != "":
            print("Invalid choice. Using default priority: Medium")
            priority = "Medium"

        # Get tags
        tags_input = input("Enter tags (comma-separated, press Enter to skip): ").strip()
        tags = []
        if tags_input:
            tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]

        # Add the task using the service
        task = service.add_task(title, description, priority=priority, tags=tags)
        print(f"✓ Task added successfully! ID: {task.id}, Title: {task.title}, Priority: {task.priority}")
        if task.tags:
            print(f"Tags: {', '.join(task.tags)}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred while adding the task: {e}")


def view_tasks_menu(service):
    """Handle the view tasks functionality.

    Task ID: T012 (Implement view_tasks functionality in the menu system)
    Task ID: T013 (Format task display with ID, title, description, and completion status)
    Part of Phase 4: User Story 2 - View All Tasks
    """
    print("\n--- All Tasks ---")

    tasks = service.get_all_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "✓" if task.completed else "○"
        priority_indicator = task.priority[0]  # H for High, M for Medium, L for Low
        print(f"[{status}] {task.id}. [{priority_indicator}] {task.title}")
        if task.description:
            print(f"    Description: {task.description}")
        if task.tags:
            print(f"    Tags: {', '.join(task.tags)}")
        if task.due_date:
            print(f"    Due: {task.due_date.strftime('%Y-%m-%d')}")
        print()


def update_task_menu(service):
    """Handle the update task functionality.

    Task ID: T017 (Implement update_task functionality in the menu system)
    Part of Phase 5: User Story 3 - Update and Manage Tasks
    """
    print("\n--- Update Task ---")

    try:
        task_id = int(input("Enter task ID to update: ").strip())

        # Check if task exists
        if not service.task_exists(task_id):
            print(f"Error: Task with ID {task_id} does not exist!")
            return

        # Get the current task
        current_task = service.get_task_by_id(task_id)
        print(f"Current task: [{ '✓' if current_task.completed else '○' }] {current_task.id}. {current_task.title}")
        if current_task.description:
            print(f"Current description: {current_task.description}")

        # Get new values (with current values as defaults)
        new_title = input(f"Enter new title (current: '{current_task.title}', press Enter to keep current): ").strip()
        if not new_title:
            new_title = current_task.title

        new_description = input(f"Enter new description (current: '{current_task.description}', press Enter to keep current): ").strip()
        if not new_description:
            new_description = current_task.description

        # Update the task
        updated_task = service.update_task(task_id, new_title, new_description)
        if updated_task:
            print(f"✓ Task updated successfully! ID: {updated_task.id}, Title: {updated_task.title}")
        else:
            print(f"Error: Failed to update task with ID {task_id}")

    except ValueError as e:
        print(f"Error: Invalid input. Please enter a valid task ID.")
    except Exception as e:
        print(f"An error occurred while updating the task: {e}")


def delete_task_menu(service):
    """Handle the delete task functionality.

    Task ID: T018 (Implement delete_task functionality in the menu system)
    Part of Phase 5: User Story 3 - Update and Manage Tasks
    """
    print("\n--- Delete Task ---")

    try:
        task_id = int(input("Enter task ID to delete: ").strip())

        # Check if task exists
        if not service.task_exists(task_id):
            print(f"Error: Task with ID {task_id} does not exist!")
            return

        # Get the task before deletion for confirmation
        task_to_delete = service.get_task_by_id(task_id)
        print(f"Task to delete: [{ '✓' if task_to_delete.completed else '○' }] {task_to_delete.id}. {task_to_delete.title}")

        # Confirm deletion
        confirm = input("Are you sure you want to delete this task? (y/N): ").strip().lower()
        if confirm in ['y', 'yes']:
            success = service.delete_task(task_id)
            if success:
                print(f"✓ Task with ID {task_id} deleted successfully!")
            else:
                print(f"Error: Failed to delete task with ID {task_id}")
        else:
            print("Task deletion cancelled.")

    except ValueError:
        print("Error: Invalid input. Please enter a valid task ID.")
    except Exception as e:
        print(f"An error occurred while deleting the task: {e}")


def mark_task_menu(service):
    """Handle the mark task complete/incomplete functionality.

    Task ID: T019 (Implement mark_complete functionality in the menu system)
    Part of Phase 5: User Story 3 - Update and Manage Tasks
    """
    print("\n--- Mark Task Complete/Incomplete ---")

    try:
        task_id = int(input("Enter task ID to mark: ").strip())

        # Check if task exists
        if not service.task_exists(task_id):
            print(f"Error: Task with ID {task_id} does not exist!")
            return

        # Get the current task
        current_task = service.get_task_by_id(task_id)
        current_status = "completed" if current_task.completed else "incomplete"
        print(f"Current task: [{ '✓' if current_task.completed else '○' }] {current_task.id}. {current_task.title}")
        print(f"Current status: {current_status}")

        # Ask for new status
        status_choice = input("Mark as (C)omplete or (I)ncomplete? (C/I): ").strip().lower()

        if status_choice in ['c', 'complete']:
            new_status = True
        elif status_choice in ['i', 'incomplete']:
            new_status = False
        else:
            print("Invalid choice. Please enter 'C' for complete or 'I' for incomplete.")
            return

        # Update the task status
        updated_task = service.mark_task_complete(task_id, new_status)
        if updated_task:
            new_status_text = "completed" if updated_task.completed else "incomplete"
            print(f"✓ Task marked as {new_status_text} successfully! ID: {updated_task.id}, Title: {updated_task.title}")
        else:
            print(f"Error: Failed to update task status for ID {task_id}")

    except ValueError:
        print("Error: Invalid input. Please enter a valid task ID.")
    except Exception as e:
        print(f"An error occurred while marking the task: {e}")


def search_tasks_menu(service):
    """Handle the search tasks functionality."""
    print("\n--- Search Tasks ---")

    try:
        keyword = input("Enter keyword to search for: ").strip()

        if not keyword:
            print("Error: Keyword is required!")
            return

        matching_tasks = service.search_tasks(keyword)

        if not matching_tasks:
            print(f"No tasks found matching '{keyword}'.")
            return

        print(f"\n--- Search Results for '{keyword}' ---")
        for task in matching_tasks:
            status = "✓" if task.completed else "○"
            priority_indicator = task.priority[0]  # H for High, M for Medium, L for Low
            print(f"[{status}] {task.id}. [{priority_indicator}] {task.title}")
            if task.description:
                print(f"    Description: {task.description}")
            if task.tags:
                print(f"    Tags: {', '.join(task.tags)}")
            if task.due_date:
                print(f"    Due: {task.due_date.strftime('%Y-%m-%d')}")
            print()

    except Exception as e:
        print(f"An error occurred while searching tasks: {e}")


def filter_tasks_menu(service):
    """Handle the filter tasks functionality."""
    print("\n--- Filter Tasks ---")

    try:
        print("Filter by:")
        print("1. Status (Completed/Pending)")
        print("2. Priority")
        print("3. Tag")
        print("4. Multiple criteria")

        filter_choice = input("Enter choice (1-4): ").strip()

        status = None
        priority = None
        tag = None

        if filter_choice == "1":
            print("Select status:")
            print("1. Completed")
            print("2. Pending")
            status_choice = input("Enter choice (1-2): ").strip()
            if status_choice == "1":
                status = True
            elif status_choice == "2":
                status = False
            else:
                print("Invalid choice.")
                return
        elif filter_choice == "2":
            print("Select priority:")
            print("1. High")
            print("2. Medium")
            print("3. Low")
            priority_choice = input("Enter choice (1-3): ").strip()
            if priority_choice == "1":
                priority = "High"
            elif priority_choice == "2":
                priority = "Medium"
            elif priority_choice == "3":
                priority = "Low"
            else:
                print("Invalid choice.")
                return
        elif filter_choice == "3":
            tag = input("Enter tag to filter by: ").strip()
            if not tag:
                print("Error: Tag is required!")
                return
        elif filter_choice == "4":
            # Ask for status
            status_choice = input("Filter by status? (y/N): ").strip().lower()
            if status_choice in ['y', 'yes']:
                print("Select status:")
                print("1. Completed")
                print("2. Pending")
                status_input = input("Enter choice (1-2): ").strip()
                if status_input == "1":
                    status = True
                elif status_input == "2":
                    status = False
                else:
                    print("Invalid status choice.")
                    return

            # Ask for priority
            priority_choice = input("Filter by priority? (y/N): ").strip().lower()
            if priority_choice in ['y', 'yes']:
                print("Select priority:")
                print("1. High")
                print("2. Medium")
                print("3. Low")
                priority_input = input("Enter choice (1-3): ").strip()
                if priority_input == "1":
                    priority = "High"
                elif priority_input == "2":
                    priority = "Medium"
                elif priority_input == "3":
                    priority = "Low"
                else:
                    print("Invalid priority choice.")
                    return

            # Ask for tag
            tag_choice = input("Filter by tag? (y/N): ").strip().lower()
            if tag_choice in ['y', 'yes']:
                tag = input("Enter tag: ").strip()
                if not tag:
                    print("Error: Tag is required!")
                    return
        else:
            print("Invalid choice.")
            return

        filtered_tasks = service.filter_tasks(status=status, priority=priority, tag=tag)

        if not filtered_tasks:
            print("No tasks found matching the filter criteria.")
            return

        print(f"\n--- Filter Results ---")
        for task in filtered_tasks:
            status = "✓" if task.completed else "○"
            priority_indicator = task.priority[0]  # H for High, M for Medium, L for Low
            print(f"[{status}] {task.id}. [{priority_indicator}] {task.title}")
            if task.description:
                print(f"    Description: {task.description}")
            if task.tags:
                print(f"    Tags: {', '.join(task.tags)}")
            if task.due_date:
                print(f"    Due: {task.due_date.strftime('%Y-%m-%d')}")
            print()

    except Exception as e:
        print(f"An error occurred while filtering tasks: {e}")


def sort_tasks_menu(service):
    """Handle the sort tasks functionality."""
    print("\n--- Sort Tasks ---")

    try:
        print("Sort by:")
        print("1. Priority (High to Low)")
        print("2. Title (A to Z)")
        print("3. Due Date (Earliest first)")
        print("4. ID (Lowest first)")

        sort_choice = input("Enter choice (1-4): ").strip()

        sort_by = "id"
        reverse = False

        if sort_choice == "1":
            sort_by = "priority"
            reverse = True  # High to Low
        elif sort_choice == "2":
            sort_by = "title"
            reverse = False  # A to Z
        elif sort_choice == "3":
            sort_by = "due_date"
            reverse = False  # Earliest first
        elif sort_choice == "4":
            sort_by = "id"
            reverse = False  # Lowest first
        else:
            print("Invalid choice.")
            return

        sorted_tasks = service.sort_tasks(sort_by=sort_by, reverse=reverse)

        if not sorted_tasks:
            print("No tasks to sort.")
            return

        print(f"\n--- Sorted Tasks by {sort_by} ---")
        for task in sorted_tasks:
            status = "✓" if task.completed else "○"
            priority_indicator = task.priority[0]  # H for High, M for Medium, L for Low
            print(f"[{status}] {task.id}. [{priority_indicator}] {task.title}")
            if task.description:
                print(f"    Description: {task.description}")
            if task.tags:
                print(f"    Tags: {', '.join(task.tags)}")
            if task.due_date:
                print(f"    Due: {task.due_date.strftime('%Y-%m-%d')}")
            print()

    except Exception as e:
        print(f"An error occurred while sorting tasks: {e}")


def manage_task_attributes_menu(service):
    """Handle the manage task attributes functionality."""
    print("\n--- Manage Task Attributes ---")

    try:
        task_id = int(input("Enter task ID to update attributes: ").strip())

        # Check if task exists
        if not service.task_exists(task_id):
            print(f"Error: Task with ID {task_id} does not exist!")
            return

        # Get the current task
        current_task = service.get_task_by_id(task_id)
        print(f"Current task: [{ '✓' if current_task.completed else '○' }] {current_task.id}. [{current_task.priority[0]}] {current_task.title}")
        if current_task.description:
            print(f"Current description: {current_task.description}")
        if current_task.tags:
            print(f"Current tags: {', '.join(current_task.tags)}")
        if current_task.due_date:
            print(f"Current due date: {current_task.due_date.strftime('%Y-%m-%d')}")

        # Get new priority (optional)
        print(f"\nCurrent priority: {current_task.priority}")
        print("Select new priority (or press Enter to keep current):")
        print("1. High")
        print("2. Medium")
        print("3. Low")
        priority_choice = input("Enter choice (1-3, press Enter to keep current): ").strip()

        new_priority = None
        if priority_choice == "1":
            new_priority = "High"
        elif priority_choice == "2":
            new_priority = "Medium"
        elif priority_choice == "3":
            new_priority = "Low"
        elif priority_choice != "":
            print("Invalid choice. Keeping current priority.")
            new_priority = None

        # Get new tags (optional)
        print(f"\nCurrent tags: {', '.join(current_task.tags) if current_task.tags else 'None'}")
        tags_input = input("Enter new tags (comma-separated, press Enter to keep current): ").strip()
        new_tags = None
        if tags_input:
            new_tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
        elif tags_input == "":
            new_tags = current_task.tags  # Keep current tags if empty input

        # Update the task attributes
        updated_task = service.update_task_priority_tags(task_id, priority=new_priority, tags=new_tags)

        if updated_task:
            print(f"✓ Task attributes updated successfully! ID: {updated_task.id}, Title: {updated_task.title}")
            print(f"Priority: {updated_task.priority}")
            if updated_task.tags:
                print(f"Tags: {', '.join(updated_task.tags)}")
        else:
            print(f"Error: Failed to update task attributes for ID {task_id}")

    except ValueError:
        print("Error: Invalid input. Please enter a valid task ID.")
    except Exception as e:
        print(f"An error occurred while updating task attributes: {e}")


if __name__ == "__main__":
    main()