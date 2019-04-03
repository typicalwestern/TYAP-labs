import re

my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Cтудент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"
my = re.sub(r'Возраст;Категория;', '\t\t\t\t\t О студенте; ;', my_string)
a = re.sub(r'Ф;И;О;', '_;ФИО;', my)
lst = [x.split(';') for i, x in enumerate(a.split('_')) if i > 0]
for x in lst:
 print(x[0], '\t', x[1], '\t', x[2], '\t', x[4], '\t', x[3])
