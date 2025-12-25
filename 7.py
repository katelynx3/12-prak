numbers = [10, 20, 30, 40, 50]
search = int(input('Введите число для поиска '))
index = -1
for i in range(len(numbers)):
    if numbers[i] == search:
        index = i
        print(f'Число найдено на позиции {i}')
        break
else:
    print('Нет такого числа')

#
