# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int
import random

def mixing (array):
    for i in range(len(array) * 3):
        firstPosition = random.randint(0, len(array) - 1)
        secondPosition = random.randint(0, len(array) - 1)
        array[firstPosition], array[secondPosition] = array[secondPosition], array[firstPosition]

myArray = [1,2,3,4,5,6,7,8]
print(myArray)
mixing(myArray)
print(myArray)
