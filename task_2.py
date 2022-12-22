# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму
# элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

count = int(input("Укажите количество элементов последовательности: "))
newArray = []
sum = 0

for i in range(1, count + 1):
    nowElement = round((1 + 1 / i)**i, 2)

    if int(nowElement) == nowElement:
        nowElement = int(nowElement)

    newArray.append(nowElement)
    sum += nowElement

print(newArray)
print(f'Сумма {sum}')
