class UserException(Exception):

    def __init__(self, message="You can't add any more students to this group!"):
        self.message = message
        super().__init__(self.message)