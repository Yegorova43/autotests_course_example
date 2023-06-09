def create_phone_number(num_tuple):
  # переводим числа из кортежа в строки
  temp_string = ''
  for num in num_tuple:
    temp_string += str(num)

  # форматируем полученные строки с помощью срезов
  str_phone = '(' + temp_string[0:3] + ')' + ' ' + temp_string[3:6] + '-' + temp_string[6:]
  return str_phone
    

data = [
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 0),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (0, 2, 3, 0, 5, 6, 0, 8, 9, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
]

test_data = [
    "(123) 456-7890", "(111) 111-1111", "(023) 056-0890", "(000) 000-0000"
]


for i, d in enumerate(data):
    assert create_phone_number(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')