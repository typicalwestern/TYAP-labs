import random

N = int(input('Сколько будет чисел?'))
while N <= 10:
    N = int(input('Некорректное количество элементов. Список должен состоять более чем из 10 элементов. Введите верное количество чисел.'))
print('Ваш список состоит из', N, 'элементов')

chisla = [int(x) for x in input('Введите числа через пробел ').split()]
while len(chisla) != N:
    print('Введено количество элементов, не соответствующее заявленному')
    chisla = [int(x) for x in input('Введите числа через пробел ').split()]

a = random.randint(0, 100)
b = random.randint(0, 100)
c = random.randint(0, 100)
d = random.randint(0, 100)
f = random.randint(0, 100)

chisla.append(a)
chisla.append(b)
chisla.append(c)
chisla.append(d)
chisla.append(f)

#print(chisla)

chisla = [x for x in chisla if x % 2 != 0]
print(chisla)

