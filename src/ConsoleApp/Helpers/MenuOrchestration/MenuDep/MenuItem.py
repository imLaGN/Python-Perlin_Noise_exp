
class MenuItem:
    """
    Represents a single option item in a menu with associated text and method call name.
    *Refer to MenuHandler for available method call names.*
    """

    ## Attributes ##
    _text = ""               # Display text for the menu item
    _methodCallName = ""     # Associated method call name for the menu item

    ## Methods ##
    def __init__(self, text, methodCallName):
        """
        Initiate a Menu Item with display text and associated method call name.
        *Refer to MenuHandler for available method call names.*
        """
        self._text = text
        self._methodCallName = methodCallName

    def __str__(self):
        """
        Returns the display text of the menu item.
        Ease the process of rendering the menu.
        E.g: str(menuItem) -> "Start Game"
        Returns:
            str: The display text of the menu item.
        """
        #Ensure text is valid
        if not self._text or self._text.strip() == '':
            return ""

        return f"{self._text}"

    def __repr__(self):
        """
        Returns a detailed string representation of the MenuItem instance.
        Returns:
            str: The detailed string representation of the MenuItem.
        """
        return f"MenuItem(text={self._text}, methodCallName={self._methodCallName})"


    def getHandler(self):
        """
        Retrieves the associated method call name for the menu item.
        *Used by the MenuHandler to invoke the correct method.*
        Returns:
            str: The method call name.
        """
        if not self._methodCallName or self._methodCallName.strip() == '':
            return ""

        return self._methodCallName