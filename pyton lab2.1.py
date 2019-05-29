rez = []
string = input('Введите строку ')
replacements = (',', '-', '!', '?', '.', ':')
for r in replacements:
    string = string.replace(r, ' ')
words = string.split()
for i in range(0,len(words)):
    c = len(words[i])
    if words[i][c-2:c] == 'ов':
        rez.append(words[i])
print(rez)
