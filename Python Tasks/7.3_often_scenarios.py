# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#
# if num == 1:
#     print('Это единица, она не простая и не составная')
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')


# На вход программе подаются два целых числа a и b (a≤b).
# Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b включительно,
# куб которых оканчивается на 4 или 9
# counter = 0
# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#     if i ** 3 % 10 in [4, 9]:    #i ** 3 % 10 == 4 or i ** 3 % 10 == 9
#         counter += 1
# print(counter)


# На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке.
# Напишите программу, которая подсчитывает сумму введенных чисел.
# total = 0
# n = int(input())
# for i in range(n):
#     num = int(input())
#     total += num
# print(total)


# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет значение выражения:
# (1+ 1/2 + 1/3 + ... + 1/n) - ln(n).
# from math import log
# total = 0
# n = int(input())
# for i in range(1, n + 1):
#     total += 1 / i
# print(total - log(n))


# На вход программе подается натуральное число n.
# Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно),
# квадрат которых оканчивается на 2,5 или 8.
# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     if i ** 2 % 10 in [2, 5, 8]:
#         total += i
# print(total)


# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет n!.
# Факториалом натурального числа n называется произведение всех натуральных чисел от 1 до n
# n = int(input())
# total = 1
# for i in range(1, n + 1):
#     total *= i
# print(total)


# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
# total = 1
# for i in range(10):
#     num = int(input())
#     if num > 0:
#         total *= num
# print(total)


# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет сумму всех его делителей.
# total = 0
# n = int(input())
# for i in range(1, n + 1):
#     if n % i == 0:
#         total += i
# print(total)


# На вход программе подается натуральное число n.
# Напишите программу вычисления знакочередующей суммы:
# 1−2+3−4+5−6+…+((−1)^n+1) * n
# n = int(input())
# total = 0
# for i in range(n):
#     if i % 2 == 0:
#         total += i + 1
#     else:
#         total -= i + 1
# print(total)


# На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке.
# Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
# largest = 1
# m_largest = 0
# n = int(input())
# for i in range(1, n + 1):
#     num = int(input())
#     if num > largest:
#         m_largest = largest
#         largest = num
#     elif num > m_largest:
#         m_largest = num
# print(largest)
# print(m_largest)


# Напишите программу, которая считывает последовательность
# из 10 целых чисел и определяет является ли каждое из них четным или нет.
# counter = 0
# for i in range(10):
#     num = int(input())
#     flag = 'NO'
#     if num % 2 == 0:
#         counter += 1
#         if counter == 10:
#             flag = 'YES'
# print(flag)


# ещё один вариант:
# counter = 0
# for i in range(10):
#     num = int(input())
#     if num % 2 == 0:
#         counter += 1
# if counter == 10:
#     print('YES')
# else:
#     print('NO')

# Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Фибоначчи.
# На вход программе подается одно число n, (n≤100) – количество членов последовательности.
# n = int(input())
# a, b = 0, 1
# for i in range(n):
#     a, b = b, a + b
#     print(a, end= ' ')
