"""
Задача 2: Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

n = input('Введите число: ')
i=0 
sum=0

while i < 3:
 sum += int(n[i-1])
 i+=1
     

print('Cумма всех цифр Вашего числа равна: ', sum)