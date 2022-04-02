from base.exceptions import NullElementException, EmptyStackException
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

    def pop(self):
        if self.size() == 0:
            raise EmptyStackException(messages.EMPTY_STACK_EXCEPTION)

        return self.data.pop()

    def peek(self):
        if self.size() == 0:
            raise EmptyStackException(messages.EMPTY_STACK_EXCEPTION)

        return self.data[-1]

