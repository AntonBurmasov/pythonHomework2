# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка
# стоящих на нечётной позиции.
#
# Пример:
#
#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


list = [6, 7, 3, 6, 2, 56, 122, 3]

sum = 0
i = 1

while i < len(list):
    sum = sum + list[i]
    i += 2

print(sum)

