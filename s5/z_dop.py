"""Входные данные
В первой строке входного файла INPUT.TXT записано единственное число N – количество элементов массива. 
Вторая строка содержит N целых чисел, представляющих заданный массив. 
Все элементы массива разделены пробелом. Каждое из чисел во входном файле, в том числе и N, 
не превышает 100 по абсолютной величине.

Выходные данные
В единственную строку выходного файла OUTPUT.TXT нужно вывести два числа, 
разделенных пробелом: сумму положительных элементов и произведение чисел, 
расположенных между минимальным и максимальным элементами. 
Значения суммы и произведения не превышают по модулю 10000."""

N = int(input())
a = [int(i) for i in input().split()]
flag = True
max = max(a)
max1=0
min = min(a)
min1=0
sum = 0
mult = 1

for i in range(N):
    if a[i-1] > 0:
        sum += a[i-1]
    if a[i-1] == max:
        max1 = i
    if a[i-1] == min:
        min1 = i
    if a[i-1]>100 or a[i-1]*-1>100:
        flag==False

if min1>max1:
    min=max1
    max1=min1
    min1=min

"""print (*a,'           ', min, max, min1, max1)"""
"""Почему-то минимальное значение 0, при чем вторая задача решается"""

for i in range(min1+1,max1,1):
    mult=mult*a[i-1]

if (flag==True) and (sum<=10000 or mult<=10000) and (sum*-1<=10000 or mult*-1<=10000):
    print(f"{sum} {mult}")
else:
    print('Значения по модулю превышают 100, либо сумма/произведение превышет по модулю 10000')