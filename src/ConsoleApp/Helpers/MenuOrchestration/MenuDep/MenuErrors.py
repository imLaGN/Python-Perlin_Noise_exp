"""
This module defines the custom exceptions used within the menu implementation.
"""


class MenuSelectionError(Exception):
    """Custom exception for menu selection errors."""
    def __init__(self, message="Invalid menu selection. Please try again."):
        self.message = message
        super().__init__(self.message)