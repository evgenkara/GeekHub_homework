# Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість символів.
# Файл також додайте в репозиторій. На екран має бути виведений список із трьома блоками -
# символи з початку, із середини та з кінця файлу. Кількість символів в блоках - та,
# яка введена в другому параметрі. Придумайте самі, як обробляти помилку, наприклад,
# коли кількість символів більша, ніж є в файлі або, наприклад, файл із двох символів
# і треба вивести по одному символу, то що виводити на місці середнього блоку символів?).
# Не забудьте додати перевірку чи файл існує.


def main():
    print(make_task('test.txt', 2))


def make_task(path, num):
    try:
        with open(path, 'r') as f:
            text = f.read()
            if len(text) <= num:
                return f'Файл слишком короткий\n{text}'
            elif num < len(text) <= 2 * num:
                return f'Файл слишком короткий\n{[text[:num], text[num:]]}'
            elif 2 * num < len(text) < 3 * num:
                return f'Файл слишком короткий\n{[text[:num], text[num:-num], text[-num:]]}'
            else:
                return [text[:num], text[(len(text) - num) // 2:(len(text) + num) // 2], text[-num:]]

    except FileNotFoundError:
        return f'No such file or directory: {path}'


if __name__ == '__main__':
    main()
