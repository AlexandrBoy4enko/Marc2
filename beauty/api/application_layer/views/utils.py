class CustomException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
        print(errors)


class MoneyException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
        print(errors)