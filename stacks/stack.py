from base.exceptions import NullElementException
from stacks import messages

class Stack:
    def __init__(self) -> None:
        self.data = []

    def size(self):
        return len(self.data)

    def push(self, element):
        if element is None:
            raise NullElementException(messages.NULL_ELEMENT_EXCEPTION)
        
        self.data.append(element)
        return element
