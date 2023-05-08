def modification(lst):
    # сохраняем первый и последний элемент в переменные
    first_item = lst[0]
    last_item = lst[-1]
    # удаляем первый элемент списка
    lst.remove(first_item)
    # вставляем последний элемент списка на первую позицию
    lst.insert(0, last_item)
    # удаляем последний элемент списка
    lst.pop(- 1)
    # вставляем первый элемент списка на последнюю позицию
    lst.append(first_item)
    return lst


data = [
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    ['н', 'л', 'о', 'с']
]

test_data = [
    [3, 2, 1], [5, 2, 3, 4, 1], ['с', 'л', 'о', 'н']
]


for i, d in enumerate(data):
    assert modification(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')