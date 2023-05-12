def which_triangle(a, b, c):
    # Проверяем, возможно ли существование треугольника с заданными сторонами
    if a + b > c and a + c > b and b + c > a:
        # Проверяем все стороны треугольника на равенство
        if a == b and b == c:
            type_triangle = "Равносторонний"
            # 2 любые стороны треугольника равны между собой, при этом третья не равна первым двум
        elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):  #TODO избыточное условие
            type_triangle = "Равнобедренный"
            # Все стороны треугольника не равны друг другу
        elif a != b and a != c and b != a and b != c:
            type_triangle = "Обычный"
    else:
        # По заданным сторонам невозможно построить треугольник
        type_triangle = "Не треугольник"

    return type_triangle
    

data = [
    (3, 3, 3),
    (1, 2, 2),
    (3, 4, 5),
    (3, 2, 3),
    (1, 2, 3)
]

test_data = [
    "Равносторонний", "Равнобедренный", "Обычный", "Равнобедренный", "Не треугольник"
]


for i, d in enumerate(data):
    assert which_triangle(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
