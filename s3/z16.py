"""Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
n = 5
1 2 3 4 5
x = 3
-> 1"""

A=int(input('Введите количество элементов в массиве: '))
mass = [0]*A

for i in range(A):
    mass[i]=int(input(f'Введите {i+1}-е число: '))

X=int(input('Введите число, которое будете искать: '))

N=0

for i in range(A):
   if mass[i]==X:
        N+=1

print(f'Число "{X}" было найдено {N} раз')