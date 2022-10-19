# Написати функцію <bank>


def bank(deposit, years, percent=10):
    for i in range(years):
        deposit += deposit * 10 / 100
    deposit = round(deposit, 2)
    print(deposit)
    return deposit


deposit = int(input('Deposit: '))
years = int(input('Years: '))

bank(deposit, years)
