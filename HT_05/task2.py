# Написати функцію <bank>


def bank(deposit, years, percent=10):
    for i in range(years):
        deposit += deposit * percent / 100
    deposit = round(deposit, 2)
    print(deposit)
    return deposit


deposit = int(input('Deposit: '))
years = int(input('Years: '))


bank(deposit, years, 5)
bank(deposit, years)
bank(deposit, years, 20)

