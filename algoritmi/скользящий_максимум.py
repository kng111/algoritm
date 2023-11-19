'''
Условие задачи: Максимум в скользящем окне

Ввод:

    Число n (1 ≤ n ≤ 10^5) - количество элементов в последовательности.
    n чисел, разделенных пробелами - элементы последовательности.
    Число k (1 ≤ k ≤ n) - размер скользящего окна.
Вывод:

    Для каждого положения окна выведите максимальный элемент внутри окна.
    Примеры:
        Пример ввода:
            3
            2 1 5
            1
        Пример вывода:
            2 1 5
        Пример ввода:
            8
            2 7 3 1 5 2 6 2
            4
        Пример вывода:
            7 7 5 6 6

Примечание:
    Последовательность должна быть просмотрена поочередно для каждого положения окна размера k.
    Выводить максимальный элемент внутри окна для каждого положения окна.
'''

n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
if m == 1:
    print(*a)
else:
    b = [0]*n
    c = [0]*n
    for i in range(n):
        b[i] = max(a[i], b[i - 1]) if (i % (m-1)) else a[i]
    c[-1]=a[-1]
    for i in range(n-2,-1,-1):
        c[i] = max(a[i], c[i + 1]) if ((i + 1) % (m-1)) else a[i]
    for i in range(n-m+1):
        print(max(c[i], b[i + m - 1]), end=' ')