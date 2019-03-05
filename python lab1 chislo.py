from random import randint

print('Введите диапазон для загадывания числа')
a = randint(int(input('Нижняя граница диапазона ')), int(input('Верхняя граница диапазона ')))
print('Угадайте натуральное число')

ch = int(input())
while ch != a:
    if ch > a:
        print('Загаданное число меньше')
        ch = int(input())
    elif ch < a:
        print('Загаданное число больше')
        ch = int(input())
print('Вы угадали!')
