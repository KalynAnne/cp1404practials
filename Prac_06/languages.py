"""Import Class ProgrammingLanguage"""
from Prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    """Create list of languages"""
    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for i in languages:
        if ProgrammingLanguage.is_dynamic(i):
            print(i.name)


main()
