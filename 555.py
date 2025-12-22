data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
one = data[:3]
two = data[-3:]
reverse = data[::-1]
nechet = data[0::2]
print(f'Первая тройка чисел: {one}')
print(f'Последняя тройка чисел: {two}')
print(f'Список в обратном порядке: {reverse}')
print(f'Числа с нечетным индексом: {nechet}')
