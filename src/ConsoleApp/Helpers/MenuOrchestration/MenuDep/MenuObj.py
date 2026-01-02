import MenuDef
import MenuItem
import MenuErrors

from MenuDef import MenuType
from MenuErrors import MenuSelectionError
from string import Template

class MenuObj:
    """
    Establishes the structure and basic behaviors of a Menu.
    """

    ## Attributes ##
    # Instance Configurations #
    _menuType = MenuType.UNDEFINED  # We got big plans for this boi

    # Instance Properties #
    @property
    def menuType(self):
        return self._menuType

    # Content Attributes #
    title = ""      # Menu's Main title - Just a header, bruh
    subTitle = ""   # Menu's Sub title - Serves as a description
    statement = ""  # Menu's Statement - Serves as a prompt
    items = []      # Menu's Items - Serves as a list of options


    ## Constructor ##
    def __str__(self):
        return self.render()


    # Methods #
    def render(self):
        """
        Renders the menu as a formatted string.
        Returns:
            str: The formatted menu string.
        """
        res = ""

        res = MenuObj.appendIfExist(res, self.title)
        res = MenuObj.appendIfExist(res, self.subTitle)
        res = MenuObj.appendIfExist(res, self.statement)
        for item in self.items:
            res += f"{str(item)}\n"

        return res

    def solveOption(self, selectedVal):
        """
        Solves the selected menu option.
        Args:
            selectedVal (int): The integer representing the selected menu item/option.
        Returns:
            str: The method call name associated with the selected menu option.
                *May return empty string if no method call name is associated.*
        Raises:
            MenuSelectionError: If the selected value is out of range.
        """
        if selectedVal < 1 or selectedVal > len(self.items):
            raise MenuSelectionError()

        return self.items[selectedVal - 1].getHandler()

    ## Helper Methods ##
    @staticmethod
    def appendIfExist(str, item):
        """
        Appends the item to the string if it exists (is not empty or whitespace).
        Args:
            str (str): The original string.
            item (str): The item to append.
        Returns:
            str: The updated string.
        """
        # Check for empty or whitspace strings
        if not str(item) or str(item).strip() == '':
            return str

        # We expect the previous line to have already had a newline
        return f"{str}{item}\n"
