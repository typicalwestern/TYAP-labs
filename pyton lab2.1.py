import re
string = input('Введите строку ')

result = re.findall(r'\w+ов', string)
print(result)

