# На вход программе подается последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является слово «КОНЕЦ» (без кавычек).
# Напишите программу, которая выводит члены данной последовательности.
text = input()
while text != 'КОНЕЦ':
    print(text)
    text = input()


# На вход программе подается последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является слово «КОНЕЦ» или «конец» (большими или маленькими буквами, без кавычек).
# Напишите программу, которая выводит члены данной последовательности.
text = input()
while text != 'КОНЕЦ' and text != 'конец':
    print(text)
    text = input()


# На вход программе подается последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является одно из трех слов: «стоп», «хватит», «достаточно» (маленькими буквами, без кавычек).
# Напишите программу, которая выводит общее количество членов данной последовательности.
counter = 0
text = input()
while text not in('стоп', 'хватит', 'достаточно'):
    counter += 1
    text = input()
print(counter)


# На вход программе подается последовательность целых чисел, делящихся на 7, каждое число на отдельной строке.
# Концом последовательности является любое число не делящееся на 7.
# Напишите программу, которая выводит члены данной последовательности.
num = int(input())
while num % 7 == 0:
    print(num)
    num = int(input())


# На вход программе подается последовательность целых чисел, каждое число на отдельной строке.
# Концом последовательности является любое отрицательное число.
# Напишите программу, которая выводит сумму всех членов данной последовательности.
total = 0
num = int(input())
while num >= 0:
    total += num
    num = int(input())
print(total)


# На вход программе подается последовательность целых чисел от 1 до 5, характеризующее оценку ученика,
# каждое число на отдельной строке. Концом последовательности является любое отрицательное число,
# либо число большее 5. Напишите программу, которая выводит количество пятерок.
counter = 0
num = int(input())
while 1 <= num <=5:
    print(num)
    if num == 5:
        counter += 1
    num = int(input())
print(counter)


# Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево,
# к тому же ведьмак не принимает купюры, он принимает только чеканные монеты.
# В мире ведьмака существуют монеты с номиналами 1,5,10,25.
# Напишите программу, которая определяет какое минимальное количество чеканных монет нужно заплатить ведьмаку.
counter = 0
price = int(input())
while price >= 25:
    counter += 1
    price -= 25
while price >= 10:
    counter += 1
    price -= 10
while price >= 5:
    counter += 1
    price -= 5
while price >= 1:
    counter += 1
    price -= 1
print(counter)


# Дано натуральное число.
# Напишите программу, которая выводит его цифры в столбик в обратном порядке.
num = int(input())
while num != 0:
    last_digit = num % 10
    num = num // 10
    print(last_digit)


# Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.
num = int(input())
total = 0
while num > 0:
    digit = num % 10
    total = total * 10 + digit
    num = num // 10
print(total)

# or
num = int(input())
while num != 0:
    last_digit = num % 10
    num = num // 10
    print(last_digit, end= '')


# Дано натуральное число n, (n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.
n = str(int(input()))
a = max(n)
b = min(n)
print('Максимальная цифра равна', a)
print('Минимальная цифра равна', b)

# or
total = 0
largest = 0
smallest = 9
n = int(input())
while n > 0:
    total = n % 10
    if total > largest:
        largest = total
    elif total < smallest:
            smallest = total
    n = n // 10
print('Максимальная цифра равна', largest)
print('Минимальная цифра равна', smallest)


# Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
total = 0
total2 = 1
n = int(input())
lenght = len(str(n))
first_num = n // (10 ** (lenght - 1))
last_num = n % 10
sum = first_num + last_num
while n > 0:
    digit = n % 10
    total += digit
    total2 *= digit
    n = n // 10
print(total, lenght, total2, total / lenght, first_num, sum, sep='\n')


# Дано натуральное число n, (n>9).
# Напишите программу, которая определяет его вторую (с начала) цифру.
n = int(input())
lenght = len(str(n))
second_num = n % (10 ** (lenght - 1)) // 10 ** (lenght - 2)
print(second_num)

n = int(input())
while n > 9:
    x = n % 10
    n = n // 10
print(x)


# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
n = int(input())
flag = 'YES'
num = n % 10
while n > 0:
    digit = n % 10
    n = n // 10
    if digit != num:
        flag = 'NO'
print(flag)


# Дано натуральное число. Напишите программу, которая определяет,
# является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.
# "справа налево упорядоченной по неубыванию” означает что правая цифра меньше или РАВНА левой.
n = int(input())
flag = 'YES'
while n // 10 > 0:
    digit = n % 10
    if digit > (n // 10) % 10:
        flag = 'NO'
    n = n // 10
print(flag)
