# Створити цикл від 0 до ... (вводиться користувачем).
# В циклі створити умову, яка буде виводити поточне значення,
# якщо остача від ділення на 17 дорівнює 0.


user_input = int(input('Enter a number: '))
for i in range(user_input + 1):
    if i % 17 == 0:
        print(i)
