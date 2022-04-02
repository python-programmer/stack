from base.exceptions import NullElementException, EmptyStackException
from stacks import messages

class Stack:
    """
    A stack data structure
    """

    def __init__(self) -> None:
        self.data = []

    def size(self):
        """
        getting the size of the stack

        Parameters
        ----------
        None

        Returns
        -------
        size: the length of the stack
        """
        return len(self.data)

    def push(self, element):
        """
        pushing an item to the stack

        Parameters
        ----------
        element : Any, required
            An item that we want to be added to the stack

        Returns
        -------
        element
        """
        if element is None:
            raise NullElementException(messages.NULL_ELEMENT_EXCEPTION)
        
        self.data.append(element)
        return element

    def pop(self):
        """
        poping an item to the stack

        Parameters
        ----------
        None

        Returns
        -------
        element: Any

        Exceptions
        ----------
        EmptyStackException: if the stack is empty
        """
        if self.size() == 0:
            raise EmptyStackException(messages.EMPTY_STACK_EXCEPTION)

        return self.data.pop()

    def peek(self):
        """
        reteriving the top element from the stack without removing it

        Parameters
        ----------
        None

        Returns
        -------
        element: Any

        Exceptions
        ----------
        EmptyStackException: if the stack is empty
        """
        if self.size() == 0:
            raise EmptyStackException(messages.EMPTY_STACK_EXCEPTION)

        return self.data[-1]

    def empty(self):
        """
        reteriving the top element from the stack without removing it

        Parameters
        ----------
        None

        Returns
        -------
        is_empty: bool
        """
        return self.size() == 0

