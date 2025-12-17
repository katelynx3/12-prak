price = [1500, 500, 2000, 3500, 1000, 4500]
total = sum(price)
print(f'''Самый дорогой товар - {max(price)}
Самый дешевый товар - {min(price)}
Общая стоимость - {sum(price)}
Средняя цена товара - {total / len(price)}''')
