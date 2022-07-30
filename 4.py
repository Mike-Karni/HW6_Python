songString = input("Введите ваше стихотворение ").lower()
vowels= ('а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я')
if songString.isdigit():
    print("Вы ввели не строковое значение. Перезапустите программу и введите стихотворение , а не число! ")
list2 = songString.split()
finalList = []

for words in list2:
    k = 0
    for letter in words:
        if letter in vowels:
            k += 1
    finalList.append(k)
if len(set(finalList)) == 1:
    print('Твоя письма ритмична!!')
else:
    print('Твоя песня не имеет ритма!')
