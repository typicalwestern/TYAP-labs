a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))
d = float(input('Введите d: '))
f=float(input('Введите f: '))
if a==0:
    print('Ошибка! Деление на 0, проверьте правильность введённых данных!')
rez = abs(a-b*c*d**3+(c**5-a**2)/a+f**3*(a-213))
print('Ответ: ', rez)

