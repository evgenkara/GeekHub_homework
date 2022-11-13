# Створити клас Person, в якому буде присутнім метод __init__
# який буде приймати якісь аргументи, які зберігатиме в відповідні змінні.
# - Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
# - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атрибут profession
#   (його не має інсувати під час ініціалізації в самому класі) та виведіть його на екран (прінтоніть)


class Person(object):
    """
    class Person
    """

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def show_age(self):
        print(self.kwargs.get("age"))

    def print_name(self):
        print(self.kwargs.get("name"))

    def show_all_information(self):
        print(self.kwargs)


person1 = Person(name='Robert', age=34, profession='Engineer')
person2 = Person(name='Michael', age=35, profession='Driver')


person1.show_all_information()
person2.show_all_information()