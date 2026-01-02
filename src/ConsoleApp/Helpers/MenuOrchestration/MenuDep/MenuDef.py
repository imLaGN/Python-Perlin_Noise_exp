from enum import Enum

class MenuType(Enum):
    UNDEFINED = 0
    MAIN_MENU = 1
    SETTINGS_MENU = 2
    HELP_MENU = 3
    EXIT_MENU = 4

class MenuTemplate(Enum):
    SIMPLE = 1
    DETAILED = 2
    GRAPHICAL = 3
    TEXT_BASED = 4