# На вход программе подается строка состоящая из имени и фамилии человека, разделенных одним пробелом.
# Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.
# Программа должна вывести «YES» если имя и фамилия начинаются с заглавной буквы и «NO» в противном случае.
s = input()
if s in s.title():
    print('YES')
else:
    print('NO')


# На вход программе подается строка.
# Напишите программу, которая меняет регистр символов, другими словами замените все строчные символы заглавными и наоборот.
s = input()
print(s.swapcase())


# На вход программе подается строка текста.
# Напишите программу, которая определяет является ли оттенок текста хорошим или нет.
# Текст имеет хороший оттенок, если содержит подстроку «хорош» во всевозможных регистрах.
# Программа должна вывести «YES» если текст имеет хороший оттенок и «NO» в противном случае.
s = input()
if 'хорош' in s.lower():
    print('YES')
else:
    print('NO')


# На вход программе подается строка.
# Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.
s = input()
counter = 0
for i in range(len(s)):
    if 'a' <= s[i] <= 'z':
        counter += 1
print(counter)


# На вход программе подается строка текста, состоящая из слов, разделенных ровно одним пробелом.
# Напишите программу, которая подсчитывает количество слов в ней.
s = input()
print(s.count(' ') + 1)


# На вход программе подается строка генетического кода,
# состоящая из букв А (аденин), Г (гуанин), Ц (цитозин), Т (тимин).
# Напишите программу, которая подсчитывает сколько аденина, гуанина, цитозина
# и тимина входит в данную строку генетического кода.
# На вход программе подается строка генетического кода, состоящая из символов А, Г, Ц, Т, а, г, ц, т.
s = input().lower()
print('Аденин:', s.count('а'))
print('Гуанин:', s.count('г'))
print('Цитозин:', s.count('ц'))
print('Тимин:', s.count('т'))


# Джим Хоппер с помощью радиоприемника пытается получить сообщение Оди.
# На приемник ему поступает nn различных последовательностей кода Морзе.
# Декодировав их, он получает последовательности из цифр и строчного латинского алфавита,
# при этом во всех сообщениях Оди содержится число 11, причем минимум 3 раза.
# Помогите определить Джиму количество сообщений от Оди.
# В первой строке подаётся число nn – количество сообщений,
# в последующих nn строках вводятся строки, содержащие латинские строчные буквы и цифры.
# Программа должна вывести количество строк в которых содержится число 11 минимум 3 раза.
# Числа 11 необязательно должны быть разделены другими символами,
# нужно подсчитать вхождение последовательности символов "11", т.е. например
# в строке "111" содержится одна такая последовательность, в то время как в "1111" их уже две.
n = int(input())
total = 0
for i in range(n):
    x = input()
    counter = 0
    a = x.count('11')
    if a >= 3:
        counter += 1
        if counter >= 1:
            total += 1
print(total)


# На вход программе подается строка текста.
# Напишите программу, которая подсчитывает количество цифр в данной строке.
s = input()
counter = 0
for i in range(len(s)):
    if s[i] in '0123456789':
        counter += 1
print(counter)


# На вход программе подается строка текста.
# Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru
# Программа должна вывести «YES» если введенная строка заканчивается подстрокой .com или .ru и «NO» в противном случае.
s = input()
if s.endswith('.com') or s.endswith('.ru'):
    print('YES')
else:
    print('NO')


# На вход программе подается строка текста.
# Напишите программу, которая выводит на экран символ, который появляется наиболее часто.
# Текст может содержать строчные и заглавные буквы английского и русского алфавита, а также цифры.
# Если таких символов несколько, следует вывести последний по порядку символ.
# Следует различать заглавные и строчные буквы, а также буквы русского и английского алфавита.
s = input()
x = 0
maxi = 0
for i in s:
    if s.count(i) >= maxi:
        maxi = s.count(i)
        x = i
print(x)


# На вход программе подается строка текста.
# Если в этой строке буква «f» встречается только один раз, выведите её индекс.
# Если она встречается два и более раз, выведите индекс её первого и последнего вхождения на одной строке,
# разделенных символом пробела. Если буква «f» в данной строке не встречается, следует вывести «NO».
s = input()
if s.count('f') > 1:
    print(s.find('f'), s.rfind('f'))
elif s.count('f') == 1:
    print(s.find('f'))
else:
    print('NO')


# На вход программе подается строка текста, в которой буква «h» встречается минимум два раза.
# Напишите программу, которая удаляет из этой строки первое и последнее вхождение буквы «h», а также все символы,
# находящиеся между ними.
s = input()
x = s.find('h')
y = s.rfind('h')
print(s[:x] + s[y + 1:])
