import re


class Round:
    def __init__(self, title, description, examples, hint, clue, checker):
        self.title = title
        self.description = description
        self.examples = examples
        self.hint = hint
        self.clue = clue
        self.checker = checker

    def check(self, pattern):
        try:
            regex = re.compile(pattern)
        except re.error as error:
            return False, f"Синтаксическая ошибка: {error}"

        return self.checker(regex)
