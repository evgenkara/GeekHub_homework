# Програма-світлофор. Створити програму-емулятор світлофора для авто і пішоходів.
# Після запуска програми на екран виводиться в лівій половині - колір автомобільного,
# а в правій - пішохідного світлофора. Кожну 1 секунду виводиться поточні кольори.
# Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в
# звичайних світлофорах (пішоходам зелений тільки коли автомобілям червоний).


import time



def main():
    street_lighter()

    
def street_lighter():

    colors = ['STOP', 'READY', 'MOVE']
    red = '\033[1;31m'
    yellow = '\033[1;33m'
    green = '\033[1;32m'
    base = '\033[0m'
    
    while True:
        
        for i in range(4):
            print(f'{red}{colors[0]}\t\t{green}{colors[2]}{base}')
            time.sleep(1)
 
        for i in range(2):
            print(f'{yellow}{colors[1]}\t\t{red}{colors[0]}{base}')
            time.sleep(1)
 
        for i in range(4):
            print(f'{green}{colors[2]}\t\t{red}{colors[0]}{base}')
            time.sleep(1)
 
        for i in range(2):
            print(f'{yellow}{colors[1]}\t\t{red}{colors[0]}{base}')
            time.sleep(1)


if __name__ == '__main__':
    main()





