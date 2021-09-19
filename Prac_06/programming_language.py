

class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing.title()
        self.reflection = True or False
        self.year = year

    def is_dynamic(self):
        if self.typing == "dynamic".title():
            return True
        else:
            pass

    def __str__(self):
        return "{}, {} Typing, Reflection = {}, first appeared in {}".format(self.name, self.typing, self.reflection, self.year)
