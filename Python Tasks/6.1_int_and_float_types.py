# Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
# На вход программе подаётся два числа с плавающей точкой – длины катетов, каждое на отдельной строке
num1, num2 = float(input()), float(input())
S = 1/2 * num1 * num2
print(S)


# Две старушки идут навстречу друг другу с постоянными скоростями v1 и v2 км/ч.
# Определите, через какое время старушки встретятся, если расстояние между ними равно S км.
# На вход программе подаются три числа с плавающей точкой v1, v2, s, каждое на отдельной строке.
S, V1, V2 = float(input()), float(input()), float(input())
T = S / (V1 + V2)
print(T)


# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему.
# Если при этом введённое с клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).
# На вход программе подается одно действительное число.
num = float(input())
if num == 0:
    print('Обратного числа не существует')
else:
    print(num ** -1)


# У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту».
# Напишите программу, которая определяет, какой температуре по шкале Цельсия соответствует указанное значение по шкале Фаренгейта.
# Используйте формулу для перевода: (см курс)
# На вход программе подаётся вещественное число градусов по шкале Фаренгейта.
F = float(input())
C = 5 / 9 * (F - 32)
print(C)


# На вход программе подается число nn – количество собачьих лет.
# Напишите программу, которая вычисляет возраст собаки в человеческих годах.
# В течение первых двух лет собачий год равен 10.510.5 человеческим годам.
# После этого каждый год собаки равен 4 человеческим годам.
# На вход программе подаётся натуральное число – количество собачьих лет.
age = int(input())
if age <= 2:
    print(age * 10.5)
else:
    print((age - 2) * 4 + 21)


# Дано положительное действительное число.
# Выведите его первую цифру после десятичной точки.
# На вход программе подается положительное действительное число.
num = float(input())
a = int(num * 10 % 10)
print(a)


# Дано положительное действительное число. Выведите его дробную часть.
# На вход программе подается положительное действительное число.
num = float(input())
a = int(num)
print(num - a)


# Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.
# На вход программе подается пять целых чисел, каждое на отдельной строке.
a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
print('Наименьшее число =', min(a, b, c, d, e))
print('Наибольшее число =', max(a, b, c, d, e))


# Напишите программу, которая упорядочивает три числа от большего к меньшему.
# На вход программе подается три целых числа, каждое на отдельной строке.
a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print(a + b + c - min(a, b, c) - max(a, b, c))
print(min(a, b, c))


# Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре.
# Напишите программу, которая определяет интересное число или нет.
# Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».
# На вход программе подается целое трехзначное число
num = int(input())
a = num // 100
b = num // 10 % 10
c = num % 10
x = max(a, b, c)
y = min(a, b, c)
if abs(x - y) == (a + b + c - x - y):
    print('Число интересное')
else:
    print('Число неинтересное')


# Даны пять чисел. Напишите программу, которая вычисляет сумму их модулей
# На вход программе подается пять действительных чисел, каждое на отдельной строке.
a1, a2, a3, a4, a5 = float(input()), float(input()), float(input()), float(input()), float(input())
print(abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5))


# Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути.
# Если только вы не умеете проходить сквозь стены, вам обязательно придется идти вдоль его параллельно-перпендикулярных улиц.
# На плоскости манхэттенское расстояние между двумя точками определяется так (см курс)
# Напишите программу определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.
# На вход программе подается четыре целых числа, каждое на отдельной строке
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
print(abs(x1 - x2) + abs(y1 - y2))
