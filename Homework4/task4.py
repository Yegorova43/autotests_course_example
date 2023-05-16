import math

def multiplication_chain(num):
    count_multy = 0

    # если в числе всего 1 символ, сразу выдаем счетчик 0
    if len(str(num)) == 1:
        return count_multy

    else:
        #  делаем из переданного числа список и перемножаем между собой все составляющие
        mult_num = math.prod(map(int, str(num)))
        count_multy += 1
        while len(str(mult_num)) > 1:
            # находим новое произведение чисел
            mult_num_new = math.prod(map(int, str(mult_num)))
            # присваиваем новое произведение переменной вне цикла
            mult_num = mult_num_new
            # увеличиваем счетчик на 1
            count_multy += 1
    return count_multy


data = [
    39, 4, 25, 999, 5050, 222333444
]

test_data = [
    3, 0, 2, 4, 1, 4
]

for i, d in enumerate(data):
    assert multiplication_chain(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
