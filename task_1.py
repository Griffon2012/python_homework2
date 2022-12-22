numberString = input('Введите вещественное число: ')
sum = 0
for char in numberString:
    if char.isnumeric():
        sum += int(char)
print(f'Сумма цифр: {sum}')