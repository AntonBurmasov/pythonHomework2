# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]


list = [4, 7, -4, 2, 5, 6, 4, 10, 9]
print(list)
new_list = []
i = 0
j = -1
while i < len(list) / 2:
    new_list.append(list[i] * list[j])
    i = i + 1
    j = j - 1

print(new_list)
