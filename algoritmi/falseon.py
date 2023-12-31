'''Задача: Нахождение позиции первой ошибки в последовательности чисел

Условия:

Дана строка чисел, разделенных пробелами. Первое число в строке - количество элементов в последовательности.
Напишите функцию run, которая находит позицию первого отрицательного числа в последовательности (1-индексация).
Если все числа неотрицательные, верните 'Success'.
Позиция ошибки - это индекс первого отрицательного числа в последовательности. Если отрицательных чисел нет, верните 'Success'.
Числа могут быть любыми целыми.
Примеры:

run("10\n9 7 5 5 2 9 9 9 2 -1") возвращает 10, так как последнее число отрицательное.
run("5\n1 2 3 4 5") возвращает 'Success', так как все числа неотрицательные.
run("8\n-1 2 -3 4 -5 6 -7 8") возвращает 1, так как первое число отрицательное.
Это некоторые из возможных условий, которые вы можете использовать для задачи нахождения позиции первой ошибки в последовательности чисел.'''

n = int(input())
s = list(map(int, input().split()))
n = len(s)

d={}
def up(v):
    next=s[v]
    if next==-1:
        return 1
    if v not in d:
        d[v]=up(next)+1
    return d[v]


mx = 0
for i in range(n):
    mx = max(mx, up(i))
print(mx)