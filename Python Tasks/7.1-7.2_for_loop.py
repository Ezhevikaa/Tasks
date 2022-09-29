# Напишите программу, которая выводит слова «Python is awesome!» (без кавычек) 10 раз
# for i in range(10):
#     print('Python is awesome!')


# Дано предложение и количество раз которое его надо повторить.
# Напишите программу, которая повторяет данное предложение нужное количество раз.
# В первой строке записано текстовое предложение, во второй — количество повторений.
# a = input()
# for i in range(int(input())):
#     print(a)


# Напишите программу, которая использует ровно три цикла for
# для печати следующей последовательности символов (см курс):
# for i in range(6):
#     print('AAA')
# for i in range(5):
#     print('BBBB')
# print('E')
# for i in range(9):
#     print('TTTTT')
# print('G')



# На вход программе подается натуральное число n.
# Напишите программу, которая печатает звездный прямоугольник размерами n×19.
# На вход программе подаётся натуральное число n∈[1;20] — высота звездного прямоугольника.
# Программа должна вывести звездный прямоугольник размерами n×19.
# Для печати звездной линии используйте умножение строки на число.
# n = int(input())
# for i in range(n):
#     print('*' * 19)


# Напишите программу, которая считывает одну строку текста и выводит 10 строк,
# пронумерованных от 0 до 9, каждая с указанной строкой текста.
# На вход программе подается одна строка текста.
# str1 = input()
# for i in range(10):
#     print(i, str1)


# На вход программе подается натуральное число n.
# Напишите программу, которая для каждого из чисел от 0 до n (включительно) выводит фразу:
# «Квадрат числа [число] равен [число]» (без кавычек).
# n = int(input())
# for i in range(n + 1):
#     print('Квадрат числа', i, 'равен', (i ** 2))


# На вход программе подается натуральное число n, (n≥2) – катет прямоугольного равнобедренного треугольника.
# Напишите программу, которая выводит звездный треугольник в соответствии с примером.
# n = int(input())
# for i in range(n):
#     print((n - i) * '*')


# На вход программе подается три натуральных числа m,p,n:
# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения.
# Напишите программу, которая предсказывает размер популяции организмов.
# Программа должна выводить размер популяции в каждый день, начиная с 1 и заканчивая n-м днем.
# m, p, n = int(input()), int(input()), int(input())
# for i in range(n):
#     print((i + 1), (m * (p/100 + 1) ** i)) #формула нахождения процента за период

# Даны два целых числа m и n ( m≤n).
# Напишите программу, которая выводит все числа от m до n включительно.
# m, n = int(input()), int(input())
# for i in range(m, n + 1):
#     print(i)


# Даны два целых числа m и n. Напишите программу, которая выводит все числа от m до n включительно в порядке возрастания,
# если m < n, или в порядке убывания в противном случае.
# m, n = int(input()), int(input())
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# else:
#     for i in range(m, n - 1, -1):
#         print(i)


# Даны два целых числа m и n (m > n).
# Напишите программу, которая выводит все нечетные числа от m до n включительно в порядке убывания.
# m, n = int(input()), int(input())
# if m % 2 == 1:
#     for i in range(m, n - 1, -2):
#         print(i)
# else:
#     for i in range(m - 1, n - 1, -2):
#         print(i)


# Даны два натуральных числа m и n (m≤n).
# Напишите программу, которая выводит все числа от m до n включительно удовлетворяющие хотя бы одному из условий:
# число кратно 17;
# число оканчивается на 9;
# число кратно 3 и 5 одновременно.
m, n = int(input()), int(input())
for i in range(m, n + 1):
    if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
        print(i)


# Дано натуральное число n.
# Напишите программу, которая выводит таблицу умножения на n.
# n = int(input())
# for i in range(1, 11):
#     print(n, 'x', i, '=', n * i)