# Цель: применить навыки создания цикла while, а так же применения операторов break и continue.
# Задача "Нули ничто, отрицание недопустимо!":
# Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите отрицательное или не закончится список (выход за границу).
# Пункты задачи:
# 1. Запишите исходный список в переменную my_list.
# 2. Напишите цикл while с соответствующими задаче условиями.
# 3. Используйте операторы прерывания/продолжения цикла в соответствии с условиями задачи.
counter = 0
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count_my_list = len(my_list)
while counter < count_my_list:
    if my_list[counter] < 0:
        break
    elif my_list[counter] > 0:
        print(my_list[counter])
        counter = counter + 1
    else:
        counter = counter + 1
        continue

