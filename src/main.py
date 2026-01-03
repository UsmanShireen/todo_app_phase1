"""
Todo Application - Single Entry Point

This file serves as the main application entry point to start the CLI application.
It imports and invokes the menu from src/cli/main.py to maintain separation of concerns
while providing a single entry point as requested.
"""
import sys
import os
# Add the project root to the path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.cli.main import main


def run():
    """
    Run the Todo Application.

    This function serves as the entry point to start the CLI application
    by invoking the main menu function from the CLI module.
    """
    main()


if __name__ == "__main__":
    run()