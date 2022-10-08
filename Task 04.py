#  Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

number = int(input("Введите число: "))

list_numbers = list(range(1, number+1))
for elem in list_numbers:
    if elem % 2 == 0:
        print(elem, end=" ")