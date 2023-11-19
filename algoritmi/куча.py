'''Условие задачи: Построение кучи
Ввод:
Число n (1 ≤ n ≤ 10^5) - количество элементов в массиве.
n чисел, разделенных пробелами - элементы массива.
Вывод:
Минимальное количество обменов элементов массива, необходимых для того, чтобы превратить данный массив в кучу.
Примеры:


Пример ввода:
6
0 1 2 3 4 5
Пример вывода:
0


Пример ввода:
6
7 6 5 4 3 2
Пример вывода:
4
2 5
1 4
0 2
2 5


Примечание:

Построение кучи происходит путем проведения операций "просеивания вниз" (sift-down) для некоторых вершин дерева. Количество операций выводится в выводе.
Нулевой индекс массива в данной задаче игнорируется (т.е., элементы массива находятся в индексах от 1 до n). '''




def build_min_heap(arr):
    def sift_down(j):
        min_index, left, right = j, 2*j+1, 2*j+2
        if left < size and arr[left] < arr[min_index]:
            min_index = left
        if right < size and arr[right] < arr[min_index]:
            min_index = right
        if j != min_index:
            arr[j], arr[min_index] = arr[min_index], arr[j]
            operations.append([j, min_index])
            sift_down(min_index)

    operations = []
    size = len(arr)
    i = size//2-1
    while i >= 0:
        sift_down(i)
        i -= 1
    return operations

input()
arr = list(map(int, input().split()))
operations = build_min_heap(arr)
print(len(operations))
for op in operations:
    print(*op)