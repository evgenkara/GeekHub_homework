# Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні
# операції з 2-ма числами, а саме додавання, віднімання, множення, ділення.
# - Якщо під час створення екземпляру класу звернутися до атрибута last_result він повинен повернути пусте значення.
# - Якщо використати один з методів - last_result повинен повернути результат виконання ПОПЕРЕДНЬОГО методу.


class Calc(object):
    '''
    Calculator
    '''

    def __init__(self):
        self.last_result = None
        self.result = None

    def get_summary(self, x, y):
        self.last_result = self.result
        self.result = x + y

    def get_difference(self, x, y):
        self.last_result = self.result
        self.result = x - y

    def get_product(self, x, y):
        self.last_result = self.result
        self.result = x * y

    def get_division(self, x, y):
        if y == 0:
            print('На ноль делить нельзя!')
        else:
            self.last_result = self.result
            self.result = x / y


c = Calc()
print(c.last_result)
c.get_summary(1, 1)
print(c.last_result)
c.get_product(2, 3)
print(c.last_result)
c.get_difference(6, 4)
print(c.last_result)
c.get_division(10, 2)
print(c.last_result)
c.get_division(5, 0)
print(c.last_result)
