class UnableToFindWordError(Exception):
    def __init__(self, word):
        self.message = f"Sorry, unable to find word '{word}'."
        super().__init__(self.message)


class UnableToFindLanguageError(Exception):
    def __init__(self, language):
        self.message = f"Sorry, the program doesn't support {language}."
        super().__init__(self.message)
