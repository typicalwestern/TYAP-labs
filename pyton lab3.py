import os, os.path

def resh(vibor):
    if vibor == 1:
        path = input('Write Path ->')
        list = os.listdir(path)
        kolvo = len(list)
        print (kolvo)

    if vibor == 2:
        for i in ok:
            if int(i[2]) > 1700:
                print(i[0],i[1],i[2],i[3])

    if vibor == 3:
        minus = int(input('на какое число вы желаете уменьшить количество товара? '))
        for i in ok:
            i[3] = int(i[3]) - minus
            print(i[0],i[1],i[2],i[3])

    if vibor == 4:
        dir = input('Введите директорию для сохранения файла -> ')
        e = open(dir, 'w')
        for i in ok:
            e.write(str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]) + ' ' + str(i[3]) + '\n')
        e.close()


vibor = int(input("Введите желаемый номер задания: "))
while vibor != 1 and vibor != 2 and vibor != 3 and vibor != 4:
    vibor = int(input("Введите номер варианта повторно: "))
f = open('products.txt', 'r')
kok = []
ko = []
ok = []
c = f.read()
kok = c.replace(' \n', ' '). split()
f.close()
lenc = len(kok)
for i in range(0,lenc):
    ko = (kok[i].split(','))
    ok.append(ko[0].split(';'))
ok.sort(key = lambda i: i[2])
if vibor == 1 or vibor == 2 or vibor == 3 or vibor == 4:
    resh(vibor)
    prov = input('Хотите продолжить? Введите yes, Y, 1 или no, N, 0: ')
    while prov != 'yes' and prov != 'Y' and prov != '1' and prov != 'no' and prov != 'N' and prov != '0':
        prov = input('Данный ответ некооректный/ Введите ответ еще раз. ')
    while prov == 'yes' or prov == 'Y' or prov == '1':
        vibor = int(input("Введите желаемый номер задания: "))
        while vibor != 1 and vibor != 2 and vibor != 3 and vibor != 4:
            vibor = int(input("Введите номер варианта повторно: "))
            resh(vibor)
        prov = input('Хотите продолжить? Введите yes, Y, 1 или no, N, 0: ')
    if prov == 'no' or prov == 'N' or prov == '0':
        exit()
