# Напишите программу, которая сравнивает пароль и его подтверждение. Если они совпадают,
# то программа выводит: «Пароль принят», иначе: «Пароль не принят».
# На вход программе подаются две строки.
# password_1, password_2 = input(), input()
# if password_1 == password_2:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')


# Напишите программу, которая определяет, является число четным или нечетным.
# На вход программе подаётся одно целое число.
# x = int(input())
# if x % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')


# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение:
# сумма первой и последней цифр равна разности второй и третьей цифр.
# На вход программе подаётся одно целое положительное четырёхзначное число.
# num = int(input())
# a = num // 1000
# b = num // 100 % 10
# c = num // 10 % 10
# d = num % 10
# if a + d == b - c:
#     print('ДА')
# else:
#     print('НЕТ')


# Напишите программу, которая определяет, разрешен пользователю доступ к интернет-ресурсу или нет.
# На вход программе подаётся целое число — возраст пользователя.
# Программа должна вывести текст «Доступ разрешен» если возраст не менее 18, и «Доступ запрещен» в противном случае.
# age = int(input())
# if age >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')


# Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке)
# последовательными членами арифметической прогрессии.
# На вход программе подаются три числа, каждое на отдельной строке.
# a, b, c = int(input()), int(input()), int(input())
# if b - a == c - b:
#     print('YES')
# else:
#     print('NO')


# Напишите программу, которая определяет наименьшее из двух чисел.
# На вход программе подаётся два различных целых числа.
# a, b = int(input()), int(input())
# if a < b:
#     print(a)
# else:
#     print(b)


# Напишите программу, которая определяет наименьшее из четырёх чисел.
# На вход программе подаётся четыре целых числа.
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a <= b:
#     x = a
# else:
#     x = b
# if c <= d:
#     y = c
# else:
#     y = d
# if x < y:
#     print(x)
# else:
#     print(y)


# Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:
# до 13 включительно – детство;
# от 14 до 24 – молодость;
# от 25 до 59 – зрелость;
# от 60 – старость.
# На вход программе подаётся одно целое число – возраст пользователя.
# age = int(input())
# if age <= 13:
#     print('детство')
# elif 14 <= age <= 24:
#     print('молодость')
# elif 25<= age <= 59:
#     print('зрелость')
# else:
#     print('старость')


# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.
# На вход программе подаются три целых числа.
# a, b, c = int(input()), int(input()), int(input())
# if a <= 0:
#     a = 0
# else:
#     a = a
# if b <= 0:
#     b = 0
# else:
#     b = b
# if c <= 0:
#     c = 0
# else:
#     c = c
# print(a + b + c)


