# Дан список из 7 различных элементов. Используя функции (не использовать цикл), необходимо найти:
# сумму и среднее арифметическое с округлением до 2 знаков после запятой;


from statistics import mean
from functools import reduce
def get_list_info(lst):
    # максимальный элемент списка
    max_elem = max(lst)
    # минимальный элемент списка
    min_elem = min(lst)
    # сумма 
    sum_list = sum(lst)
    # среднее арифметическое приведенное к типу float и с округлением до 2 знаков после запятой
    average = round((float(mean(lst))), 2 )

   
    return min_elem, max_elem, sum_list, average
    
    
data = [
    [1, 2, 3, 4, 5, 6, 7],
    [-1, -2, -3, -4, -5, -6, -7],
    [99, 56, 209, -308, -12, -18, 42],
    [-1, -2, -3, 0, 1, 2, 3],
]

test_data = [
    (1, 7, 28, 4.0), (-7, -1, -28, -4.0), (-308, 209, 68, 9.71), (-3, 3, 0, 0.0)
]


for i, d in enumerate(data):
    assert get_list_info(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')