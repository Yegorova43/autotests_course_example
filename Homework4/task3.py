def sum_digits(num):
    
    # Приводим число к строке, чтобы работать с каждым символом отдельно
    num_str = str(num)
    # создает список для хранения всех символов из числа
    num_lst = []
    # итерируемся по списку из строк, в итоговый список добавляем элементы с типом int
    for i in num_str:
        a = 0
        a += int(i)
        num_lst.append(a)
    
    # создаем переменную для подсчета суммы элементов из числа
    our_sum = 0
    # итерируемся по списку из элементов числа, складываем все элементы между собой
    for i in num_lst:
        our_sum += i
    
    return (our_sum)   
    

data = [
    39, 4, 25, 999, 5050, 222333444
]

test_data = [
    12, 4, 7, 27, 10, 27
]


for i, d in enumerate(data):
    assert sum_digits(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')    

