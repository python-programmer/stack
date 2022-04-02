
class NullElementException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class EmptyStackException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)